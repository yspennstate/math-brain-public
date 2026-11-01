Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 2500000/29645831 -> 250000000/2932597567`. Methods tried: B24 / B19 / B5.**

# HARD7-03 — common-overlap pair correction gives a substantially sharper D0025 plateau certificate

Status: **PARTIAL**. Seppäläinen Problem 4 is not solved in full.

## 1. Continuity, ownership, required repository state, and capability honesty

This execution resumes the existing exclusive canonical claim

`operations/claims/D0025.md`, owner `HARD7-03`, key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`.

I re-read the controlling files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the active D0025 claim and indexed D0025/intake trail; the latest complete own checkpoint `20260919T1318Z__d0025-exact-interior-mixed-max.md`; and the newest complete neighboring HARD7-02 and HARD7-04 reports available at run start. HARD7-02 is on Campbell--O'Rourke heavy-tailed elliptic matrices, while HARD7-04 is on van der Hofstad configuration-model duality. No canonical collision, release, posted equivalent, or peer ownership change involving D0025 was found. Shared root ledgers were not modified.

The large `probability_1000_intake_*/problems.jsonl` collection is not safely renderable byte-for-byte in one connector response. I therefore used the repository's indexed source/alias/claim search for D0025 and neighboring particle-system aliases instead of falsely claiming a literal full-file dump. The canonical claim remains unique to HARD7-03.

The exposed scheduler/runtime interface still has **no model selector and no reasoning-effort selector** and supplies no authenticated reasoning telemetry or guaranteed execution duration. It exposes task identity/title/prompt, schedule/timing, enabled state, and ordinary task-update fields. GPT-6/maximum therefore remains prompt-requested only. This runtime identifies as GPT-5.6 Sol and exposes no reasoning level, hence `UNVERIFIED`. Changing this requires a platform/scheduler implementation or another authorized interface that actually exposes model/reasoning controls; a repository edit cannot do it. Historical `You cannot modify this task` errors are authorization/context restrictions. The repository now records that P26 was subsequently editable from another authorized context; the compliant workaround is the owning/authorized context or platform support, never a permission bypass or duplicate schedule. I did not probe, create, disable, or modify any schedule in this run.

## 2. Primary source and bounded current-literature refresh

The primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1--15, Problem 4, DOI `10.11606/resimeusp.v4i1.74889`, arXiv `math/9906194`.

Source page:

`https://revistas.usp.br/resenhasimeusp/pt_BR/article/view/74889`

ArXiv:

`https://arxiv.org/abs/math/9906194`

The admitted residual is the source's phase-transition / flat-flux question for disordered asymmetric finite-capacity `K`-exclusion after excluding the now-known ordinary `K=1` iid site-disorder theorem. The frozen first case remains

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

and

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

A fresh bounded search on 2026-09-19 used the exact source title and the queries `disordered asymmetric K-exclusion K=2 flux plateau` and `partial exclusion disorder random environment asymmetric K exclusion flux`. It recovered, in particular:

- Allan Sly, *Note on the flux for TASEP with general disorder*, arXiv `1609.06589`, proving the iid-disorder plateau for ordinary `K=1` TASEP;
- Floreani--Redig--Sau, *Hydrodynamics for the partial exclusion process in random environment*, arXiv `1911.12564` / SPA 142 (2021), where the random environment is random site capacity and the mechanism/model is different from the present iid site-rate problem;
- Gonçalves--Hayashi--Sasada, *Characterization of Gradient Condition for Asymmetric Partial Exclusion Processes and Their Scaling Limits*, arXiv `2405.15142`, treating a product-rate/gradient partial-exclusion class, again not the source's iid site-rate finite-capacity model.

No theorem closing the exact `K>=2` iid site-rate residual surfaced in this bounded search. This is **OPEN_BY_BOUNDED_SEARCH**, not an exhaustive worldwide-openness or novelty certificate.

## 3. Stable metric and carry-in

The stable quantity remains a rigorous lower bound

\[
L\le\Delta_2(Q).
\]

The preceding checkpoint proved

\[
G_1(0)\le \frac{29645831}{10000000}=2.9645831
\]

for the rate-one homogeneous `K=2` lazy-LPP central shape constant and, through the already proved D0025 transfer,

\[
\Delta_2(Q)\ge\frac1{4G_1(0)}.
\tag{3.1}
\]

Thus the carry-in metric is

\[
L_{\rm old}=\frac{2500000}{29645831}
=0.084328889279575\ldots .
\tag{3.2}
\]

The preceding four-step certificate had already integrated the exact nonnegative triple-slack corrections. The largest obvious remaining loss in the same four-step identity was more primitive: every adjacent pair-minimum was still bounded through **one chosen common predecessor**, even when the two predecessor windows share two sites.

## 4. Idea-before-code and method rotation

Before writing the new checker I committed

`artifacts/hard7_2026-09-18/HARD7-03/20260919T1418Z__idea-common-overlap-pair-correction.md`

at commit `c7ec1f3b13646a914f2491a98dd16e48e52b6641` and read it back successfully.

The preceding run used B15 / B25 / B3. This run deliberately changes the route.

- **B24 — find the extremal object.** Replace the arbitrarily selected common predecessor by the maximum over the full intersection of the two predecessor windows. Outcome: successful and structurally much stronger.
- **B19 — make it an algorithm.** Build an exact order-cone evaluator for the exponential moment of the maximum over an arbitrary selected time-two window. Outcome: successful; it reproduces three closed forms exactly.
- **B5 — add a parameter and vary it.** Re-optimize only the Chernoff parameter after the structural pair correction, using floating exploration only to nominate a rational point and exact arithmetic for the proof. Outcome: successful.

All thirty method labels have appeared somewhere in the long D0025 history; these are disclosed reuses after exhaustion, but the triple is different from the immediately preceding run and the mathematical roles are new.

## 5. B24: the maximal common predecessor is the correct pair object

Let `Y_j` be the time-two passage values entering the time-three layer, and write

\[
S_e=\max_{j\in W_e}Y_j,
\qquad
T_3(e)=S_e+C_e,
\tag{5.1}
\]

where `W_e` is the time-two predecessor window of the time-three endpoint `e` and the `C_e` are iid `Exp(1)`, independent of the preceding layers.

For adjacent endpoints `e,e+1`, define the full common-window maximum

\[
R_e=\max_{j\in W_e\cap W_{e+1}}Y_j.
\tag{5.2}
\]

Since `R_e<=S_e` and `R_e<=S_{e+1}`, pointwise

\[
\begin{aligned}
\min(T_3(e),T_3(e+1))
&=\min(S_e+C_e,S_{e+1}+C_{e+1})\\
&\ge R_e+\min(C_e,C_{e+1}).
\end{aligned}
\tag{5.3}
\]

Because `min(C_e,C_{e+1})~Exp(2)` and is independent of `R_e`, for `0<theta<1`,

\[
\boxed{
\mathbb E e^{\theta\min(T_3(e),T_3(e+1))}
\ge \frac{2}{2-\theta}\,\mathbb E e^{\theta R_e}.}
\tag{5.4}
\]

This dominates the old bound obtained by replacing `R_e` with any single shared predecessor `Y_z`. It is strictly stronger whenever the common window has two genuinely competing sites.

The time-two variables are

\[
\begin{aligned}
Y_{-2}&=A_{-1}+B_{-2},\\
Y_{-1}&=\max(A_{-1},A_0)+B_{-1},\\
Y_0&=\max(A_{-1},A_0,A_1)+B_0,\\
Y_1&=\max(A_0,A_1)+B_1,\\
Y_2&=A_1+B_2,
\end{aligned}
\tag{5.5}
\]

with all displayed `B` variables iid unit exponentials and independent of the first-layer `A` variables.

The six adjacent time-three pairs have intersections

\[
\{-2\},\quad\{-2,-1\},\quad\{-1,0\},\quad
\{0,1\},\quad\{1,2\},\quad\{2\}.
\tag{5.6}
\]

Reflection leaves three moment types:

\[
J_{\rm edge}=\mathbb E e^{\theta Y_{-2}},
\quad
J_{\rm out}=\mathbb E e^{\theta\max(Y_{-2},Y_{-1})},
\quad
J_{\rm in}=\mathbb E e^{\theta\max(Y_{-1},Y_0)}.
\tag{5.7}
\]

Each adjacent pair appears in exactly two fourth-step predecessor windows. Combining this multiplicity, reflection, and (5.4), the old pair correction can be replaced by

\[
\boxed{
C_{\cap}(\theta)
=\frac{8}{2-\theta}
\bigl(J_{\rm edge}+J_{\rm out}+J_{\rm in}\bigr).}
\tag{5.8}
\]

This replacement does **not** double count the triple correction. For nonnegative `x,y,z`, the deterministic identity used throughout the four-step chain is

\[
x+y+z-\min(x,y)-\min(y,z)-\max(x,y,z)
=(\min(x,z)-y)_+.
\tag{5.9}
\]

Thus the true adjacent-pair minima and the nonnegative triple slack in (5.9) are separate additive subtractions. The preceding `H_new` is a lower bound on the latter; (5.8) only strengthens the former.

## 6. B19: exact common-window exponential moments

For deterministic shifts `s_1,...,s_m`, iid `E_i~Exp(1)`, and `M=max_i(s_i+E_i)`, put `s_*=max_i s_i`. Integration of the tail distribution gives, for `0<theta<1`,

\[
\begin{aligned}
\mathbb E[e^{\theta M}\mid s]
&=e^{\theta s_*}
+\theta\int_{s_*}^{\infty}e^{\theta y}
\left[1-\prod_i(1-e^{s_i-y})\right]dy\\
&=e^{\theta s_*}
+\theta\sum_{\varnothing\ne S\subseteq[m]}
(-1)^{|S|+1}
\frac{e^{\sum_{i\in S}s_i-(|S|-\theta)s_*}}
{|S|-\theta}.
\end{aligned}
\tag{6.1}
\]

This is an exact identity, not a sampling approximation.

On each strict order cone

\[
0\le x_1\le x_2\le x_3
\]

for the three first-layer unit exponentials, every shift appearing in (5.5) is one of the order statistics. If a term in (6.1) becomes `exp(c_1 x_1+c_2 x_2+c_3 x_3)`, then its exact cone integral against the iid exponential density is

\[
I(c_1,c_2,c_3)
=\frac1{(3-c_1-c_2-c_3)(2-c_2-c_3)(1-c_3)}.
\tag{6.2}
\]

Equation (6.2) follows by the spacing substitution

\[
x_1=z_1,\quad x_2=z_1+z_2,\quad x_3=z_1+z_2+z_3
\]

and three independent one-dimensional exponential integrals. Summing (6.1)--(6.2) over the six orders of `(A_{-1},A_0,A_1)` gives

\[
\boxed{J_{\rm edge}=\frac1{(1-\theta)^2},}
\tag{6.3}
\]

\[
\boxed{J_{\rm out}=\frac{8-5\theta}{(2-\theta)^3(1-\theta)^2},}
\tag{6.4}
\]

and

\[
\boxed{J_{\rm in}=\frac{2(12-7\theta)}{(3-\theta)(2-\theta)^3(1-\theta)^2}.}
\tag{6.5}
\]

The checker performs exactly this six-cone inclusion-exclusion sum and verifies (6.3)--(6.5) at the certified rational parameter. It also verifies the strict improvements

\[
J_{\rm out}>M_2(1;\theta),
\qquad
J_{\rm in}>M_2(0;\theta),
\tag{6.6}
\]

while `J_edge=M_2(2;theta)`, so the structural gain occurs exactly on the four interior adjacent pairs.

## 7. B5 and the exact new Chernoff certificate

After changing the pair correction, the old Chernoff parameter is no longer near-optimal. A numerical one-parameter scan was used **only** to nominate a rational test point. The proof uses

\[
\theta=\frac{723}{1250}=0.5784
\tag{7.1}
\]

and exact rational arithmetic throughout.

At this parameter the checker gives

\[
J_{\rm edge}\approx5.625987923479363,
\quad
J_{\rm out}\approx10.002704516767647,
\quad
J_{\rm in}\approx12.859580946132890.
\tag{7.2}
\]

The old and new pair corrections are

\[
C_{\rm old}\approx131.381581747696600,
\qquad
C_{\cap}\approx160.316676344287572,
\tag{7.3}
\]

so the exact positive pair-correction gain is

\[
C_{\cap}-C_{\rm old}
=\frac{80851301328125000000000}{2794229721911833952401}
\approx28.935094596590972.
\tag{7.4}
\]

Re-evaluating, at the same `theta`, the already proved exact edge/near-edge/center triple-slack formulas from the preceding checkpoint gives

\[
H_{\rm new}\approx6.191052190489332.
\tag{7.5}
\]

Therefore the four-step exponential-moment sum satisfies

\[
A_4^{\rm actual}(\theta)
\le U_4^{\cap}(\theta)
:=\frac{3A_3(\theta)-C_{\cap}(\theta)-H_{\rm new}(\theta)}{1-\theta},
\tag{7.6}
\]

with the exact rational value archived by the checker and

\[
U_4^{\cap}(\theta)
\approx884.354261110606785.
\tag{7.7}
\]

Now choose

\[
A=\frac{2932597567}{10^9}=2.932597567.
\tag{7.8}
\]

Then

\[
x=4\theta A
=\frac{2120268040941}{312500000000}.
\tag{7.9}
\]

Since every term is positive,

\[
S_{32}(x)=\sum_{k=0}^{32}\frac{x^k}{k!}<e^x.
\]

The exact checker proves

\[
S_{32}(x)-U_4^{\cap}(\theta)>0,
\tag{7.10}
\]

with decimal size

\[
6.972328116292554\times10^{-7}.
\]

Hence

\[
U_4^{\cap}(\theta)<S_{32}(x)<e^{4\theta A}.
\tag{7.11}
\]

The inherited four-step block Chernoff lemma now applies: concatenate independent four-layer blocks, sum over the possible coarse endpoints in each block, and use Markov's inequality. For every block count `m`,

\[
\Pr\{T_1(4m,0)\ge4mA\}
\le\left(U_4^{\cap}(\theta)e^{-4\theta A}\right)^m,
\tag{7.12}
\]

whose base is strictly below one by (7.11). Therefore the homogeneous central shape satisfies

\[
\boxed{G_1(0)\le\frac{2932597567}{10^9}=2.932597567.}
\tag{7.13}
\]

This improves the previous certified shape upper bound by the exact amount

\[
\frac{29645831}{10^7}-\frac{2932597567}{10^9}
=\frac{31985533}{10^9}.
\tag{7.14}
\]

Applying the already established D0025 transfer (3.1),

\[
\boxed{
\Delta_2(Q)\ge
\frac1{4G_1(0)}
\ge\frac{250000000}{2932597567}
=0.0852486555991199\ldots .}
\tag{7.15}
\]

Thus the stable metric moves rigorously

\[
\boxed{
L:\ \frac{2500000}{29645831}
\longrightarrow
\frac{250000000}{2932597567}.}
\tag{7.16}
\]

The exact gain is

\[
\boxed{
\frac{250000000}{2932597567}-\frac{2500000}{29645831}
=\frac{79963832500000}{86939291862293177}>0,}
\tag{7.17}
\]

numerically about `9.197663195446553e-4`. This is a theorem-level improvement for the frozen binary `K=2` case, not a finite-size simulation. It remains **PARTIAL** for the source's full general-capacity problem.

## 8. Exact artifacts, execution, and readback

Idea-before-code artifact:

`artifacts/hard7_2026-09-18/HARD7-03/20260919T1418Z__idea-common-overlap-pair-correction.md`

creation commit `c7ec1f3b13646a914f2491a98dd16e48e52b6641`; read back successfully.

Exact checker:

`artifacts/hard7_2026-09-18/HARD7-03/common_overlap_pair_correction_20260919T1418Z.py`

creation commit `e6055b2ab8e05db65cf622a733876085d32808fc`; read back successfully.

Executed output:

`artifacts/hard7_2026-09-18/HARD7-03/common_overlap_pair_correction_20260919T1418Z.out`

creation commit `1754250ef4bd96ba6c47136b812bfd941a6db11d`; read back successfully. The output ends

`ALL_EXACT_CHECKS_PASS = True`.

This is a self-check, not an independent closure audit.

## 9. Honest status and next mathematical obligation

**Status: PARTIAL / source OPEN_BY_BOUNDED_SEARCH.** No closure, paper package, or audit request is triggered.

The frozen metric moved substantially, so the Section-I unchanged-run counter resets to zero. The strongest immediate lesson is that the previous four-step argument was losing much more in its pair-minimum surrogate than in the later mixed-sign refinements. The next run should therefore avoid another tiny coefficient polish and ask whether the **exact pair minimum**

\[
\mathbb E e^{\theta\min(S_e+C_e,S_{e+1}+C_{e+1})}
\]

can itself be integrated on the same six first-layer order cones, rather than lower-bounded by (5.3). That would remove the remaining `R_e+min(C_e,C_{e+1})` decoupling loss while preserving the exact triple slack.

Next route-finding triple: **B6 / B23 / B28** — deform from the common-window lower bound to the exact pair kernel; assume the residual pair dependence matters rather than vanishes; and first prove an exact typical/order-cone formula before attempting a global symbolic simplification.

```yaml
ledger_delta:
  track: HARD7-03
  canonical_claim: D0025
  source_key: disordered_asep_open_1999::problem_4
  status: PARTIAL
  metric: "rigorous lower bound L <= Delta_2(Q) for K=2, Q=(delta_1/2+delta_1)/2"
  before: "2500000/29645831"
  after: "250000000/2932597567"
  shape_upper_before: "29645831/10000000"
  shape_upper_after: "2932597567/1000000000"
  methods: [24, 19, 5]
  exact_checker: "artifacts/hard7_2026-09-18/HARD7-03/common_overlap_pair_correction_20260919T1418Z.py"
  exact_output: "artifacts/hard7_2026-09-18/HARD7-03/common_overlap_pair_correction_20260919T1418Z.out"
  exact_output_status: "ALL_EXACT_CHECKS_PASS = True"
  section_I_state: "metric moved; unchanged streak reset to 0"
  next_methods: [6, 23, 28]
```
