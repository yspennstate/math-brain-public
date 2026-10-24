Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 5000000/58398337 -> 25000000/291978907`. Methods tried: B5 / B19 / B24.**

# HARD7-03 — central double-outrunner completes the strict local-minimum chamber

Status: **PARTIAL**. Seppäläinen Problem 4 remains open in its full source scope.

## 1. Continuity, ownership, required reads, and source status

This run resumes the exclusive canonical claim

`operations/claims/D0025.md`, owner `HARD7-03`, key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`.

At run start I re-read the governing files

- `operations/hard7_2026-09-18/CONTROL.md`,
- `operations/NEW_METHODS_2026-09-16.md`,
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`,
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`,
- the D0025 claim/intake/search trail,
- the latest own checkpoint `runs/hard7_2026-09-18/HARD7-03/20260919T2021Z__d0025-near-center-boundary-triple-slack.md`,
- and the newest visible neighboring HARD7-02 / HARD7-04 directory states.

HARD7-02 and HARD7-04 remain on distinct non-Hermitian-random-matrix and growing-random-graph targets. Immediately before this report I re-read `operations/claims/D0025.md`; HARD7-03 remains the owner and no release, competing canonical claim, or posted equivalent appeared. Shared root ledgers were not edited.

The primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1--15, Problem 4, Section 4, arXiv `math/9906194`, DOI `10.11606/resimeusp.v4i1.74889`:

- journal page: `https://revistas.usp.br/resenhasimeusp/pt_BR/article/view/74889`;
- arXiv: `https://arxiv.org/abs/math/9906194`.

A fresh bounded literature search in this run used the exact source title together with `disordered K-exclusion plateau K=2 site disorder`, `site disorder K-exclusion flux plateau`, and `partial exclusion asymmetric random environment`. It again recovered, among the closest relevant literature:

1. Allan Sly, *Note on the flux for TASEP with general disorder*, `https://arxiv.org/abs/1609.06589`, proving the plateau for ordinary iid site-disordered `K=1` TASEP;
2. Christophe Bahadoran and Thierry Bodineau, *Quantitative estimates for the flux of TASEP with dilute site disorder*, `https://arxiv.org/abs/1602.06718`, again ordinary `K=1` TASEP;
3. Simone Floreani, Frank Redig, Federico Sau, *Hydrodynamics for the partial exclusion process in random environment*, `https://arxiv.org/abs/1911.12564`, whose random environment is random maximal site occupancy rather than the source's iid site jump rates;
4. Patrícia Gonçalves, Kohei Hayashi, Makiko Sasada, *Characterization of Gradient Condition for Asymmetric Partial Exclusion Processes and Their Scaling Limits*, `https://arxiv.org/abs/2405.15142`, treating a different product-rate/gradient partial-exclusion class;
5. Arvind Ayyer and Samarth Misra, *An exactly solvable asymmetric K-exclusion process*, `https://arxiv.org/abs/2310.03343`, a different `(q,t)`-deformed finite-ring model.

No theorem closing the exact iid site-rate finite-capacity `K>=2` residual surfaced. The honest status remains **OPEN_BY_BOUNDED_SEARCH**, not a worldwide-openness or novelty certificate.

The frozen test case and stable source-relevant quantity remain

\[
K=2,\qquad Q=\frac12\delta_{1/2}+\frac12\delta_1,
\]

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\},
\]

with tracked metric a rigorous lower bound `L <= Delta_2(Q)`.

### Runtime capability honesty

The exposed task surface still supplies prompt/title, schedule/timing and enabled-state controls, but **no binding model selector, no reasoning-effort selector, no authenticated reasoning telemetry and no guaranteed run-duration field**. GPT-6/maximum is therefore text-requested only. This invocation identifies as GPT-5.6 Sol; reasoning effort is unavailable and is recorded as `UNVERIFIED`.

Making GPT-6/maximum binding would require a platform scheduler/API surface that exposes model and reasoning-effort fields and authenticates the runtime selection. A repository edit cannot create that capability. The historical P26 `You cannot modify this task` response is an authorization/context restriction; the compliant workaround is modification from the owning/authorized account or workspace, or platform support/ownership remediation, never a permission bypass or duplicate schedule. No schedule was created, modified, reactivated, or disabled in this run.

## 2. Carry-in, idea-before-code, and metric movement

The preceding checkpoint certified, at

\[
\theta=\frac{57343}{100000},
\tag{2.1}
\]

\[
G_1(0)\le A_{\rm old}:=\frac{58398337}{20000000}=2.91991685,
\tag{2.2}
\]

and hence by the already established D0025 transfer

\[
\Delta_2(Q)\ge \frac1{4G_1(0)}
\tag{2.3}
\]

the certified half-width

\[
L_{\rm old}=\frac{5000000}{58398337}
=0.085618876441636\ldots.
\tag{2.4}
\]

That run completed all obvious **one-positive-gap / one-zero-gap** structural local-minimum strata. It explicitly left strict two-gap chambers as the next loss.

Before writing any new checker, this run committed the route to

`artifacts/hard7_2026-09-18/HARD7-03/20260919T2123Z__idea-central-double-outrunner.md`

at commit

`68695f6416762afe65310db2642e2670c92665b8`,

and read it back successfully.

The previous run used B11/B14/B25. This run uses the distinct triple **B5/B19/B24**.

The new exact correction proves

\[
\boxed{G_1(0)\le A_{\rm new}:=\frac{291978907}{100000000}=2.91978907,}
\tag{2.5}
\]

so

\[
\boxed{
\Delta_2(Q)\ge L_{\rm new}
:=\frac{25000000}{291978907}
=0.085622623417794\ldots .}
\tag{2.6}
\]

Thus the stable metric moves rigorously

\[
\boxed{
L:\quad \frac{5000000}{58398337}
\longrightarrow
\frac{25000000}{291978907}}
\tag{2.7}
\]

with exact positive gain

\[
\boxed{
L_{\rm new}-L_{\rm old}
=\frac{63890000000}{17051082607877659}>0.}
\tag{2.8}
\]

This is a theorem only for the frozen `K=2` binary environment and remains **PARTIAL** for Seppäläinen's general Problem 4.

## 3. B19/B24 — the unique missing strict local-minimum sign chamber

Retain the layer-two variables

\[
\begin{aligned}
Y_{-2}&=A_{-1}+B_{-2},\\
Y_{-1}&=\max(A_{-1},A_0)+B_{-1},\\
Y_0&=\max(A_{-1},A_0,A_1)+B_0,\\
Y_1&=\max(A_0,A_1)+B_1,\\
Y_2&=A_1+B_2,
\end{aligned}
\tag{3.1}
\]

with independent unit exponentials, and sliding maxima

\[
S_e=\max\{Y_z:|z-e|\le1,\ -2\le z\le2\}.
\tag{3.2}
\]

At a fourth-step center `d`, the exact fresh-layer triple kernel is evaluated at

\[
u=S_{d-1}-S_d,\qquad v=S_{d+1}-S_d.
\tag{3.3}
\]

The earlier local-minimum baseline covers `u,v>=0` by the value

\[
\kappa=\Phi_\theta(0,0)
=\frac{\theta}{(2-\theta)(3-\theta)}.
\tag{3.4}
\]

The edge and near-edge windows are nested on one side. In particular, for `d=2`, `S_3<=S_2`, and for `d=1`, `S_2<=S_1`. Therefore a local minimum at either location can only have second gap exactly zero. Those positive/zero strata are precisely the structural events treated in the preceding two boundary checkpoints.

At the center put

\[
T=S_0=\max(Y_{-1},Y_0,Y_1).
\tag{3.5}
\]

Then

\[
S_{-1}>S_0
\iff Y_{-2}>T,
\qquad
S_1>S_0
\iff Y_2>T.
\tag{3.6}
\]

Hence the strict positive-positive chamber is exactly

\[
\boxed{
\mathcal E_{++}
=\{Y_{-2}>T,\ Y_2>T\}.}
\tag{3.7}
\]

There is no hidden subcase: this is the whole central `(+,+)` local-minimum sector.

The B19 finite exploration algorithm exhaustively enumerates all `5!=120` strict orderings of `(Y_{-2},\ldots,Y_2)`. It verifies the exact sign-pattern counts

\[
\begin{array}{c|c}
 d& \text{gap-sign counts among the 120 strict orders}\\ \hline
0&(++,12),(+-,6),(+0,12),(-+,6),(-0,24),(0+,12),(0-,24),(00,24),\\
1&(+-,10),(+0,20),(-0,30),(0-,30),(00,30),\\
2&(+-,20),(+0,20),(0-,40),(00,40).
\end{array}
\tag{3.8}
\]

In particular, `(+,+)` occurs **only** at `d=0`, in exactly 12 strict orderings. The same finite checker also verifies, ordering by ordering, the earlier positive/zero event identities at the edge, near edge, and center. Thus the new event is not a sampled favorable subset: it is the unique strict local-minimum sign chamber not already made exact by the baseline plus structural-boundary corrections.

**B24 outcome: successful.** The extremal obstruction was not another arbitrary two-gap cell; it was the unique center double-outrunner chamber (3.7).

**B19 outcome: successful.** Exhaustive strict-order exploration certifies the sign classification and prevents omission/double counting.

## 4. B5 — deform from the solved boundary to two positive overshoots

Recall the exact conditional kernel

\[
\Phi_\theta(u,v)
=\theta\int_0^\infty e^{\theta t}(1-e^{-t})
 e^{-(t-u)_+-(t-v)_+}\,dt.
\tag{4.1}
\]

It is coordinatewise increasing in `(u,v)`. Introduce the gap-strength deformation

\[
\lambda\mapsto \Phi_\theta(\lambda u,\lambda v),
\qquad 0\le\lambda\le1.
\tag{4.2}
\]

At `lambda=0` this is exactly the already solved local-minimum baseline `kappa`; at `lambda=1` it is the desired strict double-outrunner kernel. Thus the new chamber can be reached monotonically from the solved boundary, rather than attacked by an unrelated inequality.

The important additional simplification is memorylessness. Conditional on the first `A` layer and on

\[
T=t=\max(Y_{-1},Y_0,Y_1),
\]

we have

\[
t\ge Y_0\ge s_0:=\max(A_{-1},A_0,A_1)
\ge A_{-1},A_1.
\tag{4.3}
\]

The two outer variables `Y_{-2}=A_{-1}+B_{-2}` and `Y_2=A_1+B_2` use fresh independent exponentials. On `mathcal E_{++}`, therefore,

\[
E_L:=Y_{-2}-t,\qquad E_R:=Y_2-t
\]

are conditionally independent `Exp(1)` variables, independent of the inner variables after conditioning on the survival event.

For `E~Exp(1)` and `s>=0`,

\[
\mathbb E\,e^{-(s-E)_+}
=e^{-s}(1+s).
\tag{4.4}
\]

Consequently the exact average kernel excess on the two fresh overshoots factors into a universal scalar. Put

\[
b=2-\theta,\qquad c=3-\theta.
\tag{4.5}
\]

Then

\[
\begin{aligned}
\mathbb E\Phi_\theta(E_L,E_R)
&=\theta\int_0^\infty
 e^{-bt}(1-e^{-t})(1+t)^2\,dt\\
&=\theta\left[
\left(\frac1b+\frac2{b^2}+\frac2{b^3}\right)
-
\left(\frac1c+\frac2{c^2}+\frac2{c^3}\right)
\right].
\end{aligned}
\tag{4.6}
\]

Since

\[
\kappa=\frac{\theta}{bc}
=\theta\left(\frac1b-\frac1c\right),
\]

the exact expected bonus is

\[
\boxed{
D(\theta)
=2\theta\left[
\left(\frac1{b^2}-\frac1{c^2}\right)
+
\left(\frac1{b^3}-\frac1{c^3}\right)
\right]>0.}
\tag{4.7}
\]

**B5 outcome: successful.** The two-gap chamber is a monotone deformation of the solved zero-gap point, and memorylessness evaluates the endpoint `lambda=1` exactly.

## 5. Exact integration over the inner maximum

The triple slack contains the factor `e^{theta T}`. Conditional on `T=t` and the first layer, the probability that both outer variables exceed `t` is

\[
\exp(A_{-1}-t)\exp(A_1-t).
\tag{5.1}
\]

Hence the entire new correction is

\[
\boxed{
C_{++}(\theta)=D(\theta)\,T_{++}(\theta),}
\tag{5.2}
\]

where

\[
T_{++}(\theta)
=\mathbb E\exp\{A_{-1}+A_1-(2-\theta)T\}.
\tag{5.3}
\]

Condition on the first layer and write

\[
s_- =\max(A_{-1},A_0),\quad
s_0=\max(A_{-1},A_0,A_1),\quad
s_+=\max(A_0,A_1).
\tag{5.4}
\]

For `t>=s_0`, the density of

\[
T=\max(s_-+B_{-1},s_0+B_0,s_++B_1)
\]

has the exact inclusion-exclusion expansion

\[
f_T(t)=
\sum_{\varnothing\ne J\subset\{-,0,+\}}
(-1)^{|J|+1}|J|
\exp\left\{\sum_{j\in J}s_j-|J|t\right\}.
\tag{5.5}
\]

Therefore, with `b=2-theta`,

\[
T_{++}(\theta)\mid A
=
\sum_{\varnothing\ne J}
\frac{(-1)^{|J|+1}|J|}{b+|J|}
\exp\left\{
A_{-1}+A_1+\sum_{j\in J}s_j-(b+|J|)s_0
\right\}.
\tag{5.6}
\]

On each of the six strict order cones of `(A_{-1},A_0,A_1)`, every `s_j` is an order statistic. Writing the ordered exponentials as

\[
x_{\rm low}=z_1,\quad x_{\rm mid}=z_1+z_2,
\quad x_{\rm high}=z_1+z_2+z_3,
\tag{5.7}
\]

turns every monomial in (5.6) into a product of three reciprocal positive rational rates. Thus at rational `theta` the entire correction is exact rational arithmetic.

At (2.1), the checker obtains

\[
T_{++}=0.148196763999686\ldots,
\tag{5.8}
\]

\[
D(\theta)=0.683533035511113\ldots,
\tag{5.9}
\]

and therefore

\[
\boxed{C_{++}=0.101297383949629\ldots>0.}
\tag{5.10}
\]

The event is reflection-invariant and occurs only for the single central triple, so it is subtracted **once**, not doubled. Its gap-sign `(+,+)` is disjoint from every previously corrected strict mixed-sign or one-zero-gap branch.

This completes the exact accounting of the entire **local-minimum sign sector** of the four-step triple-slack calculation: `(0,0)` is the original exact baseline, edge/near/center one-positive-one-zero sectors were made exact by the preceding boundary checkpoints, and (3.7) is the only strict `(+,+)` sector.

This does **not** make the complete four-step triple kernel exact; non-local-minimum sign sectors remain.

## 6. Exact Chernoff certificate and moved plateau bound

The exact checker reconstructs the preceding structural-boundary carry-in

\[
U_{4,\rm carry}=810.354377298161353\ldots.
\tag{6.1}
\]

Since the triple subtraction enters divided by

\[
q=1-\theta,
\]

the new central correction lowers it by

\[
\frac{C_{++}}q
=0.237469545325807\ldots,
\tag{6.2}
\]

so

\[
\boxed{
U_{4,\rm new}=810.116907752835459\ldots.}
\tag{6.3}
\]

Keep the same rational Chernoff point (2.1) and choose

\[
A_{\rm new}=\frac{291978907}{100000000}=2.91978907.
\tag{6.4}
\]

Then

\[
x=4\theta A_{\rm new}
=\frac{16742946464101}{2500000000000}.
\tag{6.5}
\]

For `x>0`,

\[
S_{32}(x):=\sum_{k=0}^{32}\frac{x^k}{k!}<e^x.
\tag{6.6}
\]

The executed checker proves in exact rational arithmetic

\[
S_{32}(x)-U_{4,\rm new}>0,
\tag{6.7}
\]

with numerical margin

\[
S_{32}(x)-U_{4,\rm new}
=1.444373239057331\times10^{-5}\ldots.
\tag{6.8}
\]

Therefore

\[
U_{4,\rm new}<S_{32}(x)<e^{4\theta A_{\rm new}},
\]

and the inherited four-step block Chernoff lemma gives (2.5). The already established D0025 plateau transfer (2.3) then gives (2.6).

## 7. Exact artifacts and readback

Idea before code:

- `artifacts/hard7_2026-09-18/HARD7-03/20260919T2123Z__idea-central-double-outrunner.md`
- commit `68695f6416762afe65310db2642e2670c92665b8`
- read back successfully.

Exact checker:

- `artifacts/hard7_2026-09-18/HARD7-03/central_double_outrunner_20260919T2123Z.py`
- commit `2336438cfa1a4eed7bd2298756723f3b281a22ec`
- read back successfully.

Executed output:

- `artifacts/hard7_2026-09-18/HARD7-03/central_double_outrunner_20260919T2123Z.out`
- commit `d223905718274686ffc1e7a47f62ee4bf653d567`
- read back successfully.

The checker was independently executed in this run with Python `Fraction` arithmetic before upload. The archived output terminates

`ALL_EXACT_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit.

## 8. Remaining obligation and next route

The tracked quantity moved, so Section-I stuck rotation is **not** triggered.

The strict local-minimum sign sector of this four-step triple calculation is now exact, but the source problem is far from closed. The next obstruction should no longer be described as "find another local-minimum chamber." The finite sign table (3.8) shows the remaining geometry lies in the non-local-minimum sectors, notably `(-,0)`, `(0,-)`, and strict mixed-sign `(+,-)` / `(-,+)` cells. Earlier runs improved some mixed-sign branches, but they have not proved the entire non-local-minimum contribution exact.

The next run should not repeat B5/B19/B24. A useful next triple is **B6 / B17 / B27**:

- **B6:** deform a non-local-minimum chamber to the nearest now-exact boundary and track the first term that changes sign;
- **B17:** compare the resulting rational constants with the phase-type/exponential-spacing transforms already appearing in the exact mixed-sign work, looking for a reusable closed form;
- **B27:** swap the remaining pointwise lower-bound quantifier for exact integration over the full sign chamber before optimizing any coefficient.

The stable metric remains `L <= Delta_2(Q)`; finite-size particle simulations are not evidence for the source-level asymptotic statement.

## 9. Ledger delta for the authorized reconciler

```yaml
ledger_delta:
  track: HARD7-03
  canonical_claim: D0025
  source_key: disordered_asep_open_1999::problem_4
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  metric: "rigorous lower bound L <= Delta_2(Q) for K=2, Q=(delta_1/2+delta_1)/2"
  before: "5000000/58398337"
  after: "25000000/291978907"
  before_decimal: 0.085618876441636
  after_decimal: 0.085622623417794
  exact_gain: "63890000000/17051082607877659"
  methods: [B5, B19, B24]
  new_structural_result: "central (+,+) double-outrunner is the unique missing strict local-minimum chamber; full local-minimum sign sector of the four-step triple-slack calculation is now exact"
  checker: artifacts/hard7_2026-09-18/HARD7-03/central_double_outrunner_20260919T2123Z.py
  output: artifacts/hard7_2026-09-18/HARD7-03/central_double_outrunner_20260919T2123Z.out
  checker_commit: 2336438cfa1a4eed7bd2298756723f3b281a22ec
  output_commit: d223905718274686ffc1e7a47f62ee4bf653d567
  exact_check: ALL_EXACT_CHECKS_PASS
  closure: false
  audits: "not requested; source not closed"
  next_methods: [B6, B17, B27]
```

No shared-root file was edited. No email, Drive action, public post, peer-track file edit, schedule edit, duplicate schedule, or closure claim was made.