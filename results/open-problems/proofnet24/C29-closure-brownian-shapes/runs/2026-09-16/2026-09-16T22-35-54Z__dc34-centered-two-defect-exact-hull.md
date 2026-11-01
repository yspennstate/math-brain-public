Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum, and I do not claim otherwise. **NO MOVEMENT — C29 frozen fallback metric `2 -> 2`; unchanged-run count `4 -> 5`; Section-B moves: 4, 12, 27. New PARTIAL theorem: `C29-DC34-CENTERED-TWO-DEFECT-SEMIALGEBRAIC-09 = PROVED`.**

# C29 — exact centered two-defect five-point hull

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C29-closure-brownian-shapes`.
Run date: 2026-09-16 UTC / 2026-09-17 local campaign date.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, paid compute, access change, peer-file edit, shared-ledger edit, or new schedule.

## 1. Continuity, whole-repository gate, ownership, and exclusions

I continued from the newest C29 report

`proofnet24/C29-closure-brownian-shapes/runs/2026-09-16/2026-09-16T21-37-27Z__dc34-stuck-two-defect-strategy.md`

rather than restarting the Brownian or MUB assignments. At run start I read or exact-searched the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the live C29 claim files, the newest C29 report chain, the newest R07/I0077 report, the newest C30 report, and the current C29 MUB reserve handoff. The large intake/attempt JSONL mirrors are connector-truncated; I therefore record the intake reread honestly as targeted by exact ID/source phrase rather than pretending to have rendered roughly 780 rows byte-for-byte.

### I0077 remains unavailable to C29

The canonical reservation `operations/claims/I0077.md` remains exclusively owned by R07. R07's newest report is now

`runs/R07/20260916T2124Z_i0077_positive_seam_gauges_05.md`,

which moves its own source-family metric `4 -> 5` and still labels Burdzy--Scheutzow Problem 7.8 PARTIAL. C29 therefore does not duplicate that source, does not overwrite the claim, and does not reopen already-answered Problem 7.5.

### Active C29 fallback remains RS-2026-DC34

`operations/claims/RS-2026-DC34.md` remains C29's create-only CLOSABLE OUTSIDE provisional claim, status **CLAIMED / PENDING_ADMISSION / NOT READY**. The source is Chiara Meroni's Randomstrasse Conjecture 34: a finite set may have a non-semialgebraic functional `D`-convex hull; the concrete conjectured geometry is three distinct planes in `R^3` meeting in a line.

### MUB remains HARD RESERVE

The old six-dimensional MUB attack remains untouched in `proofnet24/C29-mub-six`. Preserve exactly:

- unrestricted/full-domain normalized residual lower bound `0`;
- `11/756` only as an explicit upper benchmark, never a positive lower bound or a nonexistence proof;
- exact phase examples, cyclotomic obstructions, atlas/gauge reductions, restricted auxiliary bounds, and all failed proof routes;
- the quantifier discipline that a restricted obstruction or one explicit bad configuration cannot prove `MUB(6)<7`.

The newest reserve report remains `proofnet24/C29-mub-six/runs/2026-09-16/2026-09-16_18-35-11__run-report.md`, status PARTIAL / source OPEN.

## 2. Frozen metric and protocol state

The frozen C29 fallback metric was fixed by `operations/claims/RS-2026-DC34.md` on the original four-point lifted irrational-parallelogram candidate: the largest integer `N` for which `N` pairwise distinct affine boundary patches of that same functional `D`-convex hull are rigorously certified.

The exact four-point theorem already established exactly two such affine patches. The five-point family below is route-finding auxiliary work and is not permitted to alter that frozen metric.

Therefore

\[
\boxed{2\longrightarrow 2}.
\]

This is the fifth consecutive unchanged frozen-metric run. Because C29 is CLOSABLE, one further unchanged run reaches the owner's six-run rotation threshold. Since the target is also still stuck in the metric sense, the next C29 run must be a Section-I thinking/handoff run; if the metric does not move there, it must rotate rather than produce a seventh auxiliary theorem.

## 3. Current source and literature refresh — 16 September 2026

The live Randomstrasse post, posted 23 February 2026 and updated 5 June 2026, still states Conjecture 34 and specifically predicts a non-semialgebraic example when `D` is three distinct planes in `R^3` meeting in a line.

Meroni--Raiţă, arXiv:2509.07541, is now v2, last revised 4 August 2026. Its abstract still proves semialgebraicity for finite triangular `2x2` rank-one convex hulls and explicitly says the general directional-convexity setting is expected to behave differently. The current author research page lists that paper as to appear in *Communications in Analysis and Geometry*. Franěk--Matoušek (2009) remains the polynomial-time planar finite-`D` hull reference; it does not solve the present three-dimensional alternating-direction problem.

Fresh bounded queries this run were:

1. `"Directional Convexity" Meroni Randomstrasse Conjecture 34 semialgebraic 2026`
2. `"Semialgebraic rank-one convex hulls" Meroni Raita directional convexity arXiv 2509.07541`
3. `"functional D-convex hull" non-semialgebraic 2026 directional convexity`
4. `"Computing D-convex hulls in the plane" Franek Matousek`

They recovered the live source, arXiv v2, the 2026 Meroni seminar/research pages, and the established planar algorithm, but no later source-exact resolution of Conjecture 34 and no matching centered two-defect theorem below. This is dated bounded-search evidence only, not a novelty certificate and not proof of worldwide openness.

## 4. The Section-B moves actually used

### B4 — prove something weaker, completely

The preceding stuck report isolated the simplest unresolved special case: the centered five-point spike with both mixed cells active. I attacked exactly that special case and computed the entire functional hull instead of adding another face lemma.

### B12 — find what is conserved

The centered configuration has the affine involution

\[
F(s,t,z)=(1-s,1-t,z+1-s-t),
\]

which exchanges the northwest and southeast defects. More importantly, after linewise chord replacement the relevant slope order is conserved across the center: the left replacement slope is always at least the middle derivative, and the middle derivative is always at least the right replacement slope. This is the invariant that prevents a long chord from spanning both defects.

### B27 — swap the quantifiers

Instead of asking globally whether one third-direction sweep preserves coordinate concavity, I first solved the least-concave-majorant problem on **every fixed third-direction line**, then proved the resulting global function is separately concave. This reverses the order of the hard quantifiers and turns the blocker into finite exact derivative-jump inequalities.

## 5. Recovered centered normal form

Keep the already-fixed planar direction set

\[
D_2=\mathbb R(1,0)\cup\mathbb R(0,1)\cup\mathbb R(1,-\alpha),
\qquad \alpha>1,
\]

and let `D` be the union of the corresponding vertical planes in `R^3`. The four-corner set is

\[
K_4=\{(0,0,0),(1,0,0),(0,1,0),(1,1,1)\},
\]

with exact lower boundary

\[
h(s,t)=\max\left\{0,\ st-\alpha^{-1}t(1-t),\ s+t-1\right\}.
\tag{5.1}
\]

Add the centered spike

\[
P_\delta=\left(\frac12,\frac12,\frac14+\delta\right),
\qquad \delta>\frac14,
\]

and put `K_5=K_4 union {P_delta}`. Define

\[
c:=4\delta>1,\qquad q:=c-1=4\delta-1>0.
\]

The least separately concave majorant of the five height data is

\[
U(s,t)=
\begin{cases}
(q+2)st,&s\le\frac12,\ t\le\frac12,\\
t(c-qs),&s\ge\frac12,\ t\le\frac12,\\
s(c-qt),&s\le\frac12,\ t\ge\frac12,\\
st+c(1-s)(1-t),&s\ge\frac12,\ t\ge\frac12.
\end{cases}
\tag{5.2}
\]

The southeast and northwest cells are exactly the two cells with positive third-direction curvature `2 alpha q`.

Write

\[
r=t+\alpha s,
\qquad
r_0=\frac{\alpha+1}{2}.
\tag{5.3}
\]

Since `alpha>1`,

\[
1<r_0<\alpha.
\tag{5.4}
\]

## 6. Exact two-defect third-direction sweep

Define `V=U` on the southwest and northeast cells. On the northwest cell set

\[
V_{NW}=
\begin{cases}
\left(1+\frac q2\right)s,&r\le1,\\
s(c-qt)+\frac q\alpha(1-t)\left(t-\frac12\right),&1\le r\le r_0,\\
s+\frac q2(1-t),&r\ge r_0.
\end{cases}
\tag{6.1}
\]

On the southeast cell set

\[
V_{SE}=
\begin{cases}
\left(1+\frac q2\right)t,&r\le r_0,\\
t(c-qs)+\frac q\alpha t\left(\frac12-t\right),&r_0\le r\le\alpha,\\
t+\frac q2(1-s),&r\ge\alpha.
\end{cases}
\tag{6.2}
\]

All formulas agree on their common boundaries.

### Lemma 6.1 — these are the exact endpoint chords

On a fixed line `t=r-alpha s`, the northwest convex segment has endpoints

\[
(s_0,s_1)=
\begin{cases}
\left(0,\frac{r-1/2}{\alpha}\right),&r\le1,\\
\left(\frac{r-1}{\alpha},\frac{r-1/2}{\alpha}\right),&1\le r\le r_0,\\
\left(\frac{r-1}{\alpha},\frac12\right),&r\ge r_0,
\end{cases}
\tag{6.3}
\]

while the southeast convex segment has endpoints

\[
(s_0,s_1)=
\begin{cases}
\left(\frac12,\frac r\alpha\right),&r\le r_0,\\
\left(\frac{r-1/2}{\alpha},\frac r\alpha\right),&r_0\le r\le\alpha,\\
\left(\frac{r-1/2}{\alpha},1\right),&r\ge\alpha.
\end{cases}
\tag{6.4}
\]

On either defective segment, the restriction of `U` is a convex quadratic with quadratic coefficient `alpha q`. Hence its endpoint chord differs from `U` by exactly

\[
\boxed{\alpha q(s-s_0)(s_1-s)}.
\tag{6.5}
\]

Substituting (6.3) and (6.4) gives exactly the six formulas (6.1)--(6.2).

### Lemma 6.2 — the two local chords already form the global linewise least concave majorant

For `r<r_0`, the line meets the concave southwest piece between the northwest and southeast defects. At the northwest/southwest interface, if `r<=1` the chord-slope gap is

\[
(q+2)\left(r-\frac12\right)\ge0.
\tag{6.6}
\]

For `r>=1`, that gap is an increasing affine function of `r` with derivative `2(q+1)>0` and value `(q+2)/2` at `r=1`; hence it is positive. At the southwest/southeast interface the derivative gap is

\[
(q+2)\left(r-\frac\alpha2\right)\ge0,
\tag{6.7}
\]

because the southeast cell is present only for `r>=alpha/2`.

For `r>r_0`, the concave middle piece is northeast. The northwest-chord slope exceeds the northeast derivative at their interface by

\[
\frac{q+2}{2}(\alpha+2-2r)\ge0,
\tag{6.8}
\]

because the northwest cell is present only through `r<=alpha/2+1`. At the northeast/southeast interface the remaining gap is

\[
2(q+1)(\alpha-r)+\frac{q+2}{2}>0
\tag{6.9}
\]

for `r<=alpha`, and

\[
(q+2)\left(\alpha+\frac12-r\right)\ge0
\tag{6.10}
\]

for `r>=alpha`, since the southeast cell exists only through `r<=alpha+1/2`.

At the central line `r=r_0` the two defective cells meet at the spike. The northwest replacement slope is `1+alpha q/2`, while the southeast replacement slope is `-alpha(1+q/2)`, so the jump is strictly downward. Therefore the feared long chord spanning both defects never becomes necessary.

The piecewise line restriction of `V` is thus concave on every third-direction line and majorizes `U`. Conversely, any concave majorant of `U` on such a line must dominate each endpoint chord, and equals or exceeds `U` on the middle concave piece. Hence `V` is exactly the linewise least concave majorant `C_d U`.

## 7. Coordinate concavity survives the two-defect sweep

Inside every formula region,

\[
\partial_{ss}V=0,
\]

and the only nonzero pure second derivative is

\[
\partial_{tt}V=-\frac{2q}{\alpha}<0
\]

on the two middle chord regimes. Thus only interface jumps need checking.

Across the four slanted regime boundaries, the new-piece minus old-piece factorizations are

\[
V_{NW,2}-V_{NW,1}
=-\frac{q(2t-1)(r-1)}{2\alpha},
\tag{7.1}
\]

\[
V_{NW,3}-V_{NW,2}
=\frac{q(t-1)(r-r_0)}{\alpha},
\tag{7.2}
\]

\[
V_{SE,2}-V_{SE,1}
=-\frac{qt(r-r_0)}{\alpha},
\tag{7.3}
\]

\[
V_{SE,3}-V_{SE,2}
=\frac{q(2t-1)(r-\alpha)}{2\alpha}.
\tag{7.4}
\]

Since increasing either coordinate increases `r`, the corresponding derivative jumps are downward on their cells: `t>=1/2` in northwest, `t<=1`, `t>=0`, and `t<=1/2` in southeast.

Across the coordinate cell boundaries, the nontrivial derivative jumps are also downward. At `s=1/2`, for `t<1/2`,

\[
\partial_sV_{SE}-\partial_sU_{SW}=-(q+2)t\le0,
\tag{7.5}
\]

while for `t>1/2`,

\[
\partial_sU_{NE}-\partial_sV_{NW}=(q+2)(t-1)\le0.
\tag{7.6}
\]

At `t=1/2`, for `s<1/2`, the two northwest regimes give

\[
-(q+2)s\le0,
\tag{7.7}
\]

or

\[
\frac{q}{2\alpha}-2(q+1)s\le-\frac{q+2}{2\alpha}<0,
\tag{7.8}
\]

where the latter regime itself implies `s>=1/(2alpha)`. For `s>1/2`, the two southeast regimes give

\[
2(q+1)(s-1)+\frac{q}{2\alpha}
\le-\frac{q+2}{2\alpha}<0,
\tag{7.9}
\]

when `s<=1-1/(2alpha)`, and

\[
(q+2)(s-1)\le0
\tag{7.10}
\]

in the terminal regime.

Therefore `V` is globally concave in each coordinate direction as well as the third direction. It is `D_2`-concave.

## 8. Main theorem

### `C29-DC34-CENTERED-TWO-DEFECT-SEMIALGEBRAIC-09 = PROVED (PARTIAL)`

For every `alpha>1` and every centered spike height `delta>1/4`, with `K_5` defined above,

\[
\boxed{
\operatorname{conv}_{D}(K_5)
=
\{(s,t,z):0\le s,t\le1,\ h(s,t)\le z\le V(s,t)\},
}
\tag{8.1}
\]

where `h` is (5.1) and `V` is the finite piecewise-polynomial function (6.1)--(6.2) together with `V=U` on southwest/northeast.

In particular this entire centered two-defect family is **semialgebraic** and is contained in a finite lamination construction. It therefore cannot realize Randomstrasse Conjecture 34.

### Proof of minimality of the upper boundary

Any `D_2`-concave majorant `W` of the five height data is in particular separately concave. Since `U` is the least separately concave majorant,

\[
W\ge U.
\]

Restricting to a line `t+alpha s=r`, `W` is concave and majorizes `U`; by Lemma 6.2 it therefore majorizes the exact linewise least concave majorant `V`. Since Section 7 proves `V` itself is `D_2`-concave, `V` is the least `D_2`-concave majorant.

### Lower boundary and reverse hull inclusion

The old lower boundary `h` remains admissible at the upward spike, so adding `P_delta` does not raise the lower functional boundary. Conversely any five-point lower minorant is in particular a four-corner minorant, so it cannot lie below the old exact lower envelope.

For the constructive reverse inclusion, the nine grid nodes in

\[
\{0,1/2,1\}\times\{0,1/2,1\}
\]

on graph `U` are generated from `K_5` by horizontal/vertical laminations: the four corners and spike are inputs and the four edge-midpoint nodes come from boundary edge laminations. On each of the four grid rectangles `U` is bilinear, so two more coordinate-direction laminations generate every graph-`U` point. Every graph-`V` point in a defective cell is then one allowed third-direction chord of two graph-`U` points by (6.5). The already-generated lower graph `h` is inherited from `K_4 subset K_5`, and the vertical direction fills each interval from `h` to `V`.

Thus the reverse inclusion in (8.1) is finite and constructive, not merely a dual-separation argument.

## 9. Exact symbolic checker

Only after the formulas above were derived did I write a checker. The executed exact symbolic checker verifies:

- all six chord identities (6.5) against the closed forms (6.1)--(6.2);
- all pure coordinate second derivatives;
- the four slanted regime-change factorizations (7.1)--(7.4);
- every third-direction slope-gap identity used in Lemma 6.2;
- every coordinate-boundary derivative-jump identity (7.5)--(7.10).

Artifacts:

`proofnet24/C29-closure-brownian-shapes/artifacts/2026-09-16T22-35-54Z__centered_two_defect_symbolic.py`

corrected checker commit `b7b03d69a4989faeae50fea7e66f096c1febcf03`, and

`proofnet24/C29-closure-brownian-shapes/artifacts/2026-09-16T22-35-54Z__centered_two_defect_symbolic.out`

bound to the corrected code at commit `39b072e5aea95b0ddf637fe18e7aa14dcef545c1`.

The corrected script was executed before archival of the bound output; it ends

`ALL_EXACT_SYMBOLIC_CHECKS_PASS`.

The checker is a self-check of the finite algebraic core and does not replace the proof above.

## 10. What this rules out, and what remains

The previous run's central uncertainty is now resolved in the finite-closure direction: two simultaneously active mirror defects in the centered five-point spike still close after **one** exact third-direction sweep. No coordinate-direction return defect is created. Hence neither the one-defect band nor the centered two-defect family can generate the desired infinite alternation.

The first unresolved local mechanism is now an **asymmetric two-defect** spike above the larger activation threshold, where the two linewise chord corrections are no longer mirror paired. That is the natural place to look for a genuine cross-direction return map. However, because the frozen four-point metric has now remained unchanged for five runs and is in fact saturated at two by its exact theorem, C29 must not simply accumulate another auxiliary theorem indefinitely. The next run is a protocol thinking/handoff run, and an unchanged sixth run forces rotation.

## 11. C30 second-audit duty

C30's actual newest report is

`proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T21-50-52Z__stuck-recovery-2.md`.

It explicitly states **THINKING-ONLY / no new C30 theorem claim**. Therefore I did not manufacture a receipt-only re-audit. The latest legitimate C29-to-C30 audit remains

`C29-AUDIT-C30-N11-M27-STRUCTURAL-03 = PASS (claim-scoped)`

from the preceding C29 report. It covers only C30's `n=11,m=27` structural theorem, not complete order-eleven coverage or later scratch support-profile arithmetic.

## 12. Ledger delta for P26

```yaml
ledger_delta:
  track: C29
  allocation: CLOSABLE OUTSIDE
  proposed_source: I0077 / Burdzy-Scheutzow Problem 7.8
  proposed_source_disposition: EXCLUDED_FROM_C29_BY_EXCLUSIVE_R07_OWNERSHIP
  active_fallback: RS-2026-DC34
  active_status: PARTIAL / CLAIMED / PENDING_ADMISSION / NOT_READY
  frozen_metric: fixed four-point affine-boundary-patch count
  before: 2
  after: 2
  movement: none
  unchanged_run_count: 5
  new_claim: C29-DC34-CENTERED-TWO-DEFECT-SEMIALGEBRAIC-09 = PROVED (PARTIAL)
  theorem_scope: centered five-point spike a=b=1/2, delta>1/4, alpha>1; exact semialgebraic finite-lamination functional D-hull
  source_conjecture_closed: false
  audit_duty: no new C30 theorem to audit; preserve C29-AUDIT-C30-N11-M27-STRUCTURAL-03 PASS
  next_protocol: Section-I thinking/handoff; if metric remains 2 on next run, six-run CLOSABLE rotation is mandatory
  reserve: MUB(6)<7 remains HARD RESERVE; global residual lower bound 0; 11/756 upper benchmark only
```

P26 is the shared-ledger writer. This run did not edit `RESULTS.md`, `QUEUE.md`, `POSTED.md`, any peer track, or any claim file.

## 13. Model / reasoning control status

The actual runtime identifies as GPT-5.6 Sol; reasoning level is not exposed as authenticated telemetry, so I record **UNVERIFIED**. The exposed task-control schema still provides prompt/title, schedule/timing, enabled state, and notification controls, but no model-family selector and no reasoning-effort selector. GPT-6 / maximum therefore remains prompt-only in this interface.

Making the owner's requirement enforceable would require the scheduler/backend or an authorized enclosing runtime to expose, persist, and bind explicit model-family and reasoning-effort fields and to report the applied runtime values. The historical P26 `"You cannot modify this task"` event is a permission-context boundary, not a mathematical or scheduler-model setting; later P26 edits succeeded from an authorized context. The supported workaround is owner/admin/coordinator action in the owning authorized workspace, or platform support if that authorization is defective, never a permission bypass or duplicate task.
