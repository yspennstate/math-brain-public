Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but this runtime and the exposed scheduler provide no model-family selector or reasoning-effort selector, so I do not claim otherwise. **no movement — frozen C29 fallback metric 2 -> 2; unchanged-run count 1; Section-B moves tried: 1, 5, 24.**
Problem/source: Chiara Meroni, Randomstrasse 101 (2026), Conjecture 34 on non-semialgebraic functional directional-convex hulls; fallback claim `RS-2026-DC34`. The owner's proposed Burdzy--Scheutzow Problem 7.8 / intake I0077 remains excluded from C29 because R07 owns the canonical reservation and now has an admitted source-matching partial theorem. C29 remains **CLAIMED / PENDING_ADMISSION / NOT READY** on the fallback target.

# C29 — exact five-point spike threshold above the canonical irrational parallelogram

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C29-closure-brownian-shapes`.
Run date: 2026-09-16.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, paid compute, permission change, shared-ledger edit, peer-file edit, or new schedule.

## 1. Required continuity and ownership read

I continued from

`proofnet24/C29-closure-brownian-shapes/runs/2026-09-16/2026-09-16T17-36-30Z__dc34-canonical-hull.md`

rather than restarting the geometry. Before the new attack I reread/queried:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, root `RESULTS.md`, and `QUEUE.md`;
- canonical claims `operations/claims/I0077.md` and `operations/claims/RS-2026-DC34.md`;
- the newest own C29 fallback report above;
- newest R07 Problem-7.8 report `runs/R07/20260916T1724Z_i0077_cusp_power_shape_01.md`;
- newest neighboring Burdzy--Scheutzow R15 report on the distinct Problem 7.2;
- newest C30 Sidorenko report for C29's directed audit duty;
- the newest legacy `proofnet24/C29-mub-six` report, for reserve continuity only;
- targeted exact-ID/source searches over the intake/attempt material.

The very large JSONL intake surfaces are connector-truncated, so I do not pretend to have manually rendered every row. Exact ownership and the relevant intake/source records were recovered directly.

### I0077 exclusion remains binding

`operations/claims/I0077.md` still reserves Burdzy--Scheutzow Problem 7.8 to R07. The newest R07 report has now moved its own Problem-7.8 metric from UNMEASURED to one genuinely nonparabolic two-power cusp family by an explicit decomposable-FBM construction. Therefore C29 must not duplicate I0077. Problem 7.5 remains separately settled/excluded and was not reopened.

### C29 fallback ownership

`operations/claims/RS-2026-DC34.md` remains the create-only C29 reservation. Its frozen metric is the number of distinct affine boundary patches certified for the already-fixed lifted irrational-parallelogram candidate. The preceding run established the value `2`. This run studies a **new five-point extension** of that geometry but does not alter the frozen four-point candidate; consequently the metric remains `2`.

## 2. MUB HARD RESERVE and an operational inconsistency discovered this run

The owner's current instruction places the old dimension-six MUB existence attack in **HARD RESERVE**. Preserve all of its actual mathematics without treating it as C29's live target:

- global full-domain lower bound for the normalized residual: `0`;
- `11/756` is only an **upper** benchmark from an explicit configuration, not a positive lower bound and not a nonexistence proof;
- exact phase examples, restricted/auxiliary bounds, atlas reductions, and failed proof routes remain historical reserve material.

At run start I discovered a newer legacy MUB report dated `2026-09-16_18-35-11__run-report.md`, written after the reserve handoff. It still reports global metric `0 -> 0` and adds an exact-zero Hadamard-atlas normal form. I preserve that theorem as reserve-only historical work; it does not reactivate the MUB target and does not change C29's current metric.

I also inspected the scheduler surface. The exposed list contains the live `C29 Brownian Shapes New Methods` replacement task but **does not expose a separate editable C29-MUB task**, despite the fresh legacy MUB report. Therefore this worker cannot safely disable or retarget the originating legacy worker: there is no corresponding editable task object in this context. The legitimate fix is for the owner/coordinator to disable or retarget that worker from the scheduler/workspace in which it is actually owned; inventing a duplicate schedule or bypassing permissions would be wrong.

## 3. Source and current-literature refresh

Meroni--Raita's current arXiv v2 (`arXiv:2509.07541`, revised 4 August 2026) defines directional convexity for `D=D_2 x R`, focuses on three planar directions, and uses an irrational `pi/3` parallelogram whose compatible planar grid is infinite. Their Question 2 asks whether vertical perturbations of the four lifted vertices can force a non-semialgebraic functional `D`-convex hull; they explicitly note that the candidate boundary planes may coincide.

The preceding C29 theorem answered that **specific four-point vertical-lift mechanism negatively** by giving the exact semialgebraic hull. The broader Randomstrasse Conjecture 34 remains open on bounded evidence because it permits other finite point configurations.

Fresh 2026-09-16 searches used the exact title/identifier and combinations of

- `Directional Convexity Meroni Raita 2509.07541 Conjecture 34 five points`,
- `Conjecture 34 Directional Convexity Meroni`, and
- `non-semialgebraic D-convex hull directional convexity`.

They recovered the current source paper and general reviews but no later source-matching resolution or five-point theorem matching the result below. This is a bounded search, **not** a proof of worldwide openness or novelty.

## 4. Previous exact four-point normal form

Use the source coordinates from the previous report. Let

\[
D_2=\mathbb R(1,0)\cup\mathbb R(0,1)\cup\mathbb R(1,-\alpha),
\qquad \alpha>1,
\]

with the source irrational ratio encoded in `alpha`, and let `D=D_2 x R` in three dimensions. The canonical four lifted vertices are

\[
K_4=\{(0,0,0),(1,0,0),(0,1,0),(1,1,1)\}.
\]

The preceding theorem proved

\[
\operatorname{conv}_D(K_4)
=K_4^{(3,D)}
=\{(s,t,z):0\le s,t\le1,\ h(s,t)\le z\le g(s,t)\},
\tag{4.1}
\]

where

\[
g(s,t)=st,
\qquad
h(s,t)=\max\left\{0,\ st-\alpha^{-1}t(1-t),\ s+t-1\right\}.
\tag{4.2}
\]

In particular `g` is the exact upper boundary and `h` the exact lower boundary.

The new question is: **how far can one perturb this already-solved geometry by adding one genuinely new lifted point before the third direction must become active in the upper-envelope construction?**

## 5. Move 1 — change category: from infinite grids to a directional envelope problem

Choose

\[
0<a<1,\qquad 0<b<1,\qquad \delta>0,
\]

and add the upward spike

\[
P_{a,b,\delta}=(a,b,ab+\delta).
\]

Set

\[
K_5=K_4\cup\{P_{a,b,\delta}\}.
\tag{5.1}
\]

Instead of tracing the infinite planar grid, view the upper hull as the least `D_2`-concave majorant of the five height data and the lower hull as the greatest `D_2`-convex minorant. This converts the first five-point attack into an exact envelope calculation.

Define the one-dimensional tents

\[
T_a(s)=
\begin{cases}
 s/a,&0\le s\le a,\\
 (1-s)/(1-a),&a\le s\le1,
\end{cases}
\qquad
T_b(t)=
\begin{cases}
 t/b,&0\le t\le b,\\
 (1-t)/(1-b),&b\le t\le1.
\end{cases}
\tag{5.2}
\]

and

\[
U_\delta(s,t)=st+\delta T_a(s)T_b(t).
\tag{5.3}
\]

The coordinate directions alone force this surface: it is the least separately concave majorant of the five lifted data. The only remaining question is whether it is also concave in the source's third direction `(1,-alpha)`.

## 6. Move 5 — add the spike parameter and locate the exact activation threshold

Define

\[
\boxed{\delta_c(a,b)=\min\{a(1-b),(1-a)b\}.}
\tag{6.1}
\]

### Theorem `C29-DC34-FIVEPOINT-SAFE-06`

For every `alpha>1`, every `0<a,b<1`, and every

\[
0<\delta\le\delta_c(a,b),
\]

the exact functional directional-convex hull of `K_5` is

\[
\boxed{
\operatorname{conv}_D(K_5)
=K_5^{(4,D)}
=\{(s,t,z):0\le s,t\le1,\ h(s,t)\le z\le U_\delta(s,t)\}.
}
\tag{6.2}
\]

Hence this whole five-point family has a semialgebraic functional `D`-convex hull obtained after finitely many laminations.

Moreover, `U_delta` is `D_2`-concave **if and only if**

\[
\delta\le\delta_c(a,b).
\tag{6.3}
\]

Thus for `delta>delta_c(a,b)` the simple coordinate-bilinear envelope fails on an open cell and a genuine third-direction concavification is mandatory. This does **not** assert non-semialgebraicity above threshold; it identifies exactly where the first nontrivial five-point mechanism begins.

### Proof

#### Step 1: `U_delta` is the least separately concave majorant

Let `u` be any function concave in the coordinate directions that majorizes the five lifted heights. Put

\[
w(s,t)=u(s,t)-st.
\]

Since `st` is affine on horizontal and vertical lines, `w` is separately concave. At the four corners,

\[
w(0,0),w(1,0),w(0,1),w(1,1)\ge0,
\]

and at the spike

\[
w(a,b)\ge\delta.
\]

Coordinate-line concavity first gives

\[
w(0,t),w(1,t),w(s,0),w(s,1)\ge0
\]

throughout the four sides. Concavity on the horizontal line `t=b`, using the spike and the two nonnegative side values, then gives

\[
w(s,b)\ge\delta T_a(s).
\]

For each fixed `s`, concavity on the vertical line through `s`, using the two nonnegative boundary values and the preceding middle value, gives

\[
w(s,t)\ge\delta T_a(s)T_b(t).
\]

Therefore every separately concave majorant satisfies

\[
u(s,t)\ge U_\delta(s,t).
\tag{6.4}
\]

Since `U_delta` interpolates the five data exactly, it is the least separately concave majorant whenever it is admissible in the third direction.

#### Step 2: exact third-direction concavity threshold

On each of the four rectangles cut by `s=a` and `t=b`, write

\[
p_s=T_a'(s),\qquad p_t=T_b'(t).
\]

For the directional derivative along `d=(1,-alpha)`, the smooth-cell second derivative is

\[
D_d^2(st)=-2\alpha,
\]

and

\[
D_d^2\bigl(\delta T_aT_b\bigr)
=-2\alpha\delta p_s p_t.
\]

Hence

\[
D_d^2U_\delta=-2\alpha(1+\delta p_s p_t).
\tag{6.5}
\]

On the southwest and northeast cells, `p_s p_t>0`, so (6.5) is strictly negative automatically. On the northwest cell,

\[
p_sp_t=-\frac1{a(1-b)},
\]

so concavity is equivalent to

\[
\delta\le a(1-b).
\]

On the southeast cell,

\[
p_sp_t=-\frac1{(1-a)b},
\]

so concavity is equivalent to

\[
\delta\le(1-a)b.
\]

Across the kink `s=a`, the directional derivative of the tent term jumps from

\[
\delta T_b/a
\quad\text{to}\quad
-\delta T_b/(1-a),
\]

which is a downward jump. Across `t=b`, remembering that `t` decreases when moving in direction `(1,-alpha)`, the directional derivative jumps from

\[
+\alpha\delta T_a/(1-b)
\quad\text{to}\quad
-\alpha\delta T_a/b,
\]

again downward. If both kinks are crossed simultaneously the jumps add and remain downward. Thus there is no hidden positive singular curvature on the interfaces.

Therefore `U_delta` is globally concave in the third direction exactly when both mixed-cell inequalities hold, i.e. exactly when (6.3) holds. For `delta>delta_c`, one of the northwest/southeast open cells has positive second directional derivative, so `U_delta` is not `D_2`-concave there.

#### Step 3: the lower boundary is unchanged

The old lower boundary `h` is `D_2`-convex and satisfies

\[
h\le st.
\]

At the new point,

\[
h(a,b)\le ab<ab+\delta,
\]

so `h-z` is still a valid `D`-convex separator for all five data and forces `z>=h` on the new functional hull.

Conversely, every `D_2`-convex minorant admissible for the five-point data is in particular admissible for the old four corner data, whose exact lower envelope is `h` by (4.1). Hence no new lower minorant can exceed `h`. The lower boundary remains exactly `h`.

#### Step 4: separators give the outer inclusion

When `delta<=delta_c`, `U_delta` is `D_2`-concave. Therefore

\[
z-U_\delta(s,t)
\]

is `D`-convex and is zero at all five lifted data points. It forces `z<=U_delta` on the functional hull. Together with `h-z`, and the old coordinate-box separators, this gives

\[
\operatorname{conv}_D(K_5)
\subseteq
\{0\le s,t\le1,\ h\le z\le U_\delta\}.
\tag{6.6}
\]

#### Step 5: finite lamination gives the reverse inclusion

The four extra cross-grid points

\[
(a,0,0),\ (a,1,a),\ (0,b,0),\ (1,b,b)
\]

are obtained in one coordinate-direction lamination from the original four corners. Together with the four corners and the spike, these are the nine nodes of the `3 x 3` grid

\[
\{0,a,1\}\times\{0,b,1\}.
\]

On each of its four rectangles, `U_delta` is bilinear because both `st` and `T_aT_b` are products of affine functions there. Starting from the four lifted corner nodes of a cell, one coordinate lamination fills two opposite lifted edges and a second coordinate lamination fills the entire bilinear graph over that cell. Accounting for the first grid-node round, the full graph of `U_delta` lies in `K_5^{(3,D)}`.

The old theorem (4.1) puts the full lower graph `(s,t,h(s,t))` inside `K_4^{(3,D)}`, hence also inside `K_5^{(3,D)}`. The pure vertical direction belongs to `D=D_2 x R`, so one more lamination round fills every vertical segment between the lower and upper graphs. Thus

\[
\{0\le s,t\le1,\ h\le z\le U_\delta\}
\subseteq K_5^{(4,D)}.
\tag{6.7}
\]

Combining (6.6), (6.7), and `K_5^{(4,D)} subset conv_D(K_5)` proves (6.2). QED.

## 7. Move 24 — the extremal safe spike is the centered one

The threshold itself has a clean extremizer:

\[
\boxed{\sup_{0<a,b<1}\delta_c(a,b)=\frac14,}
\]

with equality only at

\[
a=b=\frac12.
\]

Indeed, with

\[
x=a(1-b),\qquad y=(1-a)b,
\]

we have

\[
\delta_c=\min(x,y)\le\sqrt{xy}
=\sqrt{a(1-a)b(1-b)}\le\frac14.
\]

Equality forces `a(1-a)=b(1-b)=1/4`, hence `a=b=1/2`.

So the centered fifth point

\[
\left(\frac12,\frac12,\frac14+\delta\right)
\]

is the most stable member of this family against activation of the third direction: the simple finite formula survives exactly through `delta=1/4`. For any larger spike, third-direction concavification is compulsory.

This gives a sharply localized next target: **analyze the centered case just above `delta=1/4`**. If an infinite continued-fraction/grid cascade is ever going to survive the four-point collapse, this is the smallest symmetric five-point regime in which it can first appear.

## 8. What moved mathematically and what did not move metrically

The theorem is genuine structural progress: it proves a full exact hull formula for an open two-parameter location / one-parameter height family of five-point source-admissible configurations and identifies the exact transition at which the third source direction becomes active.

However, the frozen C29 metric is tied to the already-fixed four-point lifted irrational-parallelogram candidate. That metric remains

\[
\boxed{N=2.}
\]

I do not count affine patches from a different five-point configuration as movement. Accordingly this is **no movement**, unchanged-run count `1` after the previous run's reset.

Status remains **PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY**. The general Randomstrasse Conjecture 34 is not proved or refuted, and semialgebraicity above the threshold `delta_c` remains open.

No checker was manufactured for this theorem: it is an analytic/envelope theorem, and the full proof is written above. There is no finite enumeration claim whose truth is being inferred from numerical output.

## 9. Directed C30 audit — newest claim, not a redundant old audit

The newest C30 theorem is `C30-RANK2-REGULAR-01` for the fixed Sidorenko graph `H=K_{5,5}\setminus C_{10}`. C30 claims that every bounded symmetric nonnegative `1`-regular kernel of operator rank at most two satisfies

\[
t_H(A)\ge1,
\]

with equality only for `A=1`.

I independently checked the finite algebraic core using the complementary-cycle presentation of `H` (rather than C30's cyclic-neighbor presentation). Expanding

\[
A=1+\lambda f\otimes f,
\qquad \int f=0,\quad\int f^2=1,
\]

leaves exactly `625` edge subsets with no degree-one vertex. The resulting seventeen `(edge count, number of degree-3 pairs)` multiplicities agree term-for-term with C30's archived polynomial expansion. I also independently reconstructed the transformed polynomial in the dangerous `lambda=-s` case and obtained bidegree `(16,11)` with all `204` tensor-product Bernstein coefficients nonnegative, minimum `5` and maximum `63`.

The nonnegativity-domain reduction is also sound: positivity of `1-s f(x)f(y)` gives the pointwise bounds needed for the two cubic moment inequalities and hence

\[
r^2\le\frac{(1-s)^2}{s}.
\]

After `s=ay` and `r^2=(1-a)^2/a`, the positive Bernstein certificate proves strict positivity away from the constant kernel.

Verdict:

\[
\boxed{\texttt{C29-AUDIT-C30-RANK2-REGULAR-02 = PASS (claim-scoped)}.}
\]

Scope: the rank-at-most-two **regular-kernel theorem and equality statement** only. This audit does not certify the external regular-graphon reduction, Zhao's universal conjugacy-averaging comparison, or source-level Sidorenko closure.

C30's archived exact checker and output remain the finite certificate; I did not create a duplicate receipt-only artifact.

## 10. Model/scheduler control — fresh interface check

A fresh inspection of the actual scheduler objects again shows fields for title, prompt, schedule, timing mode, enablement and notification metadata, but **no model-family field and no reasoning-effort field**. GPT-6/maximum is therefore still prompt-only in this interface. Enforcing it would require the scheduler/backend or an authorized enclosing runtime to expose and pin those selectors.

The legacy P26 `You cannot modify this task` behavior is a permission/ownership-context boundary. The supported workaround is modification from the task's owning workspace/account by an authorized owner/admin or platform support; bypassing permissions is not valid.

The newly observed legacy C29-MUB writer is a distinct operational issue: its producing task is not present as a separately editable object in this scheduler list, so there is nothing this worker can safely disable here. The owner/coordinator must act in the originating task context if that legacy worker is to be stopped.

## 11. Next route

Do **not** return to another four-point lemma. The next C29 run should start at the exact transition found here:

\[
a=b=\frac12,\qquad \delta>\frac14,
\]

and study the alternating least-concave-majorant operators generated by the coordinate directions and `(1,-alpha)`. The concrete question is whether the supercritical centered spike closes after finitely many envelope updates or generates a continued-fraction-indexed infinite sequence of genuinely distinct supporting patches. That is the first regime in this route where the source's infinite-grid mechanism is no longer killed in one third-direction step.

Use three new Section-B moves, not `{1,5,24}` again.

## ledger_delta for P26

```text
track: C29
active_target: RS-2026-DC34 (fallback; I0077 excluded to R07)
metric_definition: fixed four-point candidate, number of certified distinct affine boundary patches
metric_before: 2
metric_after: 2
movement: no
unchanged_count: 1
status: PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY
new_claim: C29-DC34-FIVEPOINT-SAFE-06
new_structural_result: exact five-point hull for 0<delta<=min{a(1-b),(1-a)b}; centered safe threshold maximized at 1/4
audit: C29-AUDIT-C30-RANK2-REGULAR-02 = PASS (claim-scoped)
I0077: remains R07-owned; newest R07 report has one nonparabolic shape family
MUB: HARD RESERVE; preserve metric 0 and all historical bounds/routes; a fresh legacy MUB report appeared despite reserve and should not reactivate the target
shared_ledgers: not edited by C29
```
