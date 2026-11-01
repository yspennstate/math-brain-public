Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but the exposed scheduler/runtime provides no model-family selector, no reasoning-effort selector and no authenticated run telemetry, so GPT-6 maximum is not claimed. NO MOVEMENT on the fixed metric `0 -> 0`; Section-B methods actually used: #2 ATTACK THE NEGATION FIRST, #20 FIND WHY THE ALGORITHM FAILS, #22 READ THE FAILURES NOT THE SUCCESSES.**

Problem/source: David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 6.13, `tau_0` / Kemeny half only, intake I0027.

# R04 immutable run report — I0027 closure-gate audit

Run ID: `20260917T0010Z_i0027_closure_gate_audit`  
Repository/branch: `yspennstate/math-open-problems`, `master`.

## 1. Continuity and current state

I recovered the current controls before doing any new audit work: campaign `INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; `operations/NEW_METHODS_2026-09-16.md`; `operations/claims/I0027.md`; newest own report `runs/R04/20260916T2312Z_i0027_quantitative_rate.md`; newest R03 audit-bearing report `runs/R03/20260916T2337Z_22_collision_exact_crt.md`; newest R05 package `runs/R05/20260916T231500Z_i0030_n16_lazy_discrete.md`; and the newest discoverable P26 package.

The intake collection is too large to render wholesale through the connector, so I used exact I0027 / Open Problem 6.13 / owner-alias searches rather than claiming a visual reread of every intake row.

`operations/claims/I0027.md` still records R04 as exclusive provisional owner while literally saying `PENDING_ADMISSION, not READY`. I do not edit the shared claim file. `POSTED.md` does not mark the I0027 `tau_0` scope posted or settled. The retired AF4.49(ii)/C31 work remains a different source problem.

The retained source theorem is unchanged:

\[
M_n:=\max_{|V(G)|=n} K(G)=\frac{n^3}{54}+O(n^{11/4}),
\]
so in particular
\[
M_n\sim n^3/54.
\]
The frozen leading-coefficient interval remains
\[
L=U=1/54,
\qquad U-L=0.
\]

Before this run: width `0`. After this run: width `0`. **No movement.** The previous unchanged count was `2`; it is now `3`.

Mathematical status remains **PROVED_BY_R04**. Fleet/source closure remains **NOT YET** because the mandatory P26 end-to-end audit is still absent.

## 2. #2 ATTACK THE NEGATION FIRST — current-source and literature attack

I reran bounded current-literature searches on 2026-09-17 for the exact Kemeny extremal statement, the `1/54` coefficient, edge-deletion bounds, and effective-resistance decomposition routes.

The important new adjacent paper is Abiad--Carmona--Encinas--Ghorbani--Jimenez--Samperio, arXiv:2609.17481, submitted 2026-09-15 and updated 2026-09-16, *Kemeny's constant via matrix compression and eigenvalue interlacing*. Its abstract advertises lower/interlacing bounds and estimates for connectivity-preserving deletion of multiple edges. It does **not** claim the all-connected-graph maximum `M_n~n^3/54` in the abstract or surfaced metadata.

This paper is directly relevant prior art to retained C4 (sparse-deletion stability), so **novelty of C4 is not asserted** and the final paper-level prior-art review must compare its deletion theorem precisely before publication. This does not create a logical gap: R04's C4 is proved directly from the degree-weighted resistance identity and Rayleigh monotonicity and is used self-containedly.

The Alev--Anari--Lau--Oveis Gharan theorem was rechecked again: for sufficiently large `delta>1`, it removes `O(w(E)/delta)` intercluster weight while each induced cluster has effective-resistance diameter `O(delta^3 |V|/w(E))`. This remains exactly the form used by C8/C11.

No bounded search produced a published source-level resolution of the `tau_0` half or a counterexample to the R04 proof. Negative search evidence is not a novelty certificate.

## 3. #20 FIND WHY THE ALGORITHM FAILS — the only remaining closure failure is P26

The non-P26 independent audit gate has strengthened, not weakened. R03 previously passed the full mathematical source proof as

`R03-AUDIT-R04-I0027-C8-08 = PASS`.

The newest R03 report now also contains

`R03-AUDIT-R04-I0027-C11-09 = PASS`

for the quantitative strengthening. Thus a distinct OTHER-track auditor has checked both the source proof and the new rate.

A repository search for `P26-AUDIT-R04-I0027`, `P26 R04 I0027 C8`, and equivalent Kemeny audit language still finds no P26 audit of this package. The newest P26 run is instead

`P26-AUDIT-R09-TANG-Q411-PERIODIC-ENDTOEND-09 = PASS`

for Tang Question 4.11; it advances P26's package ledger on a different source. Therefore the remaining closure failure is exactly:

\[
\boxed{\text{missing mandatory P26 end-to-end audit of R04 I0027 C4/C6/C7/C8 (or C11 package).}}
\]

This is a governance/audit obligation, not a new mathematical obstruction. R04 is not authorized to edit P26's files or bypass task ownership. Consequently I do not create a paper folder, do not mark the source CLOSED, and do not disable this recurring assignment in this run.

Because the metric has now been unchanged for three consecutive runs, **the next R04 run, if P26 is still absent, must use the Section-I thinking-only stuck protocol rather than manufacture another theorem or certificate.**

## 4. #22 READ THE FAILURES — adversarial audit of the newest R05 package

The newest R05 package is `runs/R05/20260916T231500Z_i0030_n16_lazy_discrete.md`. I independently audited its new theorem R05-I0030-C14.

For a finite connected nontrivial arc-transitive `d`-regular graph, put
\[
S=A/d,\qquad Q_h=hI+(1-h)S,
\]
and for an arc `x~y`,
\[
a_m=(Q_h^m)_{xx},\qquad b_m=(Q_h^m)_{xy}.
\]
Arc-transitivity makes `a_m` vertex-independent and `b_m` arc-independent. Since `Q_h` commutes with `S`,
\[
a_{m+1}=h a_m+(1-h)b_m,
\]
so
\[
\frac{b_m}{a_m}=\frac{a_{m+1}/a_m-h}{1-h}.
\]
For `h>=1/2`, the spectrum of `Q_h` lies in `[0,1]`, hence
\[
a_m=\int q^m\,d\mu_x(q)
\]
is a Hausdorff moment sequence. Cauchy--Schwarz gives
\[
a_{m+1}^2\le a_m a_{m+2},
\]
so `a_{m+1}/a_m` and therefore `b_m/a_m` are nondecreasing. If `h>1/2`, all spectral support is positive and the local measure contains the stationary atom at `1` plus at least one distinct eigenvalue, so Cauchy--Schwarz is strict at every step.

The claimed sharpness at `h=1/2` is also correct. For `K_2`, with `c=2h-1`,
\[
r_m=\frac{1-c^m}{1+c^m},
\]
and
\[
r_1-r_2=\frac{(h-1)(2h-1)}{h(2h^2-2h+1)}>0
\]
for every `0<h<1/2`, so monotonicity fails already from step 1 to step 2. At `h=1/2`, `Q_h` is idempotent on `K_2` and the sequence is `0,1,1,...`, matching non-strict boundary monotonicity.

Independent exact checker/output:
- `artifacts/R04/20260917T0010Z_r04_r05_c14_audit_exact.py` @ `7916c5799f29f0b07030912c8993d57a18fce7a9`;
- `artifacts/R04/20260917T0010Z_r04_r05_c14_audit_exact.out` @ `3ae0ffb41f6962f0dbf20f9ba8af196f0c70504f`;
- archived terminal verdict: `AUDIT RESULT: PASS_MATH for R05-I0030-C14; novelty not audited`.

Audit ID:

`R04-AUDIT-R05-I0030-C14-20260917T0010Z = PASS_MATH / SHARPNESS_EXACT / NOVELTY_UNVERIFIED`.

This is a claim-level audit of C14, not an independent re-enumeration of the complete order-16 census metric.

## 5. Source/current-status boundary

The source remains Aldous--Fill Open Problem 6.13, `tau_0` half only. The `tau_2` half stays excluded as known from the Aksoy--Chung--Tait--Tobin relaxation-time result. The latest 2026 Kemeny papers surfaced in the bounded search concern diameter-two bounds, matrix compression/interlacing/deletion estimates, Braess phenomena, or computation; none of the surfaced source metadata claims the exact all-graph `1/54` maximum.

The mathematical source theorem is therefore still carried as R04's proof, with publication novelty **UNVERIFIED** until full prior-art review.

## 6. Model/scheduler interface

No change. The exposed scheduler mutation interface offers title, prompt, schedule/timing mode and enabled state; it exposes no model-family or reasoning-effort field. Prompt text requesting GPT-6 maximum is not authenticated runtime configuration. To change this honestly requires an authorized product/API surface exposing those settings or authenticated runtime telemetry.

A `You cannot modify this task` response is an authorization boundary. The legitimate path is the owning/admin-authorized context or platform support; there is no permission-bypass or duplicate-task workaround. Historical P26 modification failures were context-specific; repository records show a later authorized P/C context successfully updated P26. I made no scheduler changes here.

## 7. Ledger delta

```yaml
ledger_delta:
  worker: R04
  source: "Aldous-Fill Open Problem 6.13 / I0027"
  source_scope: "tau_0 / Kemeny half only"
  target: "max_G K(G) ~ n^3/54"
  metric: "width U-L of rigorous leading n^3 coefficient interval"
  before: {L: "1/54", U: "1/54", width: "0"}
  after:  {L: "1/54", U: "1/54", width: "0"}
  movement: "NO MOVEMENT"
  unchanged_count: 3
  status: "PROVED_BY_R04 / R03_ENDTOEND_PASS / P26_PENDING / NOT_FLEET_CLOSED"
  tried_moves: [2, 20, 22]
  new_r04_mathematical_claims: []
  prior_art_update:
    - "arXiv:2609.17481 has connectivity-preserving multi-edge deletion estimates; compare precisely against C4 before publication"
  audit_ids:
    - "R03-AUDIT-R04-I0027-C8-08=PASS"
    - "R03-AUDIT-R04-I0027-C11-09=PASS"
    - "P26-AUDIT-R04-I0027=PENDING"
  outgoing_audit:
    - "R04-AUDIT-R05-I0030-C14-20260917T0010Z=PASS_MATH/SHARPNESS_EXACT/NOVELTY_UNVERIFIED"
```

## 8. Next run rule

If a valid P26 end-to-end audit appears before the next invocation, consume it, verify that its scope really covers the source-closing C4/C6/C7/C8 chain, and only then create the source-matching paper folder and retire the completed assignment.

If P26 is still absent, the metric will already have three unchanged runs, so the next invocation must be a Section-I thinking-only stuck report: state the exact blocker, routes already tried, what the missing audit must independently verify, the smallest independently auditable subpackage, and the nearest existing independent audit; do not manufacture a new theorem merely to avoid the stagnation rule.
