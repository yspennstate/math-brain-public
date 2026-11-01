Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: 16 -> 17 genuinely distinct nonparabolic shape families; Section-B moves tried: #5 ADD A PARAMETER, #20 FIND WHY THE ALGORITHM FAILS, #29 ADD THE POINTS AT INFINITY.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Overall status: PARTIAL; the open-ended source request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 17: power-sheared parabolic tubes

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, and frozen metric

The frozen R07 metric remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo Brownian rescaling/reflection/translation and mere parameter changes inside one structural family.

The preceding authoritative own report is

`runs/R07/20260917T0822Z_i0077_periodic_one_sided_barriers_16.md`,

which moved the metric `15 -> 16` for log-periodically moving one-sided parabolic barriers and used Section-B moves `#3,#18,#27`. This run does not repeat that triple.

The new counted family is a **power-sheared parabolic tube**: the width remains exactly Brownian/parabolic scale `sqrt(u)`, but the center is translated by a genuinely different power `u^rho`. This is a center-motion phenomenon, not another aperture parameter.

The metric moves

\[
\boxed{16\longrightarrow17}.
\]

`unchanged_count = 0`.

The old R07 KPZ/FPP route remains retired by its immutable handoff; no historical R07 file was modified or deleted.

## 2. Required repository/source reread

Before new mathematics I recovered the current state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the searchable R07/I0077 chain through run 16;
- the newest visible neighboring R15 state: its distinct Burdzy–Scheutzow Problem 7.2 / I0076 already reached the six-run closable handoff, and R15 subsequently rotated through other sources rather than reopening 7.2;
- C29's earlier I0077 duplicate-exclusion report, which correctly refused to compete with R07;
- targeted intake/attempt searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

The canonical claim still names R07 as exclusive provisional owner and still says `PENDING_ADMISSION, not READY`. The latest owner instruction nevertheless assigns this exact target to R07. I do not rewrite the shared claim or fabricate READY status. `INDEX.md`/`RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8; `POSTED.md` has no Problem-7.8 exclusion; `QUEUE.md` lists I0077 distinctly. The root `RESULTS.md` R07/FPP row is stale by its own warning and is not used as the current mathematical baseline.

The large `probability_1000_intake_*/problems.jsonl` mirrors cannot be rendered wholesale through the exposed connector without truncation. This run's intake reread is therefore honestly **PARTIAL / targeted**, not described as a byte-for-byte whole-ledger read.

## 3. Primary source benchmark recovered

I rechecked the primary paper, including its FBM/decomposable-FBM definitions, the Section-4 spectral notation, Theorem 4.3, and the open-problem page.

An FBM has random witness times `S_j -> -infinity` such that, for every fixed `j`,

\[
B^{(j)}_t=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\]

is standard Brownian motion. A decomposable FBM is obtained by concatenating suitable stopped independent Brownian pieces.

For `-infinity <= c_1<c_2<=infinity`, the paper writes `lambda_0(c_1,c_2)` for the principal killed-Ornstein–Uhlenbeck exponent on `(c_1,c_2)`. Theorem 4.3 says:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM with the corresponding asymptotic normalized inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, a decomposable FBM can be confined pointwise to the exact parabolic strip for all `t<=0`.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 from parabolas to other space-time shapes. The forward-Lévy sentence following it is separately Problem 7.9.

## 4. Fresh current-status / prior-art pass — 2026-09-17

Fresh bounded searches this run included:

- exact title / arXiv ID plus `Problem 7.8` and `other space-time shapes`;
- `forward Brownian motion` plus `moving boundary`, `space-time shape`, `power boundary` and `translated square-root boundary` variants;
- later ordinary-Brownian moving-boundary work;
- standard Brownian Hölder-regularity references.

Relevant nearby literature includes Denisov–Hinrichs–Sakhanenko–Wachtel, *Crossing an Asymptotically Square-Root Boundary by the Brownian Motion* (Proc. Steklov Inst. Math. 316 (2022), 105–120), as well as the broader curved/moving-boundary first-passage literature. These concern ordinary Brownian boundary crossing and are important prior art, but they are not themselves the FBM Problem-7.8 statement.

For the seam argument below I use the classical path theorem that, for every `alpha<1/2`, a standard Brownian path is almost surely locally `alpha`-Hölder at **every** finite time. A convenient reference is Mörters–Peres, *Brownian Motion*, Corollary 1.20 and Remark 1.21.

I found no later paper in this bounded dated search explicitly resolving Burdzy–Scheutzow Problem 7.8 or stating the power-sheared FBM theorem below. This is **negative search evidence only; publication novelty remains UNVERIFIED**.

## 5. Section-B move #5 — ADD A PARAMETER: shear a parabola through the Brownian exponent

Fix finite constants

\[
c_1<c_2,\qquad \mu\ne0,\qquad \rho>0.
\]

Define

\[
\boxed{
\mathcal S_{\rho,\mu;c_1,c_2}
=
\left\{(-u,x):u>0,\
\mu u^\rho+c_1\sqrt u
\le x\le
\mu u^\rho+c_2\sqrt u
\right\}\cup\{(0,0)\}.
}
\tag{5.1}
\]

The cross-section has the same width `(c_2-c_1)sqrt(u)` as a source parabola, but its center is sheared by `mu u^rho`.

At the unique critical value `rho=1/2`, the shear is itself parabolic and (5.1) is exactly the source strip with endpoints `c_1+mu,c_2+mu`. Away from `rho=1/2`, the shape is genuinely nonparabolic.

The new question is therefore not whether changing the width helps, but whether a Brownian-scale strip can **move transversely** at a non-Brownian power and still support an FBM.

## 6. Section-B move #29 — ADD THE POINTS AT INFINITY: logarithmic compactification exposes the two obstructions

Normalize by Brownian scale and put `r=log u`. The center becomes

\[
s_\rho(r)
=\frac{\mu u^\rho}{\sqrt u}
=\mu e^{(\rho-1/2)r}.
\tag{6.1}
\]

The two ends `r=-infinity` and `r=+infinity` are the seam `u downarrow0` and the far past `u to infinity`.

- If `rho<1/2`, then `s_rho(r)` diverges at the **seam** but tends to zero in the **far past**.
- If `rho>1/2`, then `s_rho(r)` tends to zero at the seam but diverges in the **far past**.
- If `rho=1/2`, the normalized center is constant and one is back in Theorem 4.3.

This predicts a clean swap: sub-Brownian shear is asymptotically harmless at minus infinity but impossible to glue through the seam; super-Brownian shear is locally harmless at the seam but impossible in the far past.

## 7. I0077-R07-T18 — phase theorem for power-sheared parabolic tubes

**Status of theorem: PROVED below. Overall source status remains PARTIAL.**

Let `S_{rho,mu;c1,c2}` be (5.1), with `mu != 0`.

### (A) Sub-Brownian shear: `0<rho<1/2`

If

\[
\lambda_0(c_1,c_2)>1,
\]

then for every FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
\mu u^\rho+c_1\sqrt u
\le X_{-u}\le
\mu u^\rho+c_2\sqrt u
\quad\forall u\ge R
\right)=0.
}
\tag{T18-A1}
\]

If instead

\[
\lambda_0(c_1,c_2)<1,
\]

then there exists a decomposable FBM `X` for which the displayed inequalities hold for all sufficiently large `u`, almost surely.

But **regardless of `lambda_0(c_1,c_2)`**, no FBM can be confined to this tube through the seam:

\[
\boxed{
\mathbb P\left(
\exists\delta>0:\
\mu u^\rho+c_1\sqrt u
\le X_{-u}\le
\mu u^\rho+c_2\sqrt u
\quad\forall 0<u\le\delta
\right)=0.
}
\tag{T18-A2}
\]

In particular no FBM can satisfy the tube inequalities pointwise for every `u>=0`.

The critical far-past case `lambda_0(c_1,c_2)=1` is deliberately not classified here; it is not needed for the new family and no endpoint converse is invented.

### (B) Critical shear: `rho=1/2`

The tube is exactly

\[
(c_1+\mu)\sqrt u\le x\le(c_2+\mu)\sqrt u,
\]

so source Theorem 4.3 applies verbatim with shifted endpoints `c_1+mu,c_2+mu`.

### (C) Super-Brownian shear: `rho>1/2`

For every FBM `X`, irrespective of `lambda_0(c_1,c_2)`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
\mu u^\rho+c_1\sqrt u
\le X_{-u}\le
\mu u^\rho+c_2\sqrt u
\quad\forall u\ge R
\right)=0.
}
\tag{T18-C}
\]

Thus pointwise all-time confinement is impossible as well.

The theorem therefore gives a strict three-regime phase portrait: the `rho<1/2` far past retains the source OU threshold but loses pointwise gluing at the seam; `rho=1/2` is exactly the source parabola; `rho>1/2` is universally impossible in the far past.

## 8. Proof of T18(A): far-past phase is inherited when `rho<1/2`

Put

\[
s(u)=\mu u^{\rho-1/2}.
\]

For `rho<1/2`, `s(u)->0` as `u->infinity`.

### Universal obstruction when `lambda_0(c1,c2)>1`

By continuity of the principal OU exponent under endpoint perturbation, choose `epsilon>0` so small that

\[
\lambda_0(c_1-\epsilon,c_2+\epsilon)>1.
\tag{8.1}
\]

If eventual confinement to the sheared tube occurred, then for all sufficiently large `u`, `|s(u)|<epsilon/2`, and hence

\[
c_1-\epsilon/2
\le \frac{X_{-u}}{\sqrt u}
\le c_2+\epsilon/2.
\tag{8.2}
\]

It would follow that

\[
\liminf_{u\to\infty}\frac{X_{-u}}{\sqrt u}>c_1-\epsilon,
\qquad
\limsup_{u\to\infty}\frac{X_{-u}}{\sqrt u}<c_2+\epsilon.
\]

This contradicts Theorem 4.3(i) applied to `(c_1-epsilon,c_2+epsilon)`, whose exponent is still above one. This proves (T18-A1) on the universal side.

### Existence when `lambda_0(c1,c2)<1`

Again by endpoint continuity, choose `epsilon>0` with

\[
c_1+\epsilon<c_2-\epsilon,
\qquad
\lambda_0(c_1+\epsilon,c_2-\epsilon)<1.
\tag{8.3}
\]

Theorem 4.3(ii) supplies a decomposable FBM `X` satisfying

\[
\liminf_{u\to\infty}\frac{X_{-u}}{\sqrt u}\ge c_1+\epsilon,
\qquad
\limsup_{u\to\infty}\frac{X_{-u}}{\sqrt u}\le c_2-\epsilon.
\tag{8.4}
\]

Consequently, almost surely, for all sufficiently large `u`,

\[
c_1+3\epsilon/4
\le \frac{X_{-u}}{\sqrt u}
\le c_2-3\epsilon/4.
\tag{8.5}
\]

Also `|s(u)|<epsilon/2` eventually. Then the fixed inner interval in (8.5) is contained in

\[
[c_1+s(u),c_2+s(u)],
\]

which is exactly the normalized sheared tube. This proves eventual decomposable-FBM existence.

## 9. Proof of T18(A2): method #20 — the stopping-piece algorithm fails for a universal reason

The tempting algorithm is to use the source's decomposable stopping pieces and ask each Brownian reversed piece to track the center `mu u^rho` near its seam. For `rho<1/2` the failure is not merely algorithmic: it contradicts the simultaneous local regularity of every Brownian path.

Choose

\[
\rho<\alpha<1/2.
\]

A standard Brownian path is almost surely locally `alpha`-Hölder at **every** finite time. Fix an FBM witness index `j` for which `S_j<0` and put

\[
t_j=-S_j>0,
\qquad
B^{(j)}_t=X_{S_j+t}-X_{S_j}.
\]

Because `B^(j)` is standard Brownian motion, on a probability-one event there are random `C_j,delta_j>0` such that

\[
|B^{(j)}_{t_j-u}-B^{(j)}_{t_j}|
\le C_j u^\alpha
\qquad(0<u\le\delta_j).
\tag{9.1}
\]

The endpoint identity is exact:

\[
B^{(j)}_{t_j-u}-B^{(j)}_{t_j}
=X_{-u}-X_0=X_{-u},
\tag{9.2}
\]

using the source normalization `X_0=0`. Thus

\[
|X_{-u}|=O(u^\alpha)=o(u^\rho)
\quad(u\downarrow0).
\tag{9.3}
\]

But confinement to the sheared tube would give

\[
\frac{X_{-u}}{u^\rho}
\in
\left[
\mu+c_1u^{1/2-\rho},
\mu+c_2u^{1/2-\rho}
\right]
\longrightarrow\{\mu\},
\tag{9.4}
\]

and `mu != 0`, contradicting (9.3).

There is no random-time independence issue. For every fixed witness index `j`, `B^(j)` is a standard Brownian path, and the Hölder theorem is simultaneous over **all** of its finite times. Since `S_j->-infinity`, a witness with `S_j<0` exists almost surely; equivalently one may take a countable union over fixed indices. This proves (T18-A2).

The precise obstruction is therefore now identified: a sub-Brownian center shear is **larger than the local Brownian increment scale** at the seam even though it disappears after far-past normalization.

## 10. Proof of T18(C): super-Brownian center drift beats every FBM in the far past

Assume `rho>1/2`. Let

\[
M=\max(|c_1|,|c_2|).
\]

Because `sqrt(u)=o(u^rho)`, for all sufficiently large `u`, confinement would imply

\[
|X_{-u}|
\ge |\mu|u^\rho-M\sqrt u
\ge \frac{|\mu|}{2}u^\rho.
\tag{10.1}
\]

Suppose, toward contradiction, that eventual confinement has probability `q>0`. By increasing a deterministic `R_0` if needed, there is an event `E` of probability `q_0>0` on which the tube inequalities hold for every `u>=R_0` and (10.1) is valid there.

For standard Brownian motion `B`, the ordinary LIL implies

\[
\frac{|B_t|}{t^\rho}\longrightarrow0
\qquad(t\to\infinity)
\tag{10.2}
\]

because `rho>1/2`. Hence the decreasing events

\[
H_A=
\left\{\exists t\ge A:
|B_t|\ge\frac{|\mu|}{2}t^\rho
\right\}
\]

satisfy `P(H_A)->0`. Choose deterministic `A>=R_0` with

\[
\mathbb P(H_A)<q_0/4.
\tag{10.3}
\]

Let `S_j` be the FBM witness sequence. Since `S_j->-infinity` almost surely, choose one **deterministic index** `j` so large that

\[
\mathbb P(-S_j<A)<q_0/4.
\tag{10.4}
\]

For this fixed `j`,

\[
B^{(j)}_r=X_{S_j+r}-X_{S_j}
\]

is standard Brownian motion. At the terminal time `t=-S_j`,

\[
B^{(j)}_t=X_0-X_{S_j}=-X_{-t}.
\tag{10.5}
\]

On `E cap {-S_j>=A}`, (10.1) therefore forces

\[
|B^{(j)}_t|\ge\frac{|\mu|}{2}t^\rho
\quad\text{for some }t\ge A.
\]

This has probability at least `3q_0/4`, contradicting (10.3) because `B^(j)` has standard Brownian law. No independence between `S_j` and the Brownian witness is assumed. This proves (T18-C).

## 11. Canonical examples: same family, two opposite failures

These are examples inside one structural family and are **not** separate metric points.

### Example 1 — asymptotic YES, pointwise NO

Take

\[
\rho=1/4,\qquad\mu=1,\qquad(c_1,c_2)=(-2,2).
\]

Then

\[
\boxed{
u^{1/4}-2\sqrt u\le X_{-u}\le u^{1/4}+2\sqrt u.}
\tag{11.1}
\]

(Here and below the first `u` in (11.1) is intended; the display is `u^{1/4}` on both sides.)

The source records `lambda_0(-1,1)=1`; strict domain monotonicity gives

\[
\lambda_0(-2,2)<1.
\]

Therefore T18(A1) gives a decomposable FBM eventually inside this nonparabolic sheared tube, while T18(A2) says **no FBM at all** can satisfy it on any neighborhood of the seam `0`. This is a clean separation between far-past spectral admissibility and pointwise gluing.

### Example 2 — a subcritical aperture does not save a super-Brownian drift

Take

\[
\rho=3/4,\qquad\mu=1,\qquad(c_1,c_2)=(-2,2).
\]

Even though the underlying static aperture `[-2,2]` is source-subcritical, T18(C) says **every** FBM fails eventual confinement because the center drift `u^{3/4}` outruns Brownian scale.

These examples falsify the proposed extension “only the instantaneous aperture `c_2-c_1` and its OU exponent matter.” They do **not** refute the source's open-ended Problem 7.8.

## 12. Why this is a genuinely new metric point

Brownian scaling

\[
(t,x)\mapsto(a^2t,ax)
\]

sends the shear coefficient `mu` to another nonzero constant multiple but preserves the power `rho`. Reflection changes the sign of `mu`; time/space scaling cannot remove the `u^rho` center drift when `rho!=1/2`.

More structurally, the normalized cross-section is always a bounded interval of fixed width `c_2-c_1`, but its center is

\[
\mu u^{\rho-1/2},
\]

which diverges at exactly one endpoint of the logarithmically compactified time axis and tends to zero at the other.

This is not:

- run 3's pure-power family, which changes the **width scale** while keeping center zero;
- run 11's pinched-seam family or run 12's two-scale-aperture family, which vary the **aperture** around center zero;
- run 9's sparse drifting pulses, where large center excursions occur only on a zero-density pulse set rather than continuously at every scale;
- run 16's one-sided periodic barriers, whose normalized cross-sections are unbounded half-lines rather than bounded intervals.

Thus the frozen equivalence convention does not identify this family with any previous counted family. It contributes exactly one new point, not one per `rho`, `mu`, or endpoint choice.

## 13. What the three methods actually did

### #5 ADD A PARAMETER

Inserted a center-shear exponent `rho` and passed it through the Brownian exponent `1/2`. This produced the exact three-regime phase split and the source theorem as the critical member.

### #20 FIND WHY THE ALGORITHM FAILS

The source-style decomposable stopping-piece algorithm fails on opposite ends for opposite reasons. If `rho<1/2`, every Brownian witness is too locally regular to track the nonzero `u^rho` center through the seam. If `rho>1/2`, the center outruns the far-past Brownian scale. Both failures were promoted from algorithmic observations to universal FBM obstructions.

### #29 ADD THE POINTS AT INFINITY

Logarithmic compactification makes the normalized center `mu exp((rho-1/2)r)`. Its divergence switches from the seam endpoint to the far-past endpoint precisely at `rho=1/2`, making the proof architecture visible before calculation.

## 14. Validation / closure accounting

No finite combinatorial or arithmetic claim is central to T18, so I did **not** manufacture a checker solely to create a certificate. The theorem-sized claim is proved on the page above. Source threshold facts are imported explicitly from Theorem 4.3 and the source's OU remarks; Brownian Hölder/LIL inputs are classical and cited.

This is a self-checking research report, not an independent audit. T18 currently has:

- P26 end-to-end audit: **missing**;
- second independent OTHER-track audit: **missing**;
- publication novelty: **UNVERIFIED**;
- source status: **PARTIAL**, because Problem 7.8 is open-ended and R07 has proved another family rather than a universal characterization of all shapes.

Therefore no closure label and no `paper_*` folder are created this run.

## 15. Model / scheduler control — actual state

The installed instruction requests GPT-6 with maximum reasoning, but this run actually identifies as **GPT-5.6 Sol**, with reasoning level **UNVERIFIED**. I do not claim GPT-6 maximum.

The currently exposed task-control surface provides task text/title, schedule, enablement, and timing controls. It still exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run telemetry**. Thus GPT-6/maximum remains prompt-only in this environment. Enforcing it would require the product/API to expose those fields or action from the task's authorized owning/admin context once such controls exist.

The repository records historical `You cannot modify this task` failures, including P26 in one context, and also records that P26 later succeeded from a different authorized context. The legitimate resolution is therefore the owning authorized context or platform support, not a worker-level permission bypass or duplicate task. No scheduler modification was attempted here.

## 16. Next mathematical direction

The high-value next question is no longer another easy obstruction example. T18 suggests studying **critical and near-critical center drifts**

\[
\sqrt u\,h(\log u)
\]

with `h(r)` tending to infinity or zero slower than any exponential, for example iterated-log center shears. The point is to determine whether the exact threshold is governed by a moving-OU principal Lyapunov exponent, by Brownian slow-point geometry at the seam, or by both. That would interpolate between the source parabola, the power-shear phase transition proved here, and the earlier pulse families without merely changing a parameter.

```yaml
ledger_delta:
  track: R07
  run_id: 20260917T0923Z_i0077_power_sheared_parabolic_tubes_17
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8 / I0077"
  target: "generalize Theorem 4.3 from parabolic regions to genuinely distinct nonparabolic space-time shape families"
  fixed_metric: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem, modulo frozen trivial equivalences"
  metric_before: 16
  metric_after: 17
  movement: true
  unchanged_count: 0
  new_family: "power-sheared parabolic tubes"
  theorem_id: I0077-R07-T18
  methods: [5, 20, 29]
  source_status: PARTIAL
  theorem_status: PROVED_SELF_CHECK
  critical_case_unclassified: "rho<1/2 with lambda_0(c1,c2)=1"
  finite_checker: "none; no finite computational core"
  p26_audit: missing
  second_other_track_audit: missing
  novelty: UNVERIFIED
  canonical_claim_state: PENDING_ADMISSION
  model_requested: "GPT-6 maximum"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: UNVERIFIED
  delivery: "private GitHub only"
```
