Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6/maximum was requested, but this runtime and the exposed scheduler/task interface provide no model-family selector or reasoning-effort selector, so I do not claim otherwise. **no movement — frozen C29 fallback metric 2 -> 2; unchanged-run count 3; Section-B moves tried: 15 (break symmetry), 30 (one direction / one defect cell at a time), 3 (prove something stronger: compute the whole one-defect hull, not another face lemma). The three-unchanged-run threshold is now reached, so the next C29 run on this target must be a Section-I thinking/stuck run.**
Problem/source: Chiara Meroni, Randomstrasse 101 (2026), Conjecture 34 on non-semialgebraic functional directional-convex hulls; fallback claim `RS-2026-DC34`. The owner's proposed Burdzy--Scheutzow Problem 7.8 / intake I0077 remains excluded from C29 because R07 owns the canonical reservation and its newest report has moved its own source-family metric to 3. C29 remains **CLAIMED / PENDING_ADMISSION / NOT READY** on the fallback target.

# C29 — exact semialgebraic hull in the asymmetric one-defect supercritical band

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C29-closure-brownian-shapes`.
Run date: 2026-09-16.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, paid compute, access change, shared-ledger edit, peer-file edit, or new schedule.

## 1. Continuity, ownership, and frozen metric

I continued from the newest durable C29 report

`proofnet24/C29-closure-brownian-shapes/runs/2026-09-16/2026-09-16T19-36-06Z__dc34-supercritical-exposed-faces.md`

rather than restarting the proposed Brownian target or the retired MUB attack. Before mathematics I reread/queried `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, canonical claims `operations/claims/I0077.md` and `operations/claims/RS-2026-DC34.md`, the full current C29 report chain, newest R07 Problem-7.8 report, newest C30 report, and the newest visible legacy `proofnet24/C29-mub-six` report. Large intake/attempt JSONL surfaces were queried by exact IDs/source phrases rather than falsely described as manually rendered byte-for-byte.

### I0077 remains excluded

`operations/claims/I0077.md` still reserves Burdzy--Scheutzow Problem 7.8 to R07, status `PENDING_ADMISSION, not READY`. R07's newest report `runs/R07/20260916T1925Z_i0077_pure_power_phase_03.md` records genuine source-family movement `2 -> 3`. C29 therefore does not duplicate I0077 and does not reopen already-answered Problem 7.5.

### Frozen fallback metric remains exactly 2

The create-only C29 claim `RS-2026-DC34` freezes the metric to the number of pairwise distinct maximal affine boundary patches rigorously certified for **one fixed four-point lifted irrational-parallelogram candidate**. The complete four-point theorem already proved that its exact functional hull has exactly two such affine patches. The five-point experiments below are route-finding auxiliary work and cannot be counted into that frozen four-point metric.

Therefore

\[
\boxed{2\longrightarrow2}.
\]

This is the third consecutive unchanged frozen-metric run. Under the owner's Section-I rule, the *next* C29 run on this target is a mandatory thinking/stuck run even though the auxiliary mathematical obstruction moved substantially this run.

## 2. MUB HARD RESERVE remains unchanged

The old six-dimensional MUB existence attack remains in **HARD RESERVE**. Preserve without reinterpretation:

- unrestricted/full-domain normalized residual lower bound: `0`;
- `11/756`: an **upper** benchmark from an explicit configuration, not a positive lower bound and not a nonexistence proof;
- all exact phase examples, restricted auxiliary bounds, atlas/gauge reductions, and failed proof routes.

The newest visible reserve report is `proofnet24/C29-mub-six/runs/2026-09-16/2026-09-16_18-35-11__run-report.md`; it still has global metric `0 -> 0`. Its exact-zero atlas normal form remains reserve-only history. I did not restart that target.

## 3. Current source and literature check — 16 September 2026

The live Randomstrasse source, posted 23 February 2026 and updated 5 June 2026, defines the functional `D`-convex hull by testing against every `D`-convex function and states Conjecture 34: the functional `D`-convex hull of a finite point set need not be semialgebraic. It specifically predicts a counterexample for a cone made of three distinct planes in `R^3` meeting in a line.

Meroni--Raiţă, arXiv:2509.07541v2 (last revised 4 August 2026), Section 5, gives the source-neighboring mechanism. Example 5.3 has an infinite compatible planar grid, and Question 2 asks whether small vertical perturbations can force a non-semialgebraic three-direction hull. Their text identifies the unresolved issue as proving that the infinitely many candidate boundary planes do not collapse into only finitely many coincidences.

Fresh bounded searches this run used:

1. `"Directional Convexity" Meroni Randomstrasse Conjecture 34 2026`;
2. `"Semialgebraic rank-one convex hulls" Meroni Raita directional convexity five points`;
3. `"functional D-convex hull" non-semialgebraic directional convexity`;
4. `"Computing D-convex hulls in the plane" Franek Matousek`.

They recovered the live Randomstrasse post, arXiv:2509.07541v2, Franěk--Matoušek's planar algorithm, and older directional-convexity literature. I found no later theorem matching the exact asymmetric five-point calculation below. This is a bounded dated search, **not** a novelty certificate or proof of worldwide openness.

## 4. Recovered exact five-point normal form

Use the already-fixed affine normalization

\[
D_2=\mathbb R(1,0)\cup\mathbb R(0,1)\cup\mathbb R(1,-\alpha),
\qquad \alpha>1,
\]

and let `D` be the union of the three corresponding vertical planes in `R^3`. Put

\[
K_4=\{(0,0,0),(1,0,0),(0,1,0),(1,1,1)\}.
\]

The exact old hull is

\[
\operatorname{conv}_D(K_4)
=\{(s,t,z):0\le s,t\le1,\ h(s,t)\le z\le st\},
\tag{4.1}
\]

where

\[
h(s,t)=\max\{0,\ st-\alpha^{-1}t(1-t),\ s+t-1\}.
\tag{4.2}
\]

Add one spike

\[
P_{a,b,\delta}=(a,b,ab+\delta),
\qquad0<a,b<1,\quad\delta>0,
\tag{4.3}
\]

and write `K_5=K_4 union {P_{a,b,delta}}`. Define tents

\[
T_a(s)=\begin{cases}s/a,&s\le a,\\(1-s)/(1-a),&s\ge a,\end{cases}
\quad
T_b(t)=\begin{cases}t/b,&t\le b,\\(1-t)/(1-b),&t\ge b,\end{cases}
\tag{4.4}
\]

and the least separately concave majorant of the five height data

\[
U_\delta(s,t)=st+\delta T_a(s)T_b(t).
\tag{4.5}
\]

The preceding exact theorem established the two third-direction thresholds

\[
\tau_{SE}:=(1-a)b,
\qquad
\tau_{NW}:=a(1-b),
\tag{4.6}
\]

and

\[
U_\delta\text{ is }D_2\text{-concave}
\iff
\delta\le\min\{\tau_{SE},\tau_{NW}\}.
\tag{4.7}
\]

On the southeast cell `s>a,t<b`, third-direction curvature changes sign at `tau_SE`; on the northwest cell `s<a,t>b`, it changes sign at `tau_NW`.

The centered experiment `a=b=1/2` makes these two thresholds coincide. That symmetry is exactly what the present run breaks.

## 5. Move 15 — break symmetry: create a one-defect band

Assume

\[
\boxed{a>b.}
\tag{5.1}
\]

Then

\[
\tau_{SE}=(1-a)b<a(1-b)=\tau_{NW}.
\tag{5.2}
\]

Choose the genuinely supercritical but asymmetric interval

\[
\boxed{	au_{SE}<\delta<\tau_{NW}.}
\tag{5.3}
\]

In this band the coordinate envelope `U_delta` fails third-direction concavity on **exactly one** of its four bilinear cells, namely

\[
R_{SE}=[a,1]\times[0,b].
\tag{5.4}
\]

The other three cells remain third-direction concave. Thus the centered two-defect problem has a nontrivial solvable deformation: separate the two activation thresholds and cross only the first.

Set

\[
c:=\frac{\delta}{(1-a)b}>1,
\qquad q:=c-1>0.
\tag{5.5}
\]

On `R_SE`, (4.5) simplifies to

\[
U_\delta(s,t)=t(c-qs).
\tag{5.6}
\]

Along a third-direction line

\[
r=t+\alpha s=\text{constant},
\tag{5.7}
\]

this is a convex quadratic in `s`, with second derivative `2 alpha q>0`. Since `R_SE` is southeast, every such line meets it, if at all, in a **terminal interval** as `s` increases and `t` decreases. That one-sided geometry is the key simplification.

## 6. Move 30 — one direction / one defect cell at a time

Put

\[
\eta:=\alpha a+b.
\tag{6.1}
\]

Define `V=U_delta` off `R_SE`. On `R_SE`, define `V` by the following four compatible formulas, according to which side of `R_SE` the line (5.7) enters and which side of the unit square it exits:

\[
V_A=t(c-qa),
\qquad r\le\eta,\ r\le\alpha,
\tag{6.2}
\]

\[
V_B=t(c-qs)+\alpha q(s-a)(1-s),
\qquad r\le\eta,\ r\ge\alpha,
\tag{6.3}
\]

\[
V_C=t(c-qs)+\frac q\alpha t(b-t),
\qquad r\ge\eta,\ r\le\alpha,
\tag{6.4}
\]

\[
V_D=t+qb(1-s),
\qquad r\ge\eta,\ r\ge\alpha.
\tag{6.5}
\]

Depending on whether `eta<alpha` or `eta>alpha`, one of the middle regions `B,C` is empty. On all common boundaries the displayed formulas agree.

### Where these formulas come from

For fixed `r`, the intersection with `R_SE` is

\[
[s_0,s_1]
=\left[
\max\left\{a,\frac{r-b}{\alpha}\right\},
\min\left\{1,\frac r\alpha\right\}
\right].
\tag{6.6}
\]

The restriction of `U_delta` to this interval is a convex quadratic with quadratic coefficient `alpha q`. Therefore its least concave majorant on that interval is its endpoint chord, and

\[
V-U_\delta
=\alpha q(s-s_0)(s_1-s).
\tag{6.7}
\]

Substituting the four possible choices of `s_0,s_1` in (6.6) gives exactly (6.2)--(6.5). In particular `V>=U_delta`, with equality on the boundary through which the chord is attached.

## 7. Move 3 — stronger theorem: exact hull for the whole one-defect band

### Theorem `C29-DC34-ONE-DEFECT-SEMIALGEBRAIC-08 = PROVED (PARTIAL)`

Assume `alpha>1`, `0<b<a<1`, and

\[
(1-a)b<\delta<a(1-b).
\tag{7.1}
\]

Let `V` be given by (6.2)--(6.5) and `U_delta` elsewhere. Then `V` is the **least `D_2`-concave majorant** of the five lifted height data, and

\[
\boxed{
\operatorname{conv}_D(K_5)
=\{(s,t,z):0\le s,t\le1,\ h(s,t)\le z\le V(s,t)\}.
}
\tag{7.2}
\]

Consequently this entire asymmetric one-defect supercritical family has a **semialgebraic** functional `D`-convex hull and is obtained by a finite lamination construction.

The mirror case `b>a` with

\[
a(1-b)<\delta<(1-a)b
\]

follows by exchanging the coordinate axes (which sends the third direction line to the equivalent parameter `alpha^{-1}`). Thus every supercritical spike for which exactly one of the two mixed-cell thresholds has been crossed is still semialgebraic.

This is an auxiliary **PARTIAL** theorem. It neither proves nor refutes Randomstrasse Conjecture 34.

### Proof, Step 1: `V` is concave in the third direction

Outside `R_SE`, the hypothesis `delta<tau_NW` and the previous curvature calculation show that `U_delta` is already concave along every `(1,-alpha)` line. Inside `R_SE`, (6.7) replaces the terminal convex portion by its endpoint chord, hence makes it affine there.

It remains only to check that the chord does not create an upward derivative jump at the entry point.

If a line enters through `s=a` and exits through the bottom (`A`), the left directional derivative of `U_delta` minus the chord slope equals

\[
\frac{t\,[1+q(1-a)]}{a}>0.
\tag{7.3}
\]

If it enters through `s=a` and exits through `s=1` (`B`), the same difference is

\[
\frac{ct-a\alpha q(1-a)}a.
\tag{7.4}
\]

Region `B` implies `t\ge\alpha(1-a)`, and `c=q+1>aq`, so (7.4) is positive.

If the line enters through `t=b` and exits through the bottom (`C`), write `rho=1-s` at entry. Region `C` implies `rho\ge b/alpha`, and the derivative difference is

\[
\frac{\alpha c\rho-bq(1-b)}{1-b}
\ge
\frac{b[c-q(1-b)]}{1-b}
=
\frac{b(1+qb)}{1-b}>0.
\tag{7.5}
\]

If it enters through `t=b` and exits through `s=1` (`D`), the derivative difference is

\[
\frac{\alpha(1-s)(1+bq)}{1-b}>0.
\tag{7.6}
\]

Thus the restriction of `V` to every third-direction line is concave.

### Proof, Step 2: each piece is separately concave

Pieces `A` and `D` are affine. Piece `B` is affine in `t` and has

\[
\partial_s^2V_B=-2\alpha q<0.
\tag{7.7}
\]

Piece `C` is affine in `s` and has

\[
\partial_t^2V_C=-\frac{2q}{\alpha}<0.
\tag{7.8}
\]

So only derivative jumps across piece interfaces need checking.

### Proof, Step 3: coordinate derivative jumps across the internal slanted interfaces are downward

At `r=eta` in the `A -> C` geometry, the horizontal derivative jump and the vertical derivative jump are respectively

\[
q[\alpha(s-a)-b],
\qquad
\frac q\alpha[\alpha(s-a)-b].
\tag{7.9}
\]

On that interface inside `R_SE`, `alpha(s-a)<=b`, so both are nonpositive.

At `r=alpha` in the `C -> D` geometry the two jumps are

\[
-q[b-\alpha(1-s)],
\qquad
-\frac q\alpha[b-\alpha(1-s)],
\tag{7.10}
\]

again nonpositive because the interface lies in `t=alpha(1-s)<=b`.

If `eta>alpha`, the middle piece is `B` instead. At `r=alpha`, the `A -> B` derivative jumps are

\[
-\alpha q(s-a),\qquad -q(s-a),
\tag{7.11}
\]

and at `r=eta`, the `B -> D` jumps are

\[
\alpha q(s-1),\qquad q(s-1),
\tag{7.12}
\]

all nonpositive.

Hence the coordinate restrictions remain concave across all internal interfaces.

### Proof, Step 4: coordinate derivative jumps across the old tent kinks are also downward

Across `s=a` from the southwest cell into `R_SE`, the horizontal derivative jump is

\[
\frac{t[q(a-1)-1]}a<0
\tag{7.13}
\]

in region `A`. In region `B` it is

\[
\frac{a\alpha q(1-a)-ct}{a}\le0,
\tag{7.14}
\]

because `B` implies `t>=alpha(1-a)` and `c>aq`.

Across `t=b`, from `R_SE` into the northeast cell as `t` increases, the jump in region `D` is

\[
-\frac{(1-s)(1+bq)}{1-b}<0.
\tag{7.15}
\]

In region `C`, with `rho=1-s>=b/alpha`, it is

\[
-\frac{\alpha c\rho-bq(1-b)}{\alpha(1-b)}\le0.
\tag{7.16}
\]

Therefore `V` is concave in both coordinate directions as well. Combined with Step 1, `V` is globally `D_2`-concave.

### Proof, Step 5: minimality of `V`

Let `W` be any `D_2`-concave majorant of the five height data. Since coordinate directions belong to `D_2`, `W` is separately concave. The preceding C29 argument proving minimality of (4.5) therefore gives

\[
W\ge U_\delta
\quad\text{on }[0,1]^2.
\tag{7.17}
\]

Restrict to a third-direction line. `W` is concave there and majorizes `U_delta`; hence it majorizes the least concave majorant of that restriction. By construction that least concave majorant is exactly `V`. Therefore

\[
W\ge V.
\tag{7.18}
\]

Since `V` itself is `D_2`-concave and interpolates/majorizes the five data, it is the least `D_2`-concave majorant.

### Proof, Step 6: lower boundary and functional-hull outer inclusion

The old lower boundary `h` remains exact after adding an upward spike. Indeed `h<=st`, so

\[
h(a,b)\le ab<ab+\delta,
\]

and `h-z` remains a valid `D`-convex separator. Conversely every lower minorant admissible for all five points is admissible for the original four corners, whose exact lower envelope is `h`.

Since `V` is `D_2`-concave, `z-V(s,t)` is `D`-convex. Together with `h-z` and the coordinate-box separators this yields

\[
\operatorname{conv}_D(K_5)
\subseteq
\{0\le s,t\le1,\ h\le z\le V\}.
\tag{7.19}
\]

### Proof, Step 7: finite lamination gives the reverse inclusion

All nine lifted grid nodes over

\[
\{0,a,1\}\times\{0,b,1\}
\]

on the graph of `U_delta` are obtained from `K_5` by horizontal/vertical laminations: the four corners and spike are input points, while `(a,0)`, `(a,1)`, `(0,b)`, `(1,b)` come from the four boundary edges. On each of the four grid rectangles, `U_delta` is bilinear, so every point of its graph follows from two further coordinate-direction laminations of its four lifted corner nodes. Thus the whole graph of `U_delta` is contained in the finite lamination hull.

For a point in `R_SE`, the value `V(s,t)` is, by (6.7), the value of the chord joining two graph-`U_delta` points on the same planar `(1,-alpha)` line. Their three-dimensional difference lies in the corresponding vertical direction plane, so one additional permitted lamination produces the graph of `V`.

The old graph of `h` is already in the finite lamination hull of `K_4`. The vertical direction belongs to every source plane, so vertical lamination between `(s,t,h(s,t))` and `(s,t,V(s,t))` fills the entire interval between them. Hence

\[
\{0\le s,t\le1,\ h\le z\le V\}
\subseteq K_5^{(\infty,D)}
\subseteq\operatorname{conv}_D(K_5).
\tag{7.20}
\]

Together with (7.19), this proves (7.2). Because `h` is a maximum of finitely many quadratic/affine polynomials and `V` is given by finitely many polynomial formulas on finitely many linear cells, the hull is semialgebraic. `square`

## 8. What this changes — and what it does not

The previous centered supercritical calculation showed where new affine supports appear. The present theorem gives a sharper structural diagnosis:

- if the two mixed-cell thresholds are separated and only the first has been crossed, **one exact third-direction chord sweep closes the hull**;
- no infinite alternating cascade is possible in that one-defect band;
- therefore the centered choice `a=b` is not merely convenient symmetry: it removes the entire solvable one-defect regime by forcing the two defects to activate simultaneously;
- the simplest remaining five-point route to possible wildness is now a **two-defect regime**, preferably just above the second threshold with `a!=b`, where the defects activate at distinct parameter values but are both present.

This is useful negative information for Conjecture 34, but it does not settle the source. In particular, the source permits arbitrary finite point sets, while this theorem treats one five-point family. It is **PARTIAL**.

The theorem also does not move C29's frozen metric: the metric is tied to the already-fixed four-point candidate, whose exact affine-patch count remains 2. Counting the new five-point pieces would compare different objects and is prohibited.

## 9. Stuck threshold and next-run obligation

The frozen metric has now remained `2` for three consecutive runs after its initial `UNMEASURED -> 2` movement. Therefore the next C29 run on `RS-2026-DC34` must be a Section-I **thinking/stuck report with no new claims**.

The precise blocker after this run is no longer “what happens immediately above the first five-point threshold.” That band is solved by Theorem 08. The next blocker is:

\[
\boxed{
\text{Does the exact alternating concavification stabilize finitely once both mixed cells are active?}
}
\tag{9.1}
\]

The simplest remaining special case is an asymmetric spike with

\[
a>b,
\qquad
\delta>a(1-b)
\]

but `delta-a(1-b)` arbitrarily small. This keeps the two activation thresholds separated and should reveal whether the second defect creates a genuine return map or merely another finite chord correction.

No next-run action is chosen here because this is not yet the mandatory thinking run; the next invocation must perform the full Section-I inventory and choose exactly one allowed recovery action.

## 10. Directed C30 audit duty

The newest C30 report is

`proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T19-51-58Z__stuck-recovery-1.md`.

It explicitly states **“No new C30 theorem claim is made in this report.”** Its `m=27` split and binary-window inequalities are route-selection evidence for the next ordinary C30 run, not promoted claims. Therefore there is no honest new C30 theorem for C29 to second-audit this run, and I do **not** manufacture a receipt-only PASS.

Preserve the previous directed audit

`C29-AUDIT-C30-CUBIC-TENSOR-ZERO-02 = PASS (claim-scoped)`

from the preceding C29 report. It covers only C30's finite-rank zero-cubic-tensor theorem, not C30's current `m=27` proof skeleton, not order-eleven completion, and not universal Sidorenko closure.

For sanity only, I independently rechecked the arithmetic threshold appearing in C30's stuck report:

\[
\left\lceil\frac{54^{15}}{11^{20}}\right\rceil=143898.
\]

This is not recorded as a new audit because C30 did not make a new theorem claim.

## 11. Ledger delta for P26 / shared-ledger writer

Do not edit peer/shared files from C29. Requested reconciliation:

- C29 active fallback remains `RS-2026-DC34`, owner C29, **CLAIMED / PENDING_ADMISSION / NOT READY**;
- proposed I0077 remains excluded from C29 because canonical owner R07 now has source-family metric `3`;
- frozen C29 metric remains `2 -> 2` on the fixed four-point candidate;
- unchanged-run count becomes `3`, so the next C29 run on this target is mandatory Section-I thinking/stuck recovery;
- new auxiliary theorem: `C29-DC34-ONE-DEFECT-SEMIALGEBRAIC-08 = PROVED (PARTIAL)`, exact semialgebraic functional hull for every asymmetric five-point spike with exactly one mixed-cell threshold crossed;
- do **not** count this five-point theorem toward the frozen four-point metric;
- source Conjecture 34 remains OPEN on this record; no READY certification and no novelty certificate;
- MUB remains HARD RESERVE, unrestricted residual lower bound `0`, `11/756` upper benchmark only;
- C30 directed duty: no fresh theorem claim in C30 STUCK RECOVERY 1, so no new audit; preserve `C29-AUDIT-C30-CUBIC-TENSOR-ZERO-02 = PASS (claim-scoped)`.

## 12. Model / scheduler control

The runtime still identifies the model as GPT-5.6 Sol; no separate reasoning-level telemetry is exposed, so reasoning is `UNVERIFIED`. The automation/task interface available to this worker exposes prompt/title/schedule/timing/enabled/notification controls but no model-family selector and no reasoning-effort selector. Thus GPT-6/maximum remains prompt-only.

Changing that requires scheduler/backend support or an authorized enclosing runtime/UI that exposes and persists model/reasoning fields. A `You cannot modify this task` response remains an ownership/permission-context boundary; the legitimate workaround is owner/admin/coordinator action from the owning authorized workspace (or platform support), not a permission bypass or duplicate schedule.
