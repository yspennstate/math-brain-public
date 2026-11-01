Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 12500/148461 -> 3125/37092`. Methods tried: B8 / B18 / B25.**

# HARD7-03 — exact order-cone target-domination correction

Status: **PARTIAL / Seppäläinen Problem 4 remains open as a whole.** This run resumes the exclusive `D0025` claim and improves the frozen `K=2`, binary site-disorder plateau certificate by replacing the preceding small sufficient domination events with the full target-domination events that are actually needed for the same three-endpoint max-plus collapse.

## 1. Continuity, ownership, source status, and required repository reads

The active canonical claim remains `operations/claims/D0025.md`, owned by `HARD7-03`, canonical key `disordered_asep_open_1999::problem_4`. I resumed the newest own report

`runs/hard7_2026-09-18/HARD7-03/20260919T0723Z__d0025-four-step-triple-slack-domination.md`

rather than restarting admission.

Before the new mathematics I re-read the controlling HARD7 policy, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the active D0025 claim, the indexed D-intake/canonical-key material, and the newest neighboring HARD7-02 / HARD7-04 state. No release, competing owner, posted equivalent, or source-resolution record surfaced.

Primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), Problem 4, Section 4; arXiv `math/9906194`; DOI `10.11606/resimeusp.v4i1.74889`.

A bounded 2026-09-19 current-literature refresh searched the source title and the phrases `disordered K-exclusion plateau site disorder K>=2`, `general K TASEP site disorder plateau`, and `asymmetric partial exclusion site disorder plateau`. It recovered Seppäläinen's source, Allan Sly's 2016 `K=1` plateau theorem (`arXiv:1609.06589`), and Gonçalves--Hayashi--Sasada's distinct product-rate/gradient partial-exclusion model (`arXiv:2405.15142`). I did not locate a 2024--2026 theorem closing the exact general-`K>=2` iid site-rate residual. This is bounded negative evidence only, not a worldwide-openness or novelty certificate.

The frozen test case remains

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

with

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

The fixed tracked quantity is a rigorous lower bound `L <= Delta_2(Q)`.

## 2. Before/after movement

The preceding checkpoint certified

\[
G_1(0)\le \frac{148461}{50000}=2.96922,
\qquad
L\ge \frac{12500}{148461}=0.084197196570143\ldots .
\]

This run proves

\[
\boxed{G_1(0)\le \frac{9273}{3125}=2.96736}
\]

and therefore, by the already established slow-rate cusp/plateau transfer,

\[
\boxed{
\Delta_2(Q)\ge \frac1{4G_1(0)}
\ge \frac{3125}{37092}
=0.0842499730400086\ldots .}
\]

Thus

\[
L:\quad \frac{12500}{148461}
\longrightarrow \frac{3125}{37092},
\]

with exact gain

\[
\frac{3125}{37092}-\frac{12500}{148461}
=\frac{96875}{1835571804}>0.
\]

This resets the unchanged-run count: the frozen source-relevant metric moved in this run.

## 3. New idea before code

The preceding report bounded each three-endpoint slack by restricting to a small product event that was sufficient to force one layer-two passage value to dominate its relevant competitors. That loses most of the useful event.

The new route is to integrate the **entire target-domination event exactly**.

Write the first-layer iid `Exp(1)` variables as `A_{-1},A_0,A_1`, and the second-layer iid `Exp(1)` endpoint weights as `B_j`. As in the previous checkpoint,

\[
\begin{aligned}
Y_{-2}&=A_{-1}+B_{-2},\\
Y_{-1}&=\max(A_{-1},A_0)+B_{-1},\\
Y_0&=\max(A_{-1},A_0,A_1)+B_0,\\
Y_1&=\max(A_0,A_1)+B_1,\\
Y_2&=A_1+B_2.
\end{aligned}
\]

For the fourth-step triple centered at `d=2`, it is enough that `Y_2>=Y_1`; for `d=1`, it is enough that

\[
Y_1\ge \max(Y_{-1},Y_0,Y_2);
\]

for `d=0`, it is enough that

\[
Y_0\ge \max(Y_{-2},Y_{-1},Y_1,Y_2).
\]

On these events the relevant sliding predecessor maxima coincide with the target value (or, at the edge, the unused outer base can only increase the slack), so the same independent third-layer factor

\[
\kappa(\theta)=\frac{\theta}{(2-\theta)(3-\theta)}
\]

applies exactly as in the preceding report.

The idea was recorded before the checker in

`artifacts/hard7_2026-09-18/HARD7-03/20260919T0823Z__idea-order-cone-target-domination.md`

at commit `fa01e5336fc54cf7f156d2cedf89e58d5b3850c7`.

## 4. B18 — translate to shifted-exponential target ordering

Conditional on the first-layer `A` variables, each relevant `Y_j` has the form

\[
Y_j=u_j+B_j,
\]

where the `B_j` are iid unit exponentials and each deterministic base `u_j` is a maximum of a subset of the three `A` variables.

Fix a target `i`, let `J` be the relevant endpoint set, and write

\[
M=\max_{j\in J}u_j.
\]

For `0<theta<1`, define the conditional weighted target-max contribution

\[
W_i(u;\theta)=
\mathbb E\big[e^{\theta Y_i}\mathbf 1\{Y_i\ge Y_j\ \forall j\in J\}\mid u\big].
\]

Conditioning on the target value `y=Y_i` gives the exact integral

\[
W_i(u;\theta)
=e^{u_i}\int_M^\infty e^{-(1-\theta)y}
\prod_{j\ne i}(1-e^{-(y-u_j)})\,dy.
\tag{4.1}
\]

Expanding the finite product yields

\[
W_i(u;\theta)
=e^{u_i}
\sum_{S\subseteq J\setminus\{i\}}
(-1)^{|S|}
\frac{
 e^{\sum_{j\in S}u_j}
 e^{-(1-\theta+|S|)M}
}{1-\theta+|S|}.
\tag{4.2}
\]

**B18 outcome: successful.** The max-plus dependence is converted into a finite shifted-exponential order-statistic calculation; no sampling or asymptotic approximation is involved.

## 5. B8 — discretize the first layer into six exact order cones

Split the positive octant for `(A_{-1},A_0,A_1)` into the six order cones. On one cone write

\[
0\le x_1\le x_2\le x_3.
\]

Every base `u_j` and `M` in (4.2) equals one of `x_1,x_2,x_3`. Hence each inclusion-exclusion term is

\[
\exp(c_1x_1+c_2x_2+c_3x_3)
\]

times the iid exponential density `exp(-(x_1+x_2+x_3))`. With gaps

\[
x_1=g_1,\qquad x_2=g_1+g_2,\qquad x_3=g_1+g_2+g_3,
\]

the cone integral is exactly

\[
I(c_1,c_2,c_3)=
\frac{1}{
(3-c_1-c_2-c_3)
(2-c_2-c_3)
(1-c_3)}
\tag{5.1}
\]

whenever the three displayed rates are positive. For the rational `theta` used below, every generated term satisfies this condition.

Thus the full target-domination weights are finite rational sums over six cones and finitely many competitor subsets.

**B8 outcome: successful.** The continuous three-variable integral is reduced exactly to six finite order cones; this is exhaustive for the stated target-domination events, unlike finite sampling.

## 6. B25 — count the same target-max event twice

The checker evaluates the target-max weight in two equivalent ways: (i) by the max-plus event defining which layer-two endpoint dominates the sliding windows, and (ii) by the CDF/inclusion-exclusion integral (4.2) on the six first-layer order cones.

At

\[
\theta=\frac{47}{80},
\]

the exact weights are

\[
\begin{aligned}
W_2&=
\frac{5980160000}{1571314833}
=3.805831825938093\ldots,\\
W_1&=
\frac{888568922767360000000}{198396423368854513803}
=4.478754746073981\ldots,\\
W_0&=
\frac{19118590577868800000000}{3334949402343125874879}
=5.732797794304205\ldots .
\end{aligned}
\tag{6.1}
\]

For the edge term there is also a separate direct integral. Since `Y_2=A_1+B_2` and `Y_1=max(A_0,A_1)+B_1`, conditioning on `A_0,A_1,B_1` and integrating `B_2` from its exact threshold gives

\[
W_2(\theta)=
\frac{3-2\theta}{(1-\theta)^2(2-\theta)^3}.
\tag{6.2}
\]

The checker verifies (6.2) agrees exactly with the six-cone routine at `theta=47/80`.

**B25 outcome: successful.** The independently derived edge closed form exactly matches the generic order-cone calculation and supplies a nontrivial internal identity check.

## 7. Stronger triple-slack subtraction

Let

\[
H_{\rm dom}(\theta)
=\kappa(\theta)\bigl(2W_2(\theta)+2W_1(\theta)+W_0(\theta)\bigr).
\tag{7.1}
\]

At `theta=47/80`, exact arithmetic gives

\[
H_{\rm dom}
=\frac{50194227262480567500800000}
{13054445656664323729144943}
=3.844991092123188\ldots .
\tag{7.2}
\]

For comparison, evaluating the previous report's smaller sufficient-event subtraction at the same `theta` gives

\[
H_{\rm old}
=\frac{692172622849638400000}
{362870142223863437163}
=1.907494010412739\ldots,
\]

and the checker proves `H_dom-H_old>0` exactly.

Keeping the preceding exact `A_3(theta)` and adjacent-pair subtraction `C(theta)`, the fourth-step MGF sum therefore obeys

\[
A_4^{\rm actual}(\theta)
\le
U_4^{\rm dom}(\theta)
:=\frac{3A_3(\theta)-C(\theta)-H_{\rm dom}(\theta)}{1-\theta}.
\tag{7.3}
\]

At `theta=47/80`,

\[
U_4^{\rm dom}
=\frac{5059630605064232222491525120000}
{4738763773369149513679614309}
=1067.711083953643538\ldots .
\tag{7.4}
\]

## 8. Exact Chernoff certificate for the improved shape bound

Choose

\[
a=\frac{9273}{3125}=2.96736,
\qquad
x=4\theta a=\frac{435831}{62500}.
\]

The exact checker forms

\[
S_{20}(x)=\sum_{k=0}^{20}\frac{x^k}{k!}
\]

and proves

\[
S_{20}(x)-U_4^{\rm dom}(47/80)>0.
\tag{8.1}
\]

Because `x>0`, `S_20(x)<e^x`, so (8.1) implies

\[
U_4^{\rm dom}(47/80)e^{-4\theta a}<1.
\tag{8.2}
\]

The already proved four-layer block-concatenation/Chernoff argument therefore gives

\[
G_1(0)\le a=\frac{9273}{3125}.
\tag{8.3}
\]

No discrete-path simulation is used in this implication.

## 9. Exact artifacts and self-check status

Created and executed locally with exact `Fraction` arithmetic, then archived on GitHub:

- idea-before-code note: `artifacts/hard7_2026-09-18/HARD7-03/20260919T0823Z__idea-order-cone-target-domination.md`, commit `fa01e5336fc54cf7f156d2cedf89e58d5b3850c7`;
- checker: `artifacts/hard7_2026-09-18/HARD7-03/order_cone_target_domination_20260919T0823Z.py`, commit `fba2e3e5006d9e779453e18b36c49d5c1edd8e2b`;
- archived output: `artifacts/hard7_2026-09-18/HARD7-03/order_cone_target_domination_20260919T0823Z.out`, commit `961cbc86dbfa16235d6a2d7c897adfce8f9605fa`.

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit. The source problem is not closed.

## 10. What remains

The present gain comes only from the part of each triple-slack event on which a single layer-two endpoint dominates all windows required for that center. Positive triple slack also occurs outside those target-domination events. The next non-redundant route should attack that complement rather than merely increase Taylor precision or rerun the same six-cone checker.

A promising next target is the exact conditional third-layer slack as a function of the three sliding bases `(S_{d-1},S_d,S_{d+1})`: integrate the three fresh exponentials first, obtain a piecewise closed form in the two base gaps, and then seek a tractable lower bound whose expectation depends only on order-cone quantities already available. This is qualitatively different from simply adding another sufficient dominance event.

Next methods should not repeat B8/B18/B25.

## 11. Scheduler/model capability statement

The runtime exposed to this report is **GPT-5.6 Sol; reasoning level is not exposed, hence UNVERIFIED**. The current scheduler action schema exposes task title, prompt, schedule, timing mode and enabled state, but no model selector, no reasoning-effort selector and no guaranteed execution duration. Therefore the requested GPT-6/maximum setting still cannot be installed natively from this interface; prompt text is not a selector. Changing the actual scheduled model/reasoning would require the platform to expose authoritative model/reasoning fields, or an authorized account/workspace control outside the present scheduler schema.

The repository policy records prior native modification probes for P26/P01/P03 returning `You cannot modify this task`. This run does not retry or bypass that restriction and does not create a duplicate schedule. The authorized workaround remains to change the task through the account/workspace that owns it or escalate through platform support/administration; repository edits cannot repair native scheduler ownership.

## 12. Ledger delta for designated reconciler

```yaml
track: HARD7-03
claim: D0025
source: Seppalainen 1999 Problem 4
status: PARTIAL
frozen_case: K=2; Q=1/2 delta_{1/2}+1/2 delta_1
metric: rigorous lower bound L <= Delta_2(Q)
before: 12500/148461
after: 3125/37092
shape_bound_before: G_1(0) <= 148461/50000
shape_bound_after: G_1(0) <= 9273/3125
methods: [B8, B18, B25]
unchanged_runs: 0
closure: false
independent_audits_this_run: 0
```
