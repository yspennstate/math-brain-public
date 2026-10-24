Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **MOVEMENT:** `epsilon_bridge: 1/18,817,988 -> 1/14,469,504`; supported unchanged count `1 -> 0` (reset by movement). Methods actually tried: **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #14 FIND THE GROUP ACTING, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE**.

# R16 HARD OUTSIDE — I0036 / Schramm Problem 2.1: weighted logarithmic-scale pigeonhole and a stronger bridge exponent

Date: 2026-09-17 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`. Source-level status: **PARTIAL / OPEN**. This run proves a stronger explicit polynomial decay exponent for the critical hexagonal-lattice bridge partition function. It does **not** prove the SAW scaling limit or its identification with `SLE_{8/3}`. Publication novelty is **UNVERIFIED**.

## 1. Continuity, repository read, and ownership

I continued from

`runs/R16/2026-09-17T10-47-00Z_i0036-phase-transfer-dual-obstruction_2f7a.md`,

whose frozen metric was

\[
B_T\le 1000T^{-1/18,817,988}\qquad(T\ge1)
\]

and whose supported unchanged count was `1`. I preserved its phase-resolved transfer-operator route and finite obstruction; this run does not erase or restart that work.

Before new mathematics I recovered/read the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the active exclusive claim `operations/claims/I0036.md`, the newest R16 report and the preceding threshold-optimization report, the exact I0036 intake row in `probability_1000_intake_I_20260914/problems.jsonl`, the historical R09 I0036 source/admission screen, and current neighboring discrepancy state including the newest R13 Komlos report. Repository search found no competing I0036 owner and no I0036 P26 or second-OTHER end-to-end audit.

The connector cannot render all roughly 780 intake rows in one model-visible response. I therefore do not claim a literal bytewise reread of every JSONL row. The exact active source row, current claim, prior attempts, exclusions and neighboring ownership were recovered directly; missing corpus-wide information was not invented.

I0036 remains **R16 exclusive / ADMITTED_ACTIVE / HARD_OUTSIDE**.

## 2. Source and current-primary-literature refresh

The source remains Oded Schramm, *Conformally invariant scaling limits: an overview and a collection of problems*, ICM 2006, arXiv:math/0602151, Problem 2.1. In the intake's exact quotation, the problem asks for existence of the `s downarrow 0` scaling limit of the infinite half-plane self-avoiding walk and identification of that limit with `SLE_{8/3}`.

The current quantitative bridge baseline remains Dmitrii Krachun and Christoforos Panagiotis, *Quantitative sub-ballisticity of self-avoiding walk on the hexagonal lattice*, Annals of Probability 54(3) (2026), 1109--1125, DOI `10.1214/24-AOP1730`, published 31 May 2026. Their theorem gives the published explicit bridge exponent `10^{-10}`. A fresh 17 September 2026 bounded search for a later fixed-lattice SAW-to-`SLE_{8/3}` proof or a later advertised explicit improvement of their bridge exponent did not locate one. This negative search is not a worldwide openness or novelty certificate.

The stale Beck--Fiala scheduler title was refreshed as required. Bansal--Jiang, arXiv:2508.03961v2, prove `O(sqrt(t))` efficiently for `t>=log^2 n` and a weaker sparse-regime bound. Guo--Fang--Lu, arXiv:2609.11189v1, submitted 10 September 2026, explicitly state a dimension-free Boolean Komlos constant `3 sqrt(2 pi)` and deduce

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}
\]

for every integer `t>=1`, with no restriction on `n`. The repository has distinct R12 and P26 end-to-end PASS audits of that external theorem. I retain the precise label **very recent primary-preprint resolution claim, internally audited, not mature external consensus**. The canonical R16 research target remains I0036; this run does not restart Beck--Fiala merely because the native title is stale.

## 3. Retained source inequalities

Let `D_T,G_k` be Krachun--Panagiotis' critical quantities. The preceding R16 reports recovered and source-checked the following facts.

The tail estimate is

\[
\sum_{k\ge T}G_k\le c_GD_{2T-1},
\qquad
c_G=\frac{1+\sqrt2}{2},
\tag{3.1}
\]

`D_T` is nonincreasing, and

\[
B_T\le \cos(\pi/8)D_T<D_T.
\tag{3.2}
\]

At every integer scale `T>=1`, one of the source alternatives holds:

\[
T D_{10T}^{2}
\le256\sqrt2\frac{D_{\lceil(T+1)/2\rceil}}{D_{4T}}
\left(\sum_{i=0}^{T}D_i\right)
\left(\sum_{\ell=T}^{7T}G_\ell\right),
\tag{3.3a}
\]

or

\[
T^2D_{18T}^{3}
\le2^{15}\left(
\frac{D_{\lceil(T+1)/2\rceil}}{D_{10T}}
\sum_{i=0}^{\lfloor5T/2\rfloor}D_i
\right)^2
\left(\sum_{k=T}^{21T}G_k\right).
\tag{3.3b}
\]

The previous one-threshold proof used a **uniform** pigeonhole allocation over the disjoint bands `[22^jT_0,21\,22^jT_0]`. The new idea is to stop treating all logarithmic scales equally.

## 4. The three new-method attacks

### #5 — add a parameter and differentiate in it

The ratio split need not use one threshold at every selected scale. Write

\[
T_j=22^jT_0,
\qquad
\lambda_j=\lambda_0\,22^{-j\varepsilon}.
\tag{4.1}
\]

The direct-drop branch contains

\[
\lambda_j^{-1}(T_j/2)^{-\varepsilon}
=
\lambda_0^{-1}2^\varepsilon T_0^{-\varepsilon},
\tag{4.2}
\]

so this choice removes **all** dependence on `j` from that branch.

In the cubic branch, the two powers of the ratio and the two powers from the partial-sum normalization then leave the scale factor

\[
22^{-4j\varepsilon}.
\tag{4.3}
\]

Thus a uniform `1/M` pigeonhole is throwing away a deterministic gain. Differentiating the logarithmic cubic loss with respect to the scale index says the natural band budget should grow approximately like

\[
22^{4j\varepsilon}.
\tag{4.4}
\]

This is the new parameter family.

### #14 — find the group acting

The source recurrence is organized by the discrete dilation action

\[
T\mapsto22T.
\]

On logarithmic scale this is translation by one. The cancellation (4.2) is a cocycle cancellation for that `Z`-action: the threshold is transformed by exactly the factor needed to keep the direct branch invariant. The cubic branch transforms by the residual character `22^{-4j epsilon}`. The right pigeonhole measure is therefore not uniform counting measure on the orbit; it is a tilted measure compensating this character.

This is the conceptual reason for the weighted band construction below.

### #16 — compute finite profiles and stare at the sequence

I computed finite `K`-bin approximations to the ideal weight `22^{4j epsilon}` and looked for simple rational geometric ratios that remain **below** the ideal growth, so the proof can be certified by integer arithmetic.

At the clean block invariant

\[
M\varepsilon=\frac1{21},
\tag{4.5}
\]

the exact ideal ratio between adjacent `K`-bins is `22^(4/(21K))`. The finite search gave the progression

| K | rational bin ratio | normalized first-bin factor `c_0` (decimal only) |
|---:|---:|---:|
| 4 | `8/7` | `0.80944...` |
| 8 | `15/14` | `0.77574...` |
| 16 | `28/27` | `0.75068...` |
| 32 | `55/54` | `0.74177...` |
| 64 | `110/109` | `0.73944...` |
| 128 | `218/217` | `0.73613...` |

The 128-bin profile already captures most of the available weighted gain while keeping the finite core simple enough to certify exactly. I retain `K=128`; I do not claim the table itself is a theorem of independent interest.

## 5. Weighted logarithmic-scale lemma

Set

\[
A=1000,
\qquad
\varepsilon=\frac1{14,469,504},
\qquad
M=689,024,
\qquad
M\varepsilon=\frac1{21},
\tag{5.1}
\]

and

\[
q=22^{-1/21},
\qquad
K=128,
\qquad
L=M/K=5,383.
\tag{5.2}
\]

Let

\[
R=\frac{218}{217},
\qquad
S=\sum_{r=0}^{127}R^r,
\qquad
c_r=\frac{128R^r}{S}.
\tag{5.3}
\]

Then

\[
\sum_{r=0}^{127}c_r=128.
\tag{5.4}
\]

Partition the indices `j=0,...,M-1` into consecutive bins

\[
\mathcal B_r=\{rL,\ldots,(r+1)L-1\}.
\]

For `j in B_r`, assign pigeonhole weight

\[
w_j=\frac{c_r}{M}.
\tag{5.5}
\]

Because every bin has `L=M/128` elements, (5.4) gives

\[
\sum_{j=0}^{M-1}w_j=1.
\tag{5.6}
\]

Finally define the scale-dependent ratio threshold

\[
\lambda_j=\lambda_0\,22^{-j\varepsilon},
\qquad
\lambda_0=\frac{839}{625}=1.3424.
\tag{5.7}
\]

The exact inequality

\[
218^{672}<22\,217^{672}
\tag{5.8}
\]

means

\[
R<22^{1/672}=22^{4/(21\cdot128)}.
\tag{5.9}
\]

Therefore, whenever `j in B_r`,

\[
\begin{aligned}
c_r22^{-4j\varepsilon}
&\le c_0R^r22^{-4rL\varepsilon}\\
&=c_0R^r22^{-r/672}\\
&\le c_0.
\end{aligned}
\tag{5.10}
\]

This is the whole weighted gain.

## 6. The improved bridge theorem

### Theorem R16-I0036-C05

For every integer `T>=1`,

\[
\boxed{
D_T\le1000T^{-1/14,469,504}
}
\tag{6.1}
\]

and hence

\[
\boxed{
B_T\le1000T^{-1/14,469,504}.
}
\tag{6.2}
\]

### Proof

Let

\[
E_s=22^{Ms}.
\]

I prove simultaneously

\[
D_k\le Ak^{-\varepsilon}
\quad(1\le k\le E_s),
\qquad
D_{E_s}\le qA E_s^{-\varepsilon}.
\tag{6.3}
\]

The base is immediate: `D_1<=D_0=sec(pi/8)<11/10`, while `q>5/6` and hence `qA>833`.

Assume (6.3) through `T_0=E_{s-1}` and put

\[
K_0=E_s=22^M T_0.
\]

For every `T_0<=k<=K_0`, monotonicity gives

\[
D_k\le D_{T_0}
\le qAT_0^{-\varepsilon}
=AK_0^{-\varepsilon}
\le Ak^{-\varepsilon}.
\tag{6.4}
\]

So only the stronger endpoint estimate remains.

By (3.1), monotonicity and the previous strong endpoint,

\[
\sum_{k\ge T_0}G_k
\le c_GD_{2T_0-1}
\le c_GqAT_0^{-\varepsilon}.
\tag{6.5}
\]

The intervals

\[
[T_j,21T_j],
\qquad T_j=22^jT_0,
\qquad 0\le j<M,
\]

are pairwise disjoint. Since the weights (5.5) sum to one, there is some `j`, lying in some bin `B_r`, such that

\[
\sum_{k=T_j}^{21T_j}G_k
\le
\frac{c_r}{M}\,c_GqAT_0^{-\varepsilon}.
\tag{6.6}
\]

Write `T=T_j`.

For every integer `R_0>=1`, the induction hypothesis and an integral bound give

\[
\sum_{i=0}^{R_0}D_i
\le AK_1R_0^{1-\varepsilon},
\tag{6.7}
\]

where

\[
K_1=\frac{1+D_0/A}{1-\varepsilon}
<\frac{501}{500}.
\tag{6.8}
\]

The last inequality follows from `D_0=sec(pi/8)<11/10` and the explicit epsilon.

Also `lambda_j>1` throughout the block. Indeed `lambda_0>6/5`, while

\[
q=22^{-1/21}>5/6
\]

because `22*5^21<6^21`; hence `lambda_j>lambda_0q>1`.

#### Source case (3.3a)

If `D_{4T}=0`, then `D_{K_0}=0` and there is nothing to prove. Otherwise set

\[
R_a=\frac{D_{\lceil(T+1)/2\rceil}}{D_{4T}}.
\]

If `R_a>lambda_j`, then using the induction bound at `ceil((T+1)/2)` gives

\[
\begin{aligned}
D_{K_0}
&\le D_{4T}
<\lambda_j^{-1}D_{\lceil(T+1)/2\rceil}\\
&\le \frac{2^\varepsilon}{\lambda_0}AT_0^{-\varepsilon}.
\end{aligned}
\tag{6.9}
\]

The exact finite certificate proves

\[
\frac{2^\varepsilon}{\lambda_0}
<\frac{14899}{20000}
<22^{-2/21}=q^2,
\tag{6.10}
\]

where the analytic first step uses `2^epsilon<e^epsilon<1/(1-epsilon)`. Therefore

\[
D_{K_0}<q^2AT_0^{-\varepsilon}
=qAK_0^{-\varepsilon}.
\tag{6.11}
\]

If instead `R_a<=lambda_j`, use (3.3a), (6.6), and (6.7). Since `[T,7T]` is contained in the selected `[T,21T]` band,

\[
\begin{aligned}
D_{K_0}^2
&\le D_{10T}^2\\
&\le
\frac{256\sqrt2\lambda_j}{T}
(AK_1T^{1-\varepsilon})
\left(\frac{c_r}{M}c_GqAT_0^{-\varepsilon}\right)\\
&=
\left(
\frac{256\sqrt2\lambda_0c_GK_1}{M}
 c_r22^{-2j\varepsilon}
\right)
qA^2T_0^{-2\varepsilon}.
\end{aligned}
\tag{6.12}
\]

The exact finite core gives `c_r<=c_127<4/3` and, using `sqrt(2)<3/2`, `c_G<121/100`, `K_1<501/500`,

\[
\frac{256\sqrt2\lambda_0c_GK_1}{M}c_r22^{-2j\varepsilon}
<\frac12<q^3.
\tag{6.13}
\]

Hence again

\[
D_{K_0}^2<(q^2AT_0^{-\varepsilon})^2.
\tag{6.14}
\]

#### Source case (3.3b)

If `D_{10T}=0`, the endpoint is trivial. Otherwise set

\[
R_b=\frac{D_{\lceil(T+1)/2\rceil}}{D_{10T}}.
\]

If `R_b>lambda_j`, the same direct-drop argument (6.9)--(6.11) applies.

If `R_b<=lambda_j`, then (3.3b), (6.6), and (6.7) give

\[
\begin{aligned}
D_{K_0}^3
&\le D_{18T}^3\\
&\le
\frac{2^{15}\lambda_j^2}{T^2}
\left(AK_1(5T/2)^{1-\varepsilon}\right)^2
\left(\frac{c_r}{M}c_GqAT_0^{-\varepsilon}\right)\\
&=
\left[
\frac{2^{15}\lambda_0^2c_GK_1^2(5/2)^{2(1-\varepsilon)}}{M}
 c_r22^{-4j\varepsilon}
\right]
qA^3T_0^{-3\varepsilon}.
\end{aligned}
\tag{6.15}
\]

Now use the weighted cancellation (5.10). With `c_G<121/100`, `K_1<501/500`, and `(5/2)^{2(1-epsilon)}<(5/2)^2`, the bracket is strictly less than

\[
\frac{2^{15}(839/625)^2(121/100)(501/500)^2(25/4)c_0}{689024}
<\frac{47901}{100000}
<22^{-5/21}=q^5.
\tag{6.16}
\]

The final comparison is an exact integer inequality

\[
22^5\,47901^{21}<100000^{21}.
\tag{6.17}
\]

Therefore

\[
D_{K_0}^3<(q^2AT_0^{-\varepsilon})^3,
\]

and so

\[
D_{K_0}<qAK_0^{-\varepsilon}.
\tag{6.18}
\]

This closes the strong endpoint induction in every source branch. Equation (6.4) then gives (6.1) for all integers `T>=1`, and (3.2) gives (6.2). `QED`

## 7. Metric movement and what actually changed

The frozen metric moves from

\[
\boxed{
\varepsilon_{\rm bridge}=\frac1{18,817,988}
}
\]

to

\[
\boxed{
\varepsilon_{\rm bridge}=\frac1{14,469,504}
=6.911\ldots\times10^{-8}.
}
\tag{7.1}
\]

The denominator improves by the exact factor

\[
\frac{18,817,988}{14,469,504}=1.300527509\ldots.
\]

This is **not** just constant retuning of the previous proof. The substantive change is the nonuniform logarithmic-scale pigeonhole measure coupled to a scale-dependent ratio threshold. The old proof discarded the factor `22^{-4j epsilon}`; the new proof converts it into a roughly 26% reduction of the cubic pigeonhole coefficient (`c_0=0.73613...` instead of `1`) and then reoptimizes the invariant `M epsilon`.

The theorem is new to this repository. A bounded current-literature search did not locate this exponent or weighted-pigeonhole reorganization. That is **not** a publication-priority certificate.

## 8. Exact finite certificate

The exact checker is

`artifacts/R16/2026-09-17T11-47-00Z_i0036_weighted_scale_pigeonhole_check.py`

created at commit

`8d0cb8ff60900cfb3978a9ac31a6102d8634b198`.

Its executed output is

`artifacts/R16/2026-09-17T11-47-00Z_i0036_weighted_scale_pigeonhole_check.out`

created at commit

`a5a30b0e3bf1fd9b59c29690c20ac7cbb6c29cc4`.

The run ends

`ALL_EXACT_CHECKS_PASS`.

The checker verifies only the finite arithmetic: `M/K=5383`, the exact normalized geometric weights, `(218/217)^672<22`, the rational `K_1` envelope, the direct-drop comparison through `14899/20000`, `lambda_j>1`, `c_max<4/3`, the case-(a) coefficient, the cubic coefficient through `47901/100000`, and the exact movement `14,469,504<18,817,988`. The induction and all theorem-sized inequalities are written on the page above; this is a self-check, not an outside audit.

## 9. What failed and what survives

The finite-profile computation shows that increasing the number of bins keeps lowering the first-bin factor toward the ideal continuously tilted pigeonhole measure. But the gain is now diminishing. This route has moved the metric substantially, so it is retained as a quantitative tool; the next run should **not** spend its research budget merely taking `K=256,512,...` for a tiny denominator improvement.

The phase-resolved transfer route from the preceding report also survives. The bridge exponent is still far from the conjectural `1/4`, and even a much stronger vertical bridge exponent does not by itself control lateral shape. The source-level missing theorem remains a quantitative geometric/annulus-crossing estimate strong enough to feed a tightness/conformal-invariance argument.

The next genuinely different methods are **#6 DEFORM TO A POINT YOU CAN SOLVE, #10 DERANDOMIZE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE**. Concretely: deform the finite-strip transfer operator to widths where the positive Perron certificate is explicit; use those exact certificates to guess a deterministic state-dependent super-eigenvector template; then compare the resulting spectral-gap/phase constants with loop/parafermionic transfer systems in which the full discrete-holomorphic structure is available. Do not repeat `#5,#14,#16` next run.

Because the metric moved, the supported unchanged count resets to zero. No stuck recovery is triggered.

## 10. Closure / audit status

I0036 remains **PARTIAL / OPEN** relative to Schramm Problem 2.1. This bridge theorem does not prove tightness, uniqueness of subsequential limits, conformal invariance, or `SLE_{8/3}` identification.

Repository search still finds no P26 end-to-end audit and no distinct second OTHER-track end-to-end audit of the I0036 package. Therefore Section-G closure is not available and no `paper_<name>/` closure folder is created.

## 11. Model/scheduler control and the historical P26 modification failure

The exposed scheduler mutation schema still offers title/prompt, schedule or relative start, timing mode, enabled state and task identity. It exposes **no model-family field and no reasoning-effort field**, and no authenticated applied-effort telemetry. Thus GPT-6/maximum can be requested in prompt text only in this surface; it cannot be honestly asserted as the runtime.

To enforce GPT-6/maximum, an authorized product/workspace scheduler or API would have to expose model and reasoning controls and runtime telemetry, or platform/workspace support would have to migrate/repair the task into a surface that does.

The historical P26 `You cannot modify this task` result is not universal: current root `RESULTS.md` records a later successful P26 prompt update from another authorized context, while a separate context denied R-series edits. The compliant workaround for any task that still refuses modification is owner/workspace/platform authorization repair in a context that owns that task. Do not bypass permissions or create duplicate schedules.

No scheduler mutation was attempted in this run.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R16
  canonical_target: I0036
  allocation: HARD_OUTSIDE
  source: Schramm ICM 2006 Problem 2.1
  source_status: OPEN
  claim_status: ADMITTED_ACTIVE_EXCLUSIVE_R16
  metric_name: epsilon_bridge
  metric_definition: largest explicit epsilon with a complete R16 proof of B_T <= C_epsilon T^(-epsilon) for every integer T>=1 in the critical Krachun-Panagiotis hexagonal-lattice normalization
  before: 1/18817988
  after: 1/14469504
  constant_after: 1000
  movement: true
  supported_unchanged_count_before: 1
  supported_unchanged_count_after: 0
  status: PARTIAL
  methods:
    - 5
    - 14
    - 16
  theorem_id: R16-I0036-C05
  checker: artifacts/R16/2026-09-17T11-47-00Z_i0036_weighted_scale_pigeonhole_check.py
  checker_commit: 8d0cb8ff60900cfb3978a9ac31a6102d8634b198
  output: artifacts/R16/2026-09-17T11-47-00Z_i0036_weighted_scale_pigeonhole_check.out
  output_commit: a5a30b0e3bf1fd9b59c29690c20ac7cbb6c29cc4
  checker_result: ALL_EXACT_CHECKS_PASS
  p26_audit: PENDING_NOT_FOUND
  second_other_audit: PENDING_NOT_FOUND
  publication_novelty: UNVERIFIED
  next_methods:
    - 6
    - 10
    - 17
  next_obligation: quantitative lateral/aspect-ratio or transfer-operator certificate that advances the source-level scaling-limit route, not merely another tiny K-bin exponent optimization
  model_requested: GPT-6 maximum
  model_actual: GPT-5.6 Sol
  reasoning_actual: UNVERIFIED
  scheduler_model_selector_exposed: false
  scheduler_reasoning_selector_exposed: false
```

No shared root ledger, peer-track file, email, Drive content, public post, permission, purchase, workflow, or scheduler state was modified.
