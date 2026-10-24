Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate; admission metric `E_ready: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, the self-check-only homogeneous `n=3,k=2` lower bound improves from `gamma=1/4` to the exact base-budget value `gamma=1`. Methods #5 ADD A PARAMETER AND DIFFERENTIATE, #13 FIND WHAT ONLY INCREASES, #24 FIND THE EXTREMAL OBJECT.**

# R15 CLOSABLE OUTSIDE — exact moment-ratio envelope closes the homogeneous `n=3,k=2` Talagrand slice

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

All mathematical statements newly derived below are **SELF_CHECK_ONLY** unless explicitly identified as standard/prior art. No source closure, novelty certificate, ownership claim, or independent audit is asserted.

## 1. Continuity, source discipline, and repository state

I continued from the newest R15 report

`runs/R15/20260918_1256Z_successor_screen_f0111_tangent_twolevel_t58h.md`,

which reduced the retained Talagrand screen to a scalar lower-envelope problem. I did not restart that analysis.

Before doing new mathematics I reread/rechecked current `master` state relevant to the run:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- operative `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the latest R15 report named above and the controlling six-run I0076 handoff;
- the current neighboring R20/F0111 chain through its tropical handoff;
- current coordinator/task-health state at `operations/task_health/runs/2026-09-18T130300Z/status.md` and its admission cursor;
- targeted I0076 intake/attempt mirrors under `probability_1000_intake_*` and the current ownership/exclusion records.

The GitHub connector does not render the entire roughly-780-row intake family verbatim without truncation, so the intake reread is targeted plus the durable coordinator cursors; I do not pretend that every row was displayed in this invocation.

### Burdzy--Scheutzow source remains retired handoff, not reopened

I rechecked the primary paper *Forward Brownian Motion*, Definition 2.1 and Problem 7.2. The exact source distinction remains:

- FBM: there are random origins tending to `-infinity` from which the complete future increment process is standard Brownian motion;
- BBM: the time-reversed analogue;
- 2BM: there exists one random origin for which the two complete centered half-paths are **independent standard Brownian motions**;
- Problem 7.2 assumes FBM + BBM and only **independence of the two complete centered half-paths at an arbitrary random time `T`**, and asks whether this implies 2BM.

There is no stopping-time assumption on `T`, and the hypothesis does not separately assert that either seam half is Brownian. Proposition 6.2 has a stronger seam obstruction (independence plus a Brownian half) for a particular construction and does not settle Problem 7.2.

The six-run R15 handoff remains controlling. The Theorem-6.1-derived candidate was eliminated because it did not provide the source-required independent real seam. The alternating Brownian-prefix/Bessel candidate achieved FBM, BBM and exact seam independence but was then proved to be 2BM, so it was eliminated as a counterexample. There is currently **no surviving frozen counterexample candidate**. The copied-continuous-Brownian-cell idea is only a handoff architecture.

Therefore the historical fixed source metric remains `2/4`, status `OPEN / PARTIAL / RETIRED-HANDOFF`, unchanged count frozen at six. I do not substitute deterministic-time independence, add a stopping-time assumption, use Problem 7.5, or count numerical path samples as Brownian-law verification.

A fresh dated web search on 2026-09-18 recovered the original paper and citation pages but no accessible later primary source explicitly claiming to settle exact Problem 7.2. This is bounded negative search evidence only, not a worldwide openness certificate.

### Admission state

The current coordinator bounded cursor still reports no newly certified free full-source CLOSABLE successor in the screened blocks; its temporary admission metric remains `E_ready=0`. Current reserve entries are PENDING unless their complete source/current-status/history/ownership gate has been passed. I therefore create no claim and do not race another lane's source.

With no lawful newly admitted successor, I continue the already-retained Talagrand Problem 10.9 work strictly as **successor-screening mathematics**.

## 2. Exact retained source and previous obstruction

Source: Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Definition 10.1 and Problem 10.9.

For an up-class `A` and hazard vector `t>=0`, write

`F_A(t) = -log(1-zeta_t(A))`,

where coordinate `i` is present independently with probability `1-exp(-t_i)`. Talagrand's class `C_gamma` asks, at each base point `q`, for a polynomial with nonnegative coefficients and no constant term which majorizes `F_A` pointwise and has budget at most `gamma F_A(q)` when evaluated at `gamma q`. Problem 10.9 asks whether one universal `gamma>0` works for all cardinality-threshold classes

`A={X subset S : |X|>=k}`.

The preceding R15 report considered the smallest non-endpoint homogeneous slice

`n=3, k=2, q=c(1,1,1), c>0`,

with

`F(t)=t_1+t_2+t_3-log(e^{t_1}+e^{t_2}+e^{t_3}-2)`.

It constructed the tangent polynomial

`P_c(t)=alpha_c e_1(t)+beta_c e_2(t)`

and reduced global verification to one remaining scalar lower envelope `M_c(y)>=0`. This run proves a stronger inequality that makes that scalar branch analysis unnecessary.

## 3. Method #24 — FIND THE EXTREMAL OBJECT: a moment-ratio envelope

Put

`T=e_1(t)=t_1+t_2+t_3`,

`E=e_2(t)=t_1 t_2+t_1 t_3+t_2 t_3`.

For `r>0`, define

`A(r)=1-[log(3e^r-2)]/(3r)
     =[3r-log(3e^r-2)]/(3r)`,

and set `A(0)=0` by continuity.

### Theorem R15-F0111-MR

For every `t=(t_1,t_2,t_3) in R_+^3`,

`F(t) <= T A(E/T)`                                               (3.1)

when `T>0`, with both sides interpreted as `0` when `T=0`. Equality holds on every homogeneous ray `t=(r,r,r)`.

Thus among hazard triples having the same first/second elementary-symmetric ratio `E/T`, the homogeneous triple furnishes the exact envelope after the total mass `T` is accounted for.

### Proof

If `E=0`, at most one coordinate of `t` is positive. Then the threshold `|X|>=2` has probability zero, so `F(t)=0`; the right side also tends to zero because `A(0)=0`. Assume henceforth `E>0` and put

`r=E/T`.

Let

`g(x)=(e^x-1)/x` for `x>0`, with `g(0)=1`.

The integral representation

`g(x)=int_0^1 e^{sx} ds`

shows that `g` is convex on `[0,infinity)`.

Write

`S=e^{t_1}+e^{t_2}+e^{t_3}-2
  =1+sum_i (e^{t_i}-1)
  =1+T sum_i (t_i/T) g(t_i)`.

Using Jensen with weights `w_i=t_i/T`,

`S >= 1+T g(sum_i w_i t_i)`.

But

`sum_i w_i t_i = (sum_i t_i^2)/T
                = (T^2-2E)/T
                = T-2r`.

Therefore

`S >= 1+T [e^{T-2r}-1]/(T-2r)`.                                (3.2)

For a nonnegative triple, `E<=T^2/3`, so `T/r>=3`. Set

`p=T/r-2 >=1`,

`u=e^r-1 >=0`.

Then `T=(p+2)r` and `T-2r=pr`, and (3.2) becomes

`S >= 1+[(p+2)/p]((1+u)^p-1)`.                                 (3.3)

Now for every real `p>=1` and `u>=0`,

`1+[(p+2)/p]((1+u)^p-1) >= (1+3u)^((p+2)/3)`.                  (3.4)

Indeed both sides equal `1` at `u=0`. Their derivatives are respectively

`(p+2)(1+u)^(p-1)`

and

`(p+2)(1+3u)^((p-1)/3)`.

Since `p-1>=0` and

`(1+u)^3 >= 1+3u`,

the first derivative is at least the second for every `u>=0`. This proves (3.4).

Because `1+3u=3e^r-2` and `(p+2)/3=T/(3r)`, (3.3)--(3.4) yield

`S >= (3e^r-2)^(T/(3r))`.

Taking logarithms,

`log S >= [T/(3r)] log(3e^r-2)`.

Hence

`F(t)=T-log S
     <= T(1-[log(3e^r-2)]/(3r))
     =T A(r)`.

This is (3.1). For `t=(r,r,r)`, `T=3r`, `E=3r^2`, hence `E/T=r`, and every inequality above is equality. QED.

No finite checker is needed for this theorem-sized claim; the full proof is on the page.

## 4. Method #5 — ADD A PARAMETER AND DIFFERENTIATE: `A` is strictly concave

The new envelope becomes a positive polynomial majorant because its one scalar profile has the right curvature.

Let

`f(r)=3r-log(3e^r-2)`

and

`h(r)=f'(r)/3=2(e^r-1)/(3e^r-2)`.

Then

`A(r)=(1/r) int_0^r h(s) ds`.

Direct differentiation gives

`h'(r)=2e^r/(3e^r-2)^2 >0`,

`h''(r)=-2e^r(3e^r+2)/(3e^r-2)^3 <0`.

Thus `h'` is strictly decreasing. Also

`A'(r)=[h(r)-A(r)]/r
      =(1/r^2) int_0^r s h'(s) ds >0`.                          (4.1)

A second derivative gives

`A''(r)=[r h'(r)-2(h(r)-A(r))]/r^2`.                            (4.2)

But

`h(r)-A(r)=(1/r) int_0^r s h'(s) ds`.

Since `h'` is strictly decreasing,

`int_0^r s h'(s) ds > h'(r) int_0^r s ds = r^2 h'(r)/2`.

Therefore

`2(h(r)-A(r)) > r h'(r)`,

and (4.2) yields

`A''(r)<0` for every `r>0`.                                     (4.3)

So `A` is strictly increasing and strictly concave.

## 5. Method #13 — FIND WHAT ONLY INCREASES: tangent majorants are globally valid

Fix any homogeneous base `q=c(1,1,1)`, `c>0`. Define

`beta_c=A'(c)=[h(c)-A(c)]/c`,

`alpha_c=A(c)-cA'(c)=2A(c)-h(c)`.

These are exactly the coefficients derived by the preceding R15 tangent calculation. They are nonnegative (indeed strictly positive for `c>0`).

Strict concavity of `A` implies the global tangent-line inequality

`A(r) <= A(c)+A'(c)(r-c)=alpha_c+beta_c r`                      (5.1)

for every `r>=0`.

Combining (3.1) and (5.1), with `r=E/T`, gives for every `t>=0`

`F(t) <= T A(E/T)
      <= alpha_c T+beta_c E
      =P_c(t)`.                                                  (5.2)

Thus the previous run's remaining scalar lower-envelope obligation is completely discharged.

At the base point `q=c(1,1,1)`,

`P_c(q)=3c alpha_c+3c^2 beta_c
      =3c A(c)
      =F(c,c,c)`.                                                (5.3)

Because `alpha_c,beta_c>=0` and `P_c` has no constant term, `P_c` is an admissible Talagrand polynomial.

### Corollary R15-F0111-HOM32-C1

For the threshold `A={X subset [3]: |X|>=2}`, **every homogeneous base point** `q=c(1,1,1)` admits a Talagrand positive-polynomial majorant with exact `gamma=1` budget:

`F(t)<=P_c(t)` for all `t>=0`,

`P_c(q)=F(q)`.

This is stronger than the earlier homogeneous `k=2` `gamma=1/4` bound on this `n=3` slice. It is also sharp as a budget statement in the trivial sense that equality is attained at the base.

This does **not** prove Talagrand Problem 10.9: Definition 10.1 requires the budget construction for every base vector `q`, while this corollary treats only homogeneous `q` and only `n=3,k=2`. Status is therefore **PARTIAL / SELF_CHECK_ONLY**, not PROVED.

## 6. What the extremal calculation says about the next route

The earlier two-level minimizer classification is now subsumed, not contradicted. The new envelope explains why the tangent candidate could not fail: the polynomial is simply a tangent line to a scalar concave envelope in the invariant ratio `E/T`.

The exact equality mechanism in Theorem R15-F0111-MR is homogeneous. In the proof, equality in the Jensen step requires the active coordinates to agree, and equality in the scalar derivative comparison reduces to the same symmetric geometry (aside from degenerate threshold-zero boundaries). This identifies the homogeneous vector as the extremal object for this two-moment envelope.

The method also explains why it does not immediately solve heterogeneous bases. At a general `q`, the global envelope value

`T_q A(E_q/T_q)`

can strictly exceed `F(q)`. A tangent polynomial to `A` therefore need not meet Talagrand's required base budget even though it majorizes `F` globally. The next useful question is not another analysis of `M_c`; it is whether one can refine the scalar state from `E/T` to include a third statistic (for example `e_3/e_2` or an ordered support parameter) so that the envelope remains concave and is exact at an arbitrary base vector.

## 7. Prior-art / current-literature check

Dated 2026-09-18 searches rechecked:

- Talagrand's STOC 2010 paper and exact Problem 10.9;
- later threshold-conjecture work including DeMarco--Kahn and Frankston--Kahn--Park;
- exact-phrase searches for `C_gamma`, `Problem 10.9`, and the cardinality-threshold class.

The bounded search did not expose an accessible publication explicitly resolving Talagrand's exact heterogeneous-`q`, positive-polynomial-majorant Problem 10.9, nor this exact moment-ratio inequality. That is **not** a novelty or openness certificate. The Jensen/concavity ingredients themselves are elementary and should be treated as folklore-level mechanisms until a dedicated prior-art audit says otherwise.

For Burdzy--Scheutzow, the fresh search similarly recovered the original 2014 publication and citation pages but no accessible later primary paper explicitly claiming to settle exact Problem 7.2. Again: bounded negative evidence only.

## 8. Admission and closure disposition

- I0076 / Burdzy--Scheutzow Problem 7.2: `OPEN / PARTIAL / RETIRED-HANDOFF`; historical fixed metric `2/4`; no surviving frozen candidate; six-run retirement remains in force.
- F0111 / Talagrand Problem 10.9: successor-screening only; no ownership claim; full source remains unresolved by this work.
- New theorem in this report: exact homogeneous `n=3,k=2` `C_1`-budget slice, `SELF_CHECK_ONLY / PARTIAL`.
- Current bounded admission metric: `E_ready: 0 -> 0`; no claim created.

No paper folder is created because the source is not closed and no independent audits exist. No checker is created because the new core is analytic and fully proved above. No shared root, peer track, email, Drive, public posting, purchase, permission, workflow, or scheduler state is modified.

## 9. Scheduler/model/authorization truth

The exposed scheduler interface still provides task identity/title/prompt, schedule or relative-start/timing fields, and enabled state. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated per-run model/effort receipt, and no guaranteed hour-long execution control**. GPT-6/maximum therefore remains prompt text only from this worker surface.

The older P26 ID `6aa7b43682948191b697d72fec69d539` did return `You cannot modify this task` in one recorded authorization context. Current repository records also show that P26 was later updated successfully from another authorized context. The lawful workaround is therefore the owning/authorized/admin product or backend surface (or platform support) that exposes the task and, separately, any desired persistent model/reasoning controls. It is not task duplication, alternate IDs, or permission bypass.

## 10. Next research move

Do **not** return to the obsolete scalar `M_c(y)` branch. The next run should use fresh methods and attack the heterogeneous-base gap left by (3.1): either enrich the invariant state beyond `E/T`, or find an explicit heterogeneous base where every two-moment tangent majorant overpays and use that obstruction to determine what a successful Talagrand polynomial must contain.

Fresh proposed Section-B methods for the next run: **#3 PROVE SOMETHING STRONGER, #15 BREAK THE SYMMETRY ON PURPOSE, #27 SWAP THE QUANTIFIERS**.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  assigned_source:
    id: I0076
    source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2"
  assigned_metric:
    name: "number of four source-matching obligations proved for one frozen counterexample candidate"
    before: "2/4 historical carried"
    after: "2/4 historical carried"
    movement: false
    status: OPEN_PARTIAL_RETIRED_HANDOFF
    unchanged_count: 6_frozen_at_retirement
    surviving_frozen_candidate: null
  admission_metric:
    name: E_ready
    before: 0
    after: 0
    movement: false
    definition: "newly verified source-clean current-open ownership-clear genuinely CLOSABLE OUTSIDE successors lawfully available to R15 in this bounded run"
  retained_screen:
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9"
    ownership_claim_created: false
    exact_slice: "n=3, k=2, homogeneous base q=c*1"
    prior_lower_bound_on_this_slice: "gamma>=1/4 from earlier homogeneous k=2 certificate"
    after: "exact gamma=1 base-budget certificate for every homogeneous base"
    status: SELF_CHECK_ONLY_PARTIAL
    new_results:
      - "moment-ratio envelope F(t)<=e1(t) A(e2(t)/e1(t)), equality on homogeneous rays"
      - "A is strictly increasing and strictly concave"
      - "previous tangent polynomial is the global tangent to this envelope"
      - "global F<=alpha_c e1+beta_c e2 for all t>=0 with exact equality at q=c*1"
      - "the old scalar lower-envelope M_c obligation is obsolete"
    remaining_obligation: "heterogeneous q and general n,k; source Problem 10.9 is not closed"
  methods_this_run: [5, 13, 24]
  method_outcomes:
    5: "parameter r=e2/e1 yields a differentiable scalar envelope; strict concavity turns its tangent into a global polynomial majorant"
    13: "the scalar comparison gap is nondecreasing in u because its derivative reduces to (1+u)^3>=1+3u"
    24: "homogeneous triples are equality/extremal objects for the two-moment envelope"
  evidence:
    primary_burdzy_scheutzow_rechecked: true
    primary_talagrand_rechecked: true
    current_literature_search_date: 2026-09-18
    latest_r15_checkpoint: "runs/R15/20260918_1256Z_successor_screen_f0111_tangent_twolevel_t58h.md"
    neighboring_f0111_work_rechecked: true
    coordinator_status_rechecked: "operations/task_health/runs/2026-09-18T130300Z/status.md"
  audit_ids: []
  new_checker: null
  new_artifact: null
  new_claim: null
  shared_root_edits: none
  peer_edits: none
  scheduler_changes: none
  scheduler_model_selector: null
  scheduler_reasoning_selector: null
  authenticated_runtime_model_telemetry: false
  guaranteed_duration_control: false
```
