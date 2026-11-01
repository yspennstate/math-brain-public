Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 250000000/2932597567 -> 625000/7314597`. Methods tried: B6 / B23 / B28.**

# HARD7-03 — exact nested pair kernel sharpens the D0025 plateau certificate

Status: **PARTIAL**. Seppäläinen Problem 4 is not solved in full.

## 1. Continuity, ownership, repository state, and capability honesty

This execution resumes the existing exclusive claim

`operations/claims/D0025.md`, owner `HARD7-03`, key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`.

At run start I re-read `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the D0025 claim, the indexed intake/alias trail, and the newest complete own checkpoint `20260919T1418Z__d0025-common-overlap-pair-correction.md`. I also checked the newest visible neighbouring HARD7-02 and HARD7-04 commits. HARD7-02 remains on the Campbell--O'Rourke heavy-tailed elliptic-matrix question; HARD7-04 remains on the growing-random-graph/configuration-model line. No collision, release, posted equivalent, or ownership change involving D0025 was found. Shared root ledgers were not edited; this report supplies a `ledger_delta` only.

The large intake `problems.jsonl` files are not safely renderable byte-for-byte through one connector response, so I used the repository's indexed D0025 source/alias/claim trail rather than falsely claiming a literal full dump. The canonical claim remains unique to HARD7-03.

The exposed scheduler interface still has **no model selector and no reasoning-effort selector**, and supplies no authenticated reasoning telemetry or guaranteed execution duration. It exposes the ordinary task prompt/title/schedule/timing/enabled controls. GPT-6/maximum is therefore prompt-requested only. This execution identifies as GPT-5.6 Sol; the reasoning level is not exposed, so it is `UNVERIFIED`. Changing model/reasoning would require a platform/scheduler implementation or another authorized interface that actually exposes those controls. Historical `You cannot modify this task` failures are authorization/context restrictions; the repository records that P26 was later editable in another authorized context. The compliant workaround is the owning/authorized context or platform support, never a permission bypass or duplicate schedule. No schedule was created, disabled, or modified here.

## 2. Source and bounded current-literature refresh

Primary source remains:

Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1--15, Problem 4, arXiv `math/9906194`, DOI `10.11606/resimeusp.v4i1.74889`.

The admitted residual is the source's finite-capacity disordered asymmetric exclusion phase-transition/flat-flux question after excluding the now-known ordinary `K=1` iid site-disorder theorem. The frozen case is

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

with

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

A bounded current search on 2026-09-19 used the source title and the phrases `disordered asymmetric K-exclusion plateau K=2 site disorder`, `partial exclusion random environment site disorder flux plateau`, and `asymmetric K-exclusion disorder flux flat segment`. It again recovered, among the closest later works:

- Allan Sly, *Note on the flux for TASEP with general disorder*, arXiv `1609.06589`, the ordinary `K=1` iid-disorder plateau baseline;
- Simone Floreani, Frank Redig, Federico Sau, *Hydrodynamics for the partial exclusion process in random environment*, arXiv `1911.12564`, SPA 142 (2021), 124--158, DOI `10.1016/j.spa.2021.08.006`; its random environment is random **site capacity**, not the frozen iid site-rate model;
- Patrícia Gonçalves, Kohei Hayashi, Makiko Sasada, *Characterization of Gradient Condition for Asymmetric Partial Exclusion Processes and Their Scaling Limits*, arXiv `2405.15142`; it studies a product-rate/gradient partial-exclusion class, not the source's iid site-rate model;
- Arvind Ayyer, Samarth Misra, *An exactly solvable asymmetric K-exclusion process*, J. Phys. A 57 (2024), 315001, DOI `10.1088/1751-8121/ad5edd`; this is a different `(q,t)` integrable K-exclusion model.

No theorem closing the exact `K>=2` iid site-rate residual surfaced in this bounded search. The honest label remains **OPEN_BY_BOUNDED_SEARCH**, not an exhaustive worldwide-openness or novelty certificate.

## 3. Frozen metric and carry-in

The fixed source-relevant quantity is a rigorous lower bound

\[
L\le \Delta_2(Q).
\]

The preceding checkpoint proved

\[
G_1(0)\le \frac{2932597567}{10^9}=2.932597567
\]

for the homogeneous rate-one `K=2` lazy-LPP central shape and, through the already established D0025 transfer,

\[
\Delta_2(Q)\ge \frac1{4G_1(0)}.
\tag{3.1}
\]

Thus the carry-in value is

\[
L_{\rm old}=\frac{250000000}{2932597567}
=0.0852486555991199\ldots .
\tag{3.2}
\]

The preceding four-step argument had already replaced an arbitrary shared predecessor by the maximum over the full common predecessor window. The remaining visible loss was the decoupling

\[
\min(S+C,T+D)\ge R+\min(C,D),
\tag{3.3}
\]

where `R` is a common-window maximum. This run removes (3.3) **exactly for the two nested adjacent-pair classes**, while retaining the certified common-window estimate for the genuinely nonnested centre class.

## 4. Idea-before-code and method rotation

Before writing the checker I committed

`artifacts/hard7_2026-09-18/HARD7-03/20260919T1523Z__idea-exact-nested-pair-kernel.md`

at commit `fe3d9656bbdc190e0cacaf3860628388b5a3dd46` and read it back successfully.

The previous run used B24 / B19 / B5. This run uses a different triple:

- **B6 — deform to a point you can solve.** Deform from the common-window lower bound to the exact two-clock kernel on the nested window classes. **Outcome: successful.**
- **B23 — do what the proposer did not expect.** Assume the residual dependence discarded by (3.3) is quantitatively important rather than negligible. **Outcome: successful:** both nested pair classes have strictly positive exact gains.
- **B28 — replace “for all” with “for typical”.** Solve the exact order-cone/nested classes first, rather than forcing the nonnested centre pair into the same formula. **Outcome: successful:** edge and near-edge classes are exact; centre remains at the old rigorous lower bound.

All thirty labels have appeared somewhere in the long D0025 history, so these are disclosed reuses after exhaustion; the immediate triple is nevertheless new and the mathematical route differs from the preceding common-overlap argument.

## 5. Exact two-clock minimum kernel

Let `0<theta<1`, put

\[
q=1-\theta,
\]

and let `C,D` be independent unit exponentials. For deterministic `s\le t`, write `d=t-s`. Then

\[
\min(s+C,t+D)=s+\min(C,d+D).
\]

For `u\ge0`, independence gives

\[
\Pr\{\min(C,d+D)>u\}=
\begin{cases}
e^{-u},&0\le u<d,\\
e^{d-2u},&u\ge d.
\end{cases}
\tag{5.1}
\]

For any nonnegative random variable `Z`,

\[
\mathbb E e^{\theta Z}=1+\theta\int_0^\infty e^{\theta u}\Pr\{Z>u\}\,du.
\]

Using (5.1),

\[
\begin{aligned}
\mathbb E e^{\theta\min(C,d+D)}
&=1+\theta\int_0^d e^{-(1-\theta)u}\,du
+\theta e^d\int_d^\infty e^{-(2-\theta)u}\,du\\
&=\frac1q\left(1-\frac{\theta}{2-\theta}e^{-qd}\right).
\end{aligned}
\]

Hence the exact kernel is

\[
\boxed{
\mathbb E e^{\theta\min(s+C,t+D)}
=\frac{e^{\theta s}}q
\left(1-\frac{\theta}{2-\theta}e^{-q(t-s)}\right).}
\tag{5.2}
\]

Consequently, whenever random `S\le T` are measurable with respect to the preceding layers and independent of `C,D`,

\[
\boxed{
\mathbb E e^{\theta\min(S+C,T+D)}
=\frac1q\left[
\mathbb E e^{\theta S}
-\frac{\theta}{2-\theta}\mathbb E e^{S-qT}
\right].}
\tag{5.3}
\]

Equation (5.3) is exact; there is no discretization or simulation.

## 6. The two nested adjacent-pair classes

Retain the time-two variables from the preceding checkpoint:

\[
\begin{aligned}
Y_{-2}&=A_{-1}+B_{-2},\\
Y_{-1}&=\max(A_{-1},A_0)+B_{-1},\\
Y_0&=\max(A_{-1},A_0,A_1)+B_0,
\end{aligned}
\tag{6.1}
\]

with all first- and second-layer displayed clocks independent unit exponentials.

By reflection there are three classes of adjacent time-three windows. Two are nested:

### 6.1 Edge class

\[
S_{\rm e}=Y_{-2},\qquad
T_{\rm e}=\max(Y_{-2},Y_{-1}),
\tag{6.2}
\]

so `S_e<=T_e` pointwise. Direct conditioning on `A_{-1},A_0` and splitting according to which second-layer clock wins gives

\[
\boxed{
E_{\rm e}:=\mathbb E e^{S_{\rm e}-qT_{\rm e}}
=\frac{5\theta^2-14\theta+10}
{(2-\theta)^4(1-\theta)^2}.}
\tag{6.3}
\]

The checker verifies this exact expression at the certified rational `theta`.

### 6.2 Near-edge class

Set

\[
S_{\rm n}=\max(Y_{-2},Y_{-1}),\qquad
T_{\rm n}=\max(Y_{-2},Y_{-1},Y_0).
\tag{6.4}
\]

Again `S_n<=T_n` pointwise. Conditional on the first-layer variables define

\[
m=\max(A_{-1},A_0),\qquad
d=(A_0-A_{-1})_+,
\qquad D=(A_1-m)_+.
\tag{6.5}
\]

After subtracting the common shift `m`,

\[
S_{\rm n}=m+U,\qquad U=\max(E_2,E_1-d),
\]

for independent unit exponentials `E_1,E_2`. For `u\ge0`,

\[
\Pr(U\le u)=(1-e^{-u})(1-e^{-(u+d)}),
\]

hence

\[
\boxed{
f_{U\mid d}(u)=(1+e^{-d})e^{-u}-2e^{-d}e^{-2u}.}
\tag{6.6}
\]

Let `E` be the independent unit exponential entering the extra `Y_0` branch. Integrating first in `E` and then in `U`, split at `u=D`, yields

\[
\begin{aligned}
&\mathbb E\!\left[e^{U-q\max(U,D+E)}\mid d,D\right]\\
&=e^{-qD}
\left[(1+e^{-d})\left(
\frac{D}{2-\theta}+\frac1q-\frac{q}{(2-\theta)^2}
\right)-\frac{2e^{-d}}{2-\theta}\right]\\
&\qquad
+\frac{2q\,e^{-d-(2-\theta)D}}
{(2-\theta)(3-\theta)}.
\end{aligned}
\tag{6.7}
\]

This identity is still exact. To average over the first layer, order `(A_{-1},A_0,A_1)`. On each of the six strict order cones write

\[
A_{(1)}=u,\qquad A_{(2)}=u+v,\qquad A_{(3)}=u+v+w,
\qquad u,v,w\ge0.
\]

The iid exponential density becomes

\[
e^{-3u-2v-w}.
\]

On each cone, `d` is one of `0,v,w,v+w`, and `D` is either `0` or `w`; therefore every term in (6.7) is a scalar product of elementary Laplace integrals, with at most one factor `w`. Explicitly,

\[
\int_0^\infty\!\int_0^\infty\!\int_0^\infty
 e^{-a u-bv-cw}\,du\,dv\,dw=\frac1{abc},
\]

and

\[
\int_0^\infty\!\int_0^\infty\!\int_0^\infty
 w e^{-a u-bv-cw}\,du\,dv\,dw=\frac1{abc^2}.
\tag{6.8}
\]

The exact checker evaluates all six cones with `Fraction` arithmetic. At

\[
\theta=\frac{723}{1250},
\tag{6.9}
\]

it obtains

\[
\boxed{
E_{\rm e}
=\frac{13638049316406250000}{2769305968198051489}
=4.924717410434910\ldots,}
\tag{6.10}
\]

and

\[
\boxed{
E_{\rm n}
=\frac{2140239280096576690673828125000000}
{232498751696766970797950151209649}
=9.205379661082876\ldots .}
\tag{6.11}
\]

## 7. Exact gain over the common-window bound

Write

\[
J_{\rm e}=\mathbb E e^{\theta Y_{-2}}
=\frac1{(1-\theta)^2},
\]

and, from the preceding exact checkpoint,

\[
J_{\rm n}
=\mathbb E e^{\theta\max(Y_{-2},Y_{-1})}
=\frac{8-5\theta}{(2-\theta)^3(1-\theta)^2}.
\tag{7.1}
\]

By (5.3), the exact nested-pair moments are

\[
P_{\rm e}=\frac1q\left(J_{\rm e}
-\frac{\theta}{2-\theta}E_{\rm e}\right),
\qquad
P_{\rm n}=\frac1q\left(J_{\rm n}
-\frac{\theta}{2-\theta}E_{\rm n}\right).
\tag{7.2}
\]

The previous common-window bounds for these same classes were

\[
Q_{\rm e}=\frac{2}{2-\theta}J_{\rm e},
\qquad
Q_{\rm n}=\frac{2}{2-\theta}J_{\rm n}.
\tag{7.3}
\]

At (6.9), exact arithmetic certifies

\[
P_{\rm e}-Q_{\rm e}
=\frac{6319512826171875000}{9337868511362310239}>0,
\tag{7.4}
\]

and

\[
P_{\rm n}-Q_{\rm n}
=\frac{201076702055271621704101562500000}
{261322126353671667999973066856133}>0.
\tag{7.5}
\]

There are two reflected pairs of each class, and each adjacent pair appears in two fourth-step predecessor windows. Therefore the total pair-subtraction improvement is

\[
\boxed{
\Delta C
=4\big[(P_{\rm e}-Q_{\rm e})+(P_{\rm n}-Q_{\rm n})\big]
=\frac{1511718152574491621319132812500000}
{261322126353671667999973066856133}}
\tag{7.6}
\]

with

\[
\Delta C=5.784883866008889\ldots .
\]

The centre adjacent-pair class is **not** claimed exact here. Its previous common-window bound is retained unchanged. Hence (7.6) is a rigorous one-sided improvement, not an extrapolation from the nested cases.

## 8. Improved four-step Chernoff certificate

The preceding exact checkpoint archived

\[
U_4^{\cap}
=\frac{471848329119416840838853418325986387230949832280273437500000}
{533551258662847599879934006185557225047638076531060575909}.
\tag{8.1}
\]

Because the pair minima enter the four-step inclusion identity as subtractions and the outer denominator is `q=1-theta`, (7.6) gives

\[
U_4^{\rm nested}=U_4^{\cap}-\frac{\Delta C}{q}.
\tag{8.2}
\]

The exact result is

\[
\boxed{
U_4^{\rm nested}
=\frac{464527332753365031710169245072092857523367477290039062500000}
{533551258662847599879934006185557225047638076531060575909}}
\tag{8.3}
\]

or

\[
U_4^{\rm nested}=870.632999568839978\ldots .
\tag{8.4}
\]

Choose the rational shape target

\[
A=\frac{7314597}{2500000}=2.9258388.
\tag{8.5}
\]

Then

\[
x=4\theta A=\frac{5288453631}{781250000}.
\tag{8.6}
\]

Let

\[
S_{32}(x)=\sum_{k=0}^{32}\frac{x^k}{k!}.
\]

The checker proves exactly

\[
S_{32}(x)-U_4^{\rm nested}>0,
\tag{8.7}
\]

with decimal size

\[
1.000198938692282\times10^{-4}.
\]

Since every omitted exponential-series term is positive,

\[
U_4^{\rm nested}<S_{32}(x)<e^x=e^{4\theta A}.
\tag{8.8}
\]

The already proved four-layer block Chernoff lemma therefore gives, for every block count `m`,

\[
\Pr\{T_1(4m,0)\ge4mA\}
\le\left(U_4^{\rm nested}e^{-4\theta A}\right)^m,
\tag{8.9}
\]

with base strictly below one. Consequently

\[
\boxed{G_1(0)\le \frac{7314597}{2500000}=2.9258388.}
\tag{8.10}
\]

Using the existing D0025 transfer (3.1),

\[
\boxed{
\Delta_2(Q)\ge\frac1{4G_1(0)}
\ge\frac{625000}{7314597}
=0.0854455823061749\ldots .}
\tag{8.11}
\]

Thus the frozen source metric moves rigorously

\[
\boxed{
L:\ \frac{250000000}{2932597567}
\longrightarrow\frac{625000}{7314597}.}
\tag{8.12}
\]

The exact positive gain is

\[
\boxed{
\frac{625000}{7314597}
-\frac{250000000}{2932597567}
=\frac{4224229375000}{21450769365785499}>0,}
\tag{8.13}
\]

about `1.969267070549809e-4`. This is theorem-level movement for the frozen binary `K=2` model, not finite-size evidence. It remains **PARTIAL** for the full source problem.

## 9. Exact artifacts, execution, and readback

Idea-before-code artifact:

`artifacts/hard7_2026-09-18/HARD7-03/20260919T1523Z__idea-exact-nested-pair-kernel.md`

commit `fe3d9656bbdc190e0cacaf3860628388b5a3dd46`; read back successfully.

Exact checker:

`artifacts/hard7_2026-09-18/HARD7-03/exact_nested_pair_kernel_20260919T1523Z.py`

commit `10d7e4dd1967682e5ae8ba82679dbbfeb04e54bc`; read back successfully.

Executed exact output:

`artifacts/hard7_2026-09-18/HARD7-03/exact_nested_pair_kernel_20260919T1523Z.out`

commit `90edc027f75aa96f6337e3c5d6ed2d4a4149f119`; read back successfully. The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

The key rational inequalities were also re-executed in this run with independent `Fraction` arithmetic: both nested-pair gains are positive, `U4_nested<U4_common`, the truncated-exponential margin is positive, and `625000/7314597 > 250000000/2932597567`.

This is a **self-check**, not an independent closure audit.

## 10. Honest status and next mathematical obligation

**Status: PARTIAL / source OPEN_BY_BOUNDED_SEARCH.** No closure, paper package, or audit request is triggered.

The metric moved, so the Section-I unchanged-run counter resets to zero. The dominant local loss in the current four-step calculation is now the **nonnested centre adjacent pair**. For that class the two predecessor maxima have a large common window plus one exclusive side each, so `S<=T` fails globally and (5.3) cannot be applied without conditioning on which exclusive side wins.

The next run should attack that object directly rather than optimize the current rational parameter again. Suggested next triple: **B1 / B11 / B15** — change category from pair minima to a joint-CDF/Laplace kernel, dualize the minimum through the joint survival function, and break the left/right symmetry by conditioning on the winning exclusive side. If that exact centre kernel is tractable on the same six first-layer order cones, it can replace the last common-window pair bound without changing the already certified triple-slack terms.

```yaml
ledger_delta:
  track: HARD7-03
  canonical_claim: D0025
  source_key: disordered_asep_open_1999::problem_4
  status: PARTIAL
  metric: "rigorous lower bound L <= Delta_2(Q) for K=2, Q=(delta_1/2+delta_1)/2"
  before: "250000000/2932597567"
  after: "625000/7314597"
  shape_upper_before: "2932597567/1000000000"
  shape_upper_after: "7314597/2500000"
  methods: [6, 23, 28]
  exact_checker: "artifacts/hard7_2026-09-18/HARD7-03/exact_nested_pair_kernel_20260919T1523Z.py"
  exact_output: "artifacts/hard7_2026-09-18/HARD7-03/exact_nested_pair_kernel_20260919T1523Z.out"
  exact_output_status: "ALL_EXACT_CHECKS_PASS = True"
  section_I_state: "metric moved; unchanged streak reset to 0"
  next_methods: [1, 11, 15]
```