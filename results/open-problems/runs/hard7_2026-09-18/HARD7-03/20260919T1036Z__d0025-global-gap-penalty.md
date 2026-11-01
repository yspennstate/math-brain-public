Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 3125/37086 -> 25000/296511`. Methods tried: B7 / B9 / B17.**

# HARD7-03 — global negative-gap envelope recovers every four-step triple configuration

Status: **PARTIAL / Seppäläinen Problem 4 remains open as a whole.** This execution resumes the exclusive `D0025` claim and the latest local-minimum checkpoint. The new mathematical point is that the fresh-layer triple-slack kernel admits a global exponential penalty bound on *all* predecessor configurations. The previous hard local-minimum event is therefore unnecessary. Exact shifted-exponential order-statistic integration of the complement lowers the certified homogeneous `K=2` lazy-LPP central shape bound from `2.96688` to `2.96511`, and increases the frozen binary-disorder plateau half-width accordingly.

## 1. Continuity, required reads, ownership, and source status

Active canonical claim remains

`operations/claims/D0025.md`,

owner `HARD7-03`, canonical key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`. I resumed

`runs/hard7_2026-09-18/HARD7-03/20260919T0920Z__d0025-local-minimum-slack.md`

rather than restarting admission.

At run start I re-read/recovered the controlling files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the active D0025 claim; the newest visible HARD7-02 state (`2026-09-19T09-12-00Z__axis-cstar-logarithmic-mean.md`); and the newest visible HARD7-04 state (`2026-09-19T0938Z__vdh_sharp_hub_stripping.md`). Those neighboring tracks are on distinct non-Hermitian-matrix and growing-random-graph questions. Repository-wide D0025/canonical-name search still returns HARD7-03 as the owner and no release or competing equivalent claim.

Primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), Problem 4, Section 4; arXiv `math/9906194`; DOI `10.11606/resimeusp.v4i1.74889`. The source asks whether the disordered totally asymmetric `K`-exclusion system exhibits a phase transition analogous to disordered zero range, in particular a flat macroscopic-flux segment around density `K/2`.

Fresh bounded status queries on 2026-09-19 included the exact source title and the combinations `disordered K-exclusion plateau site disorder`, `general K TASEP site disorder plateau`, and `partial exclusion disorder flux K site rates`. They recovered:

- source: `https://arxiv.org/abs/math/9906194`;
- Allan Sly, *Note on the flux for TASEP with general disorder*, `https://arxiv.org/abs/1609.06589`, proving the iid site-disorder plateau for ordinary `K=1` TASEP;
- Gonçalves--Hayashi--Sasada, *Characterization of Gradient Condition for Asymmetric Partial Exclusion Processes and Their Scaling Limits*, `https://arxiv.org/abs/2405.15142`, whose product-rate/gradient partial-exclusion setting is not the source's iid site-rate general-`K` model;
- current 2026 searches also surfaced work on ordinary/open TASEP and general interacting-system hydrodynamics, but no theorem closing the exact `K>=2` iid site-rate residual.

This is a bounded negative search only. It does **not** certify worldwide openness or novelty.

The frozen test case is unchanged:

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

The tracked quantity remains a rigorous lower bound `L <= Delta_2(Q)`.

## 2. Before/after movement

The preceding checkpoint proved

\[
G_1(0)\le \frac{18543}{6250}=2.96688,
\qquad
L\ge \frac{3125}{37086}
=0.0842636035161516\ldots .
\tag{2.1}
\]

This run proves

\[
\boxed{G_1(0)\le \frac{296511}{100000}=2.96511}
\tag{2.2}
\]

and hence, by the already proved slow-rate cusp/plateau transfer in this checkpoint chain,

\[
\boxed{
\Delta_2(Q)\ge \frac1{4G_1(0)}
\ge \frac{25000}{296511}
=0.0843139040372869\ldots .}
\tag{2.3}
\]

Thus the frozen metric moves

\[
\boxed{
L:\ \frac{3125}{37086}\longrightarrow\frac{25000}{296511}}
\]

with exact positive gain

\[
\frac{25000}{296511}-\frac{3125}{37086}
=\frac{184375}{3665468982}>0.
\tag{2.4}
\]

The unchanged-run count remains zero.

## 3. Idea-before-code record

Before archiving a checker, I recorded the new route in

`artifacts/hard7_2026-09-18/HARD7-03/20260919T1028Z__idea-global-gap-penalty.md`

at commit `2ce062902217fedead5e4aba355c3e4872e4985d`, and read it back at that commit.

The preceding report had reached the exact conditional fresh-layer slack

\[
\Phi_\theta(u,v)
=\theta\int_0^\infty e^{\theta t}(1-e^{-t})
 e^{-(t-u)_+-(t-v)_+}\,dt,
\tag{3.1}
\]

where

\[
u=S_{d-1}-S_d,\qquad v=S_{d+1}-S_d.
\]

It used only the quadrant `u,v>=0`, replacing `Phi` by its value at the origin. The new route attacks the discarded complement instead of adding another hard sufficient event.

## 4. B7 — take the predecessor-gap limit, then notice the limiting factor is exact

For every real `u` and `t>=0`,

\[
(t-u)_+\le t-u\quad\text{if }u<0,
\qquad
(t-u)_+\le t\quad\text{if }u\ge0.
\]

Equivalently,

\[
\boxed{
e^{-(t-u)_+}\ge e^{\min(u,0)}e^{-t}.}
\tag{4.1}
\]

Applying (4.1) to both coordinates in (3.1) gives, for every `u,v in R`,

\[
\begin{aligned}
\Phi_\theta(u,v)
&\ge e^{\min(u,0)+\min(v,0)}
\theta\int_0^\infty e^{-(2-\theta)t}(1-e^{-t})\,dt\\
&=\boxed{
\kappa(\theta)e^{\min(u,0)+\min(v,0)}},
\end{aligned}
\tag{4.2}
\]

where

\[
\kappa(\theta)=\frac{\theta}{(2-\theta)(3-\theta)}.
\tag{4.3}
\]

The limit experiment `u->-infinity` suggested the `e^u` penalty; (4.1) shows the factor is actually exact in each negative coordinate. If both `u<=0` and `v<=0`, equality holds in (4.2), so this is the sharp pointwise constant for this separable exponential envelope on the full `(u,v)` plane.

**B7 outcome: successful.** The hard local-minimum indicator is replaced by a quantitative global penalty.

## 5. Sliding-window geometry: only one penalty can be active

Define

\[
D_d=(S_d-S_{d-1})_+ +(S_d-S_{d+1})_+.
\tag{5.1}
\]

For the width-three sliding maxima here, the two positive terms cannot occur simultaneously. Indeed, if `S_d>S_{d-1}`, a maximizer of the middle window cannot lie in its overlap with the left window. It must be the single endpoint entering from the right. That endpoint also belongs to the right-neighbor window, so `S_{d+1}>=S_d`. Reflection gives the other implication. The same argument applies at the truncated edge.

Combining this with (4.2), the exact triple correction satisfies

\[
\boxed{
R_d(\theta)\ge
\kappa(\theta)\,\mathbb E[e^{\theta S_d-D_d}].}
\tag{5.2}
\]

On the preceding local-minimum event `E_d`, `D_d=0`, so (5.2) contains the entire old contribution. Outside `E_d`, it retains a strictly positive exponentially penalized contribution.

## 6. B9 — randomize the hard acceptance event

Let `Z~Exp(1)` be independent of the passage variables. Then

\[
e^{-D_d}=\Pr\{Z>D_d\mid D_d\}.
\tag{6.1}
\]

Thus the right side of (5.2) can be read as

\[
\kappa(\theta)
\mathbb E[e^{\theta S_d}\mathbf 1\{Z>D_d\}],
\tag{6.2}
\]

with expectation over the auxiliary clock as well. The old proof accepted a configuration only when `D_d=0`; the randomized soft test accepts every configuration with probability `e^{-D_d}`. No approximation is introduced by this representation.

For the present five fourth-step endpoints, the complement of the local-minimum event decomposes into the following one-sided excess events. With

\[
\begin{aligned}
Y_{-2}&=A_{-1}+B_{-2},\\
Y_{-1}&=\max(A_{-1},A_0)+B_{-1},\\
Y_0&=\max(A_{-1},A_0,A_1)+B_0,\\
Y_1&=\max(A_0,A_1)+B_1,\\
Y_2&=A_1+B_2,
\end{aligned}
\tag{6.3}
\]

define

\[
P_2=\mathbb E[e^{(\theta-1)Y_1+Y_2};Y_1>Y_2],
\tag{6.4}
\]

\[
P_{10}=\mathbb E[e^{(\theta-1)Y_0+\max(Y_1,Y_2)};
Y_0>\max(Y_1,Y_2)],
\tag{6.5}
\]

\[
P_{12}=\mathbb E[e^{(\theta-1)Y_2+\max(Y_{-1},Y_0,Y_1)};
Y_2>\max(Y_{-1},Y_0,Y_1)],
\tag{6.6}
\]

and

\[
P_{01}=\mathbb E[e^{(\theta-1)Y_1+\max(Y_{-2},Y_{-1},Y_0)};
Y_1>\max(Y_{-2},Y_{-1},Y_0)].
\tag{6.7}
\]

The edge has one complement branch, a near-edge has the two disjoint branches (6.5)--(6.6), and the center has (6.7) plus its reflection. Therefore, if `H_loc` denotes the exact local-minimum subtraction from the preceding run,

\[
\boxed{
H_{\rm full}=H_{\rm loc}+\kappa(\theta)
\left[2P_2+2(P_{10}+P_{12})+2P_{01}\right].}
\tag{6.8}
\]

**B9 outcome: successful.** The randomized acceptance viewpoint makes clear why the complement should be integrated rather than discarded and yields the complete decomposition (6.8).

## 7. B17 — shifted-exponential order statistics make the complement exact

Condition on the first-layer `A` variables. Every relevant layer-two variable has the form

\[
Y_j=u_j+B_j,
\qquad B_j\stackrel{\rm iid}{\sim}{\rm Exp}(1),
\tag{7.1}
\]

where each `u_j` is a maximum of a fixed subset of `(A_{-1},A_0,A_1)`.

For a target `T` and lower set `L`, put

\[
M=\max_{\ell\in L}Y_\ell,\qquad
P_\theta(T;L)=
\mathbb E[e^{(\theta-1)Y_T+M};Y_T>M\mid A].
\tag{7.2}
\]

Let `m_0=max_{ell in L}u_ell`. For `z>=m_0`, inclusion-exclusion for a maximum of shifted exponentials gives

\[
F_M(z)=\prod_{\ell\in L}(1-e^{-(z-u_\ell)})
=\sum_{S\subseteq L}(-1)^{|S|}e^{u_S-|S|z},
\tag{7.3}
\]

where `u_S=sum_{ell in S}u_ell`. Hence

\[
f_M(z)=
\sum_{\varnothing\ne S\subseteq L}
(-1)^{|S|+1}|S|e^{u_S-|S|z}.
\tag{7.4}
\]

The target tail transform is also explicit. Writing `r=2-theta`,

\[
g_T(z):=\mathbb E[e^{(\theta-1)Y_T};Y_T>z\mid A]
=
\begin{cases}
 e^{(\theta-1)u_T}/r,&z<u_T,\\
 e^{u_T-rz}/r,&z\ge u_T.
\end{cases}
\tag{7.5}
\]

Consequently

\[
P_\theta(T;L)=\int_{m_0}^\infty e^z g_T(z)f_M(z)\,dz.
\tag{7.6}
\]

Split once at `u_T`. On each of the six order cones for `(A_{-1},A_0,A_1)`, every base `u_j` is one of the ordered coordinates `x_1<=x_2<=x_3`. Every term in (7.6) is therefore either a pure exponential monomial or one monomial times a single gap `x_j-x_i`. With gap coordinates, the pure monomial integral is

\[
I(c_1,c_2,c_3)=
\frac1{(3-c_1-c_2-c_3)(2-c_2-c_3)(1-c_3)},
\tag{7.7}
\]

and a gap factor is obtained by multiplying `I` by the sum of reciprocals of the corresponding independent gap rates. Thus all four quantities in (6.4)--(6.7) are finite rational sums.

As an independent identity check, the edge transform can be integrated directly. Conditional on `A_0,A_1`, put `u=max(A_0,A_1)`, `v=A_1`, `delta=u-v>=0`. Then

\[
\mathbb E[e^{(\theta-1)B_1+B_2};B_2<B_1+\delta]
=\frac1{(2-\theta)^2}+\frac\delta{2-\theta}.
\tag{7.8}
\]

Integrating the two cases `A_1>=A_0` and `A_0>A_1` gives

\[
\boxed{
P_2(\theta)=
\frac1{(1-\theta)(2-\theta)^3}
+\frac2{(2-\theta)^4}.}
\tag{7.9}
\]

The generic six-cone routine and (7.9) agree exactly in the archived certificate.

**B17 outcome: successful.** Importing the shifted-exponential maximum algebra converts every soft-penalty complement into exact rational order-cone integrals; no path simulation is used.

## 8. Exact values and the improved four-step MGF bound

Take

\[
\theta=\frac{1173}{2000}=0.5865.
\tag{8.1}
\]

Exact arithmetic gives

\[
\begin{aligned}
P_2&=\frac{71696000000000000}{52821258399640907}
=1.357332297113304\ldots,\\
P_{10}&=1.708100355314288\ldots,\\
P_{12}&=0.8137669222032878\ldots,\\
P_{01}&=1.375381698558506\ldots .
\end{aligned}
\tag{8.2}
\]

The exact fractions for all four are archived. The preceding local-minimum contribution at this `theta` is

\[
H_{\rm loc}=4.293449334123280\ldots,
\]

while the newly recovered complement contributes

\[
H_{\rm comp}=1.806728976371238\ldots,
\]

so

\[
H_{\rm full}=6.100178310494519\ldots .
\tag{8.3}
\]

Retaining the already established exact three-step MGF sum `A_3(theta)` and adjacent-pair subtraction `C(theta)`, the max/min identity from the prior checkpoints gives

\[
A_4^{\rm actual}(\theta)
\le U_4(\theta)
:=\frac{3A_3(\theta)-C(\theta)-H_{\rm full}(\theta)}{1-\theta}.
\tag{8.4}
\]

The exact checker obtains

\[
U_4(1173/2000)=
\frac{528641888617692662110044655957924880824288000000000000}
{503670161267475236669342553433146254884714844176881}
=1049.579524995835754\ldots .
\tag{8.5}
\]

## 9. Exact Chernoff certificate

Choose

\[
a=\frac{296511}{100000}=2.96511,
\qquad
x=4\theta a=\frac{347807403}{50000000}.
\tag{9.1}
\]

Let

\[
S_{32}(x)=\sum_{k=0}^{32}\frac{x^k}{k!}.
\]

The executed exact-Fraction checker proves

\[
\boxed{S_{32}(x)-U_4(1173/2000)>0},
\tag{9.2}
\]

with decimal margin

\[
0.003305587646959706\ldots .
\]

The exact positive rational is archived in the output file. Since `x>0`, `S_32(x)<e^x`; hence

\[
U_4(\theta)e^{-4\theta a}<1.
\tag{9.3}
\]

The already proved four-layer block-concatenation/Chernoff lemma from this checkpoint chain says that (9.3) implies the homogeneous central shape bound `G_1(0)<=a`: concatenating independent four-layer slabs multiplies the exponential endpoint-sum bound, so the upper-tail probability decays geometrically in the number of slabs; the shape limit then gives the claimed inequality. Thus (2.2) follows, and the previously established cusp/plateau transfer gives (2.3).

This is a theorem-sized **partial result for the frozen `K=2` binary-disorder case**, not a solution of the source's full general-`K` question.

## 10. Exact artifacts and readback status

New artifacts are:

- idea before code: `artifacts/hard7_2026-09-18/HARD7-03/20260919T1028Z__idea-global-gap-penalty.md`, commit `2ce062902217fedead5e4aba355c3e4872e4985d`, read back successfully;
- exact checker: `artifacts/hard7_2026-09-18/HARD7-03/global_gap_penalty_20260919T1028Z.py`, commit `a7827262e5fbfe743c9fe327d7afb140fffcacc3`, read back successfully;
- executed exact output: `artifacts/hard7_2026-09-18/HARD7-03/global_gap_penalty_20260919T1028Z.out`, commit `5f4225e83bc199031ca7f7279d3f40bbf01526cf`, read back successfully.

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

The checker was executed with exact Python `Fraction` arithmetic in this run before its output was archived. The edge complement is checked both by the generic six-cone routine and the independently derived closed form (7.9). These are **self-checks**, not independent audits.

## 11. Why this is substantively different from the previous run

The previous run enlarged a hard event from endpoint domination to local-minimum predecessor geometry, but still assigned zero value to its complement. This run removes that binary acceptance step completely. The new inequality (4.2) is global in the two gap variables, and (6.8) exhausts all five fourth-step triple configurations through a soft one-sided gap penalty. The gain therefore comes from a new route, not from extra Taylor terms, a finer grid, or another certificate for the same bound.

The remaining loss is now clearer: (4.2) keeps only the separable exponential lower envelope of the exact `Phi_theta(u,v)`. On configurations with one positive and one negative gap, the positive gap can improve `Phi` beyond the envelope, and that gain is still discarded. A genuinely new next route would integrate the exact one-negative-gap formula rather than repeat the present soft envelope.

This run uses the previously unused HARD7-03 method numbers B7/B9/B17. Across the accumulated D0025 checkpoints, all thirty Section-B labels have now been exercised at least once; a later run cannot literally choose three never-before-used labels on this same target, so it must at minimum use a nonconsecutive triple for a genuinely new mathematical route rather than falsely label recycled work as untried.

## 12. Model/scheduler capability statement

The requested `GPT-6 / maximum` setting remains prompt text only. The exposed scheduler interface provides task title, prompt, schedule, timing mode and enablement; it exposes no model selector, no reasoning-effort selector and no guaranteed execution duration. This run actually identifies as **GPT-5.6 Sol**; reasoning telemetry is **UNVERIFIED**. Changing the binding model/reasoning setting would require the platform to expose corresponding scheduler fields or an authorized task/workspace interface that controls them; a repository edit cannot do it.

The policy file records historical native modification probes for P26/P01/P03 that returned `You cannot modify this task`. The current root ledger also records that a later authorized context successfully updated P26, so the historical P26 denial is not represented here as a universal permanent failure. For any task that currently returns that denial, the permitted workaround is to use the owning account/workspace's authorized interface or platform support; do not bypass ownership and do not create a duplicate schedule. HARD7-03 did not modify or probe other schedules in this run.

## 13. Ledger delta for the designated reconciler

```yaml
ledger_delta:
  track: HARD7-03
  canonical_target: D0025
  owner_claim: operations/claims/D0025.md
  source_status: OPEN_BY_BOUNDED_SEARCH
  status: PARTIAL
  frozen_quantity: "L <= Delta_2(Q)"
  before: "3125/37086"
  after: "25000/296511"
  exact_gain: "184375/3665468982"
  unchanged_run_count: 0
  methods: [B7, B9, B17]
  artifact_output_tail: "ALL_EXACT_CHECKS_PASS = True"
  closure_claimed: false
  independent_audits_added: 0
  shared_root_files_modified: false
```
