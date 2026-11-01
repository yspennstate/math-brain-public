Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 3125/37092 -> 3125/37086`. Methods tried: B5 / B13 / B19.**

# HARD7-03 — local-minimum predecessor geometry improves the D0025 plateau certificate

Status: **PARTIAL / Seppäläinen Problem 4 remains open as a whole.** This run resumes the exclusive `D0025` claim. The mathematical advance is to replace the preceding endpoint-domination sufficient events by the exact event on which the middle predecessor maximum is a local minimum. This enlarges the portion of the three-endpoint max-plus slack that can be integrated rigorously and improves the frozen `K=2` binary-disorder plateau half-width.

## 1. Continuity, ownership, and source/current-status check

Active claim: `operations/claims/D0025.md`, owner `HARD7-03`, canonical key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`. I resumed the latest own checkpoint

`runs/hard7_2026-09-18/HARD7-03/20260919T0823Z__d0025-order-cone-target-domination.md`

rather than restarting admission.

Before the new mathematics I re-read/recovered:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/D0025.md`;
- the newest own HARD7-03 checkpoint and the newest visible neighboring HARD7-02 / HARD7-04 state.

No release, competing D0025 owner, posted equivalent, or source-resolution record surfaced. HARD7-02 remains on a distinct random-matrix target; HARD7-04 remains on a distinct growing-random-graph target.

Primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), Problem 4, Section 4; arXiv `math/9906194`; DOI `10.11606/resimeusp.v4i1.74889`.

Bounded current-literature refresh on 2026-09-19:

- source journal page: `https://revistas.usp.br/resenhasimeusp/pt_BR/article/view/74889`;
- source arXiv: `https://arxiv.org/abs/math/9906194`;
- Allan Sly, *Note on the flux for TASEP with general disorder*, `https://arxiv.org/abs/1609.06589`, proves the iid site-disorder plateau for ordinary `K=1` TASEP around density `1/2`;
- Gonçalves--Hayashi--Sasada, *Characterization of Gradient Condition for Asymmetric Partial Exclusion Processes and Their Scaling Limits*, `https://arxiv.org/abs/2405.15142`, treats a product-rate/gradient partial-exclusion class, not the source's iid site-rate general-`K` model;
- Ayyer--Misra, *An exactly solvable asymmetric K-exclusion process*, J. Phys. A 57 (2024), DOI `10.1088/1751-8121/ad5edd`, is a different `(q,t)`-deformed finite-ring model;
- Sakai--Akimoto, *Symmetry breaking of current response in disordered exclusion processes*, Phys. Rev. E 113 (2026), 044123, DOI `10.1103/21vm-n8gp`, concerns bias-reversal/current-response symmetry and does not close the general-`K>=2` plateau question.

Queries included the exact source title and combinations of `site disordered K-exclusion plateau K>=2`, `general K TASEP site disorder plateau`, and `partial exclusion asymmetric disorder`. I did not locate a 2024--2026 theorem closing the exact `K>=2` iid site-rate residual. This is bounded negative evidence only, not a worldwide openness or novelty certificate.

The frozen source-relevant test case remains

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

with

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

The tracked quantity remains a rigorous lower bound `L <= Delta_2(Q)`.

## 2. Before/after movement

The preceding checkpoint certified

\[
G_1(0)\le \frac{9273}{3125}=2.96736,
\qquad
L\ge \frac{3125}{37092}
=0.0842499730400086\ldots .
\tag{2.1}
\]

This run proves

\[
\boxed{G_1(0)\le \frac{18543}{6250}=2.96688}
\tag{2.2}
\]

and, by the already established slow-rate cusp/plateau transfer used in the checkpoint chain,

\[
\boxed{
\Delta_2(Q)\ge \frac1{4G_1(0)}
\ge \frac{3125}{37086}
=0.0842636035161516\ldots .}
\tag{2.3}
\]

Hence

\[
L:\quad \frac{3125}{37092}
\longrightarrow \frac{3125}{37086},
\]

with exact gain

\[
\frac{3125}{37086}-\frac{3125}{37092}
=\frac{3125}{229265652}>0.
\tag{2.4}
\]

The unchanged-run count is therefore reset.

## 3. New idea before code

The previous run recovered only those triple-slack configurations where one layer-two endpoint dominated every sliding window needed for a given center. That condition is sufficient but stronger than necessary.

The actual condition needed for the universal fresh-layer slack factor is only that the *middle sliding predecessor maximum is no larger than the two neighboring predecessor maxima*.

This idea was written before code in

`artifacts/hard7_2026-09-18/HARD7-03/20260919T0920Z__idea-local-min-slack.md`

at commit `32e893ae1163e86a2835ac83fe335ff6285bf10a` and read back successfully at that commit.

## 4. B5 — add the two predecessor-gap parameters

Recall the exact three-endpoint slack from the four-step max/min identity. Conditional on layer-two sliding maxima

\[
a=S_{d-1},\qquad b=S_d,\qquad c=S_{d+1},
\]

and fresh independent unit exponentials `C_L,C_M,C_R`, put

\[
u=a-b,\qquad v=c-b.
\]

Then

\[
\begin{aligned}
&\mathbb E\left[
\left(
\min(e^{\theta(a+C_L)},e^{\theta(c+C_R)})
-e^{\theta(b+C_M)}
\right)_+
\,\middle|\,a,b,c\right]\\
&\qquad = e^{\theta b}\Phi_\theta(u,v),
\end{aligned}
\tag{4.1}
\]

where

\[
\Phi_\theta(u,v)
:=\mathbb E\left[
\left(e^{\theta\min(u+C_L,v+C_R)}-e^{\theta C_M}\right)_+
\right].
\tag{4.2}
\]

For real `x,y`,

\[
(e^{\theta x}-e^{\theta y})_+
=\theta\int_0^\infty e^{\theta t}
\mathbf 1\{y<t<x\}\,dt.
\]

Using independence gives the exact representation

\[
\boxed{
\Phi_\theta(u,v)=
\theta\int_0^\infty
 e^{\theta t}(1-e^{-t})
 e^{-(t-u)_+-(t-v)_+}\,dt.}
\tag{4.3}
\]

This is valid for arbitrary real `u,v` for which `0<theta<1` here.

**B5 outcome: successful.** The discarded three-endpoint slack becomes an explicit two-parameter function of predecessor gaps rather than a binary endpoint-domination event.

## 5. B13 — the middle predecessor only has to be a local minimum

Equation (4.3) is coordinatewise nondecreasing in `(u,v)`. Therefore on

\[
E_d:=\{S_d\le S_{d-1},\ S_d\le S_{d+1}\},
\tag{5.1}
\]

we have `u,v>=0`, so

\[
\Phi_\theta(u,v)\ge \Phi_\theta(0,0).
\]

The value at the origin is elementary:

\[
\begin{aligned}
\Phi_\theta(0,0)
&=\theta\int_0^\infty
 e^{-(2-\theta)t}(1-e^{-t})\,dt\\
&=\frac{\theta}{(2-\theta)(3-\theta)}
=:\kappa(\theta).
\end{aligned}
\tag{5.2}
\]

Consequently the exact triple slack obeys

\[
\boxed{
R_d(\theta)
\ge
\kappa(\theta)
\mathbb E[e^{\theta S_d};E_d].}
\tag{5.3}
\]

This strictly relaxes the previous sufficient condition: endpoint domination implies the appropriate local-minimum geometry, but the converse need not hold.

**B13 outcome: successful.** The order-theoretic invariant needed by the slack factor is local minimality of `S_d`, not global domination by one `Y` endpoint.

## 6. Exact decomposition of the local-minimum events

Write the first-layer iid unit exponentials as `A_{-1},A_0,A_1` and the second-layer iid unit exponentials as `B_{-2},...,B_2`. As before,

\[
\begin{aligned}
Y_{-2}&=A_{-1}+B_{-2},\\
Y_{-1}&=\max(A_{-1},A_0)+B_{-1},\\
Y_0&=\max(A_{-1},A_0,A_1)+B_0,\\
Y_1&=\max(A_0,A_1)+B_1,\\
Y_2&=A_1+B_2.
\end{aligned}
\tag{6.1}
\]

The sliding maxima are

\[
S_e=\max\{Y_z:|z-e|\le1,\ -2\le z\le2\}.
\tag{6.2}
\]

Ties have probability zero.

### Edge center `d=2`

Here `S_2=max(Y_1,Y_2)` and the outer neighbor uses only `Y_2`; the local-minimum event reduces exactly to

\[
E_2=\{Y_2\ge Y_1\},
\qquad S_2=Y_2\quad\text{on }E_2.
\tag{6.3}
\]

Thus the edge weight is exactly the already-known weighted two-way target-max event.

### Near-edge center `d=1`

Here

\[
S_0=\max(Y_{-1},Y_0,Y_1),\quad
S_1=\max(Y_0,Y_1,Y_2),\quad
S_2=\max(Y_1,Y_2).
\]

Condition on which variable attains `S_1`. If it is `Y_1`, both neighboring windows contain `Y_1`, so local minimality is automatic. If it is `Y_2`, the right inequality is automatic and the left inequality forces `Y_{-1}>=Y_2`. Therefore the disjoint decomposition is

\[
\boxed{
E_1=
\{Y_1\ge\max(Y_0,Y_2)\}
\ \dot\cup\ 
\{Y_{-1}\ge Y_2\ge\max(Y_0,Y_1)\}.}
\tag{6.4}
\]

On the first piece `S_1=Y_1`; on the second `S_1=Y_2`.

### Central center `d=0`

Now

\[
\begin{aligned}
S_{-1}&=\max(Y_{-2},Y_{-1},Y_0),\\
S_0&=\max(Y_{-1},Y_0,Y_1),\\
S_1&=\max(Y_0,Y_1,Y_2).
\end{aligned}
\]

If `S_0=Y_0`, both neighbors contain `Y_0`, so local minimality is automatic. If `S_0=Y_{-1}`, the right neighbor must reach at least `Y_{-1}`, and because `Y_0,Y_1<=Y_{-1}`, this is equivalent to `Y_2>=Y_{-1}`. The case `S_0=Y_1` is the reflection. Hence

\[
\boxed{
\begin{aligned}
E_0={}&\{Y_0\ge\max(Y_{-1},Y_1)\}\\
&\dot\cup\{Y_2\ge Y_{-1}\ge\max(Y_0,Y_1)\}\\
&\dot\cup\{Y_{-2}\ge Y_1\ge\max(Y_{-1},Y_0)\}.
\end{aligned}}
\tag{6.5}
\]

This decomposition is exhaustive and exact; no finite sampling is used.

## 7. B19 — exact order-cone algorithm for the new chain events

Conditional on the `A` variables, every layer-two endpoint has the form

\[
Y_j=u_j+B_j
\]

with independent unit exponentials `B_j`; each base `u_j` is the maximum of a fixed subset of the three `A` variables.

Target-max events were already reduced to six exact `A`-ordering cones in the previous checkpoint. The only new object is a chain event

\[
Y_U\ge Y_T\ge Y_\ell\quad(\ell\in L)
\tag{7.1}
\]

weighted by `e^{theta Y_T}`.

Condition on `Y_T=y`. The target contributes

\[
e^{u_T}e^{-(1-\theta)y}\,dy.
\]

Each lower variable contributes the CDF factor

\[
1-e^{-(y-u_\ell)}
\]

once `y` is above its base. The upper variable contributes survival probability `1` for `y<=u_U` and `e^{-(y-u_U)}` for `y>u_U`. Thus one expands the finite product over lower variables and splits the `y`-integral once at `u_U`.

On each of the six order cones for `(A_{-1},A_0,A_1)`, all bases equal one of the ordered values

\[
0\le x_1\le x_2\le x_3.
\]

Every resulting term is an exponential monomial in `(x_1,x_2,x_3)`. With gap variables, its cone integral is exactly

\[
I(c_1,c_2,c_3)=
\frac{1}{
(3-c_1-c_2-c_3)(2-c_2-c_3)(1-c_3)}
\tag{7.2}
\]

when the generated rates are positive. For the rational `theta` used below all generated terms satisfy this condition.

Therefore every weight in (6.3)--(6.5) is computed as a finite rational sum. This is an exhaustive exact integration of those events, not Monte Carlo or finite-path evidence.

**B19 outcome: successful.** The stronger event family is algorithmically integrable with the same six order cones, but through a new chain-event integral rather than another target-max-only checker.

## 8. Exact local-minimum subtraction

At

\[
\theta=\frac{5871}{10000},
\]

the exact checker obtains the weighted local-minimum masses

\[
\begin{aligned}
M_2&:=\mathbb E[e^{\theta S_2};E_2]
\approx 3.79690002141001,\\
M_1&:=\mathbb E[e^{\theta S_1};E_1]
\approx 5.21386180336421,\\
M_0&:=\mathbb E[e^{\theta S_0};E_0]
\approx 7.04819139395704.
\end{aligned}
\tag{8.1}
\]

The exact rational values are archived in the checker output. Reflection supplies the negative centers.

Define

\[
H_{\rm loc}(\theta)
:=\kappa(\theta)(2M_2+2M_1+M_0).
\tag{8.2}
\]

The checker also evaluates the previous run's target-domination subtraction at the same `theta`, `H_dom(theta)`, and proves exactly

\[
H_{\rm loc}(\theta)-H_{\rm dom}(\theta)
=\frac{
328978900908734025206360000000000000000000000000000
}{
675637265039165665816823049189197174719368069601947
}>0.
\tag{8.3}
\]

Numerically the gain is approximately `0.48691645` in the MGF subtraction. In particular, the local-minimum event is not merely a reformulation: it gives a strictly stronger quantitative certificate.

Using the unchanged exact `A_3(theta)` and adjacent-pair correction `C(theta)` from the verified four-step chain, the actual fourth-step MGF sum obeys

\[
A_4^{\rm actual}(\theta)
\le
U_4^{\rm loc}(\theta)
:=\frac{3A_3(\theta)-C(\theta)-H_{\rm loc}(\theta)}{1-\theta}.
\tag{8.4}
\]

The exact output gives

\[
U_4^{\rm loc}(5871/10000)
\approx 1061.475021460785456.
\tag{8.5}
\]

## 9. Exact Chernoff certificate for the improved shape bound

Set

\[
a=\frac{18543}{6250}=2.96688,
\qquad
x=4\theta a
=\frac{108865953}{15625000}.
\tag{9.1}
\]

The exact checker forms the rational Taylor lower sum

\[
S_{24}(x)=\sum_{k=0}^{24}\frac{x^k}{k!}
\]

and proves

\[
S_{24}(x)-U_4^{\rm loc}(\theta)>0,
\tag{9.2}
\]

with numerical margin

\[
0.006521655521364\ldots .
\]

Since `x>0`, `S_24(x)<e^x`, hence

\[
U_4^{\rm loc}(\theta)e^{-4\theta a}<1.
\tag{9.3}
\]

The already established four-layer block-concatenation/Chernoff argument in the D0025 checkpoint chain then yields

\[
G_1(0)\le a=\frac{18543}{6250}.
\tag{9.4}
\]

Substitution into the already established slow-rate cusp/plateau transfer proves (2.3). The conclusion is asymptotic and rigorous within that established chain; it is not inferred from a finite simulation.

## 10. Exact artifacts and verification status

Idea-before-code note:

`artifacts/hard7_2026-09-18/HARD7-03/20260919T0920Z__idea-local-min-slack.md`

commit `32e893ae1163e86a2835ac83fe335ff6285bf10a`, read back successfully.

Exact `Fraction` checker:

`artifacts/hard7_2026-09-18/HARD7-03/local_min_slack_20260919T0920Z.py`

commit `03a7f132cf0b0fd4da7b48df72d53520abba9cdd`, read back successfully.

Archived exact output:

`artifacts/hard7_2026-09-18/HARD7-03/local_min_slack_20260919T0920Z.out`

commit `d03b738d1aed6ef9b1ad995b3ad927dfa8daaf14`, read back successfully. The output ends

`ALL_EXACT_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit. Seppäläinen Problem 4 is not closed.

## 11. What remains and next genuinely different route

The local-minimum argument still discards two kinds of positive slack:

1. configurations outside `E_d` can have positive `Phi_theta(u,v)` even when one predecessor gap is negative;
2. on `E_d`, replacing the exact gap-dependent `Phi_theta(u,v)` by its minimum `kappa(theta)` discards the positive gain from `u>0` or `v>0`.

A non-redundant next attack should therefore use the explicit two-gap formula (4.3) itself, not add another sufficient endpoint-order event. One candidate is to derive a globally valid piecewise lower envelope for `Phi_theta(u,v)` on the sign chambers of `(u,v)`, then integrate that envelope against the exact six-cone law of the sliding-max gaps. Another is to integrate `Phi_theta` first over the fresh layer and then over complete max-plus order chambers for one center. Either route would attack slack presently omitted by both the target-domination and local-minimum certificates.

The next run must not repeat B5/B13/B19.

## 12. Model/scheduler capability statement

The exposed scheduler interface available to this task still has fields for title, prompt, schedule/timing mode, and enabled state; it exposes **no model selector and no reasoning-effort selector**. Therefore GPT-6/maximum remains a text request, not a native configuration that this worker can set or verify. The actual model for this run is GPT-5.6 Sol; reasoning telemetry is unavailable and is reported `UNVERIFIED`.

Changing this requires the platform/backend or an authorized workspace interface to expose a model/reasoning field for scheduled tasks; a repository edit cannot do it.

The previously recorded `You cannot modify this task` result for a P26 scheduler context was **not reprobed here**, because this worker is expressly forbidden to modify other schedules. The recorded safe workaround remains: use the task/account/workspace owner context that has modification authority, or platform support if ownership is incorrect. Do not bypass the restriction or create a duplicate schedule. Root `RESULTS.md` records that a different authorized native context later succeeded in updating P26, illustrating that the denial is context/permission-sensitive rather than something a repository commit can repair.

## 13. Ledger delta for the designated shared-root reconciler

This worker does not edit shared root ledgers directly.

```yaml
ledger_delta:
  track: HARD7-03
  claim: D0025
  source: Seppalainen 1999 Problem 4
  status: PARTIAL
  fixed_metric: "rigorous lower bound L <= Delta_2(Q) for K=2, Q=1/2 delta_1/2 + 1/2 delta_1"
  before: "3125/37092"
  after: "3125/37086"
  exact_gain: "3125/229265652"
  shape_bound_before: "G_1(0) <= 9273/3125"
  shape_bound_after: "G_1(0) <= 18543/6250"
  methods: [B5, B13, B19]
  source_verdict: OPEN
  closure_claimed: false
  self_check: PASS
  independent_audits_this_run: 0
  unchanged_run_count: 0
  next_obligation: "integrate a gap-dependent lower envelope for Phi_theta(u,v) beyond the local-minimum chamber"
```
