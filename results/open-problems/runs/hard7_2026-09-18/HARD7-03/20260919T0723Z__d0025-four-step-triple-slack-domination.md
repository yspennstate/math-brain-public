Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 2500/29711 -> 12500/148461`. Methods tried: B13 / B23 / B26.**

# HARD7-03 — four-step triple-slack domination correction

Status: **PARTIAL / Seppäläinen Problem 4 remains open as a whole.** This run resumes the exclusive `D0025` claim and the four-step pair-overlap checkpoint. The substantive advance is to recover a rigorously positive part of the *exact slack* discarded by the preceding pairwise max/min inequality. The recovered three-endpoint correlation lowers the homogeneous lazy-LPP shape bound from `2.9711` to `2.96922`, hence increases the certified binary-disorder plateau half-width from `2500/29711` to `12500/148461`.

## 1. Continuity, ownership, source status, and repository state

The active canonical claim is still

`operations/claims/D0025.md`

owned by `HARD7-03`, canonical intake key `disordered_asep_open_1999::problem_4`. Before doing new mathematics I re-read the HARD7 control file, the current new-methods policy and owner directive, campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the D0025 claim, and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-03/20260919T0628Z__d0025-four-step-pair-overlap-chernoff.md`.

I also checked the neighboring HARD7-02 / HARD7-04 state available during this run. HARD7-02's last complete report was its STUCK1 checkpoint (`03c1a571e9dd69de6aac79956da5a6212fe130e3`) with later exact-axis artifacts appearing concurrently; HARD7-04's newest complete checkpoint was STUCK2 (`99894bcaca467fe7bfd065b4b3c8c8ebfec2010f`). Neither is an equivalent D0025 claim. A repository-wide canonical-key search also recovered another particle-system worker explicitly declining D0025 because HARD7-03 owns it. No claim collision, release, posted equivalent, or source-resolution record surfaced.

Primary source: Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), Problem 4, Section 4; arXiv `math/9906194`; DOI `10.11606/resimeusp.v4i1.74889`.

- source: `https://arxiv.org/abs/math/9906194`
- journal page: `https://revistas.usp.br/resenhasimeusp/pt_BR/article/view/74889`

A bounded 2026-09-19 literature refresh searched the exact source title together with `disordered K-exclusion plateau site disorder K>=2`, `general K TASEP site disorder plateau`, and `partial exclusion asymmetric site disorder flux`. It recovered the distinct Gonçalves–Hayashi–Sasada partial-exclusion work (`arXiv:2405.15142`), whose product-rate / gradient setting is not Seppäläinen's iid site-rate model, and did not locate a 2024--2026 paper closing the exact `K>=2` iid site-disorder residual. This is bounded negative evidence only, not a worldwide-openness or novelty certificate.

The frozen first test case remains

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

and the metric remains

\[
\Delta_2(Q)=\sup\{\delta\ge0:
 f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

The shared root ledgers are not modified by this worker; the structured delta at the end is for the designated reconciler.

## 2. Frozen metric: before and after

The preceding checkpoint proved

\[
G_1(0)\le \frac{29711}{10000},
\qquad
\Delta_2(Q)\ge \frac{1}{4G_1(0)}
\ge \frac{2500}{29711}.
\tag{2.1}
\]

Here `G_1(0)` is the central shape value of the homogeneous rate-one `K=2` lazy-LPP representation used throughout the checkpoint chain. This run proves

\[
\boxed{G_1(0)\le \frac{148461}{50000}=2.96922}
\tag{2.2}
\]

and therefore

\[
\boxed{
\Delta_2(Q)\ge \frac{12500}{148461}
=0.084197196570143\ldots .}
\tag{2.3}
\]

Thus

\[
L:\quad \frac{2500}{29711}
\longrightarrow \frac{12500}{148461},
\]

with exact gain

\[
\frac{12500}{148461}-\frac{2500}{29711}
=\frac{235000}{4410924771}>0.
\tag{2.4}
\]

## 3. The exact slack left by the previous four-step inequality

For three nonnegative numbers,

\[
\max(x,y,z)=x+y+z-\min(x,y)-\min(y,z)
-(\min(x,z)-y)_+.
\tag{3.1}
\]

The previous run dropped the last nonnegative term. For a fourth-step endpoint `d` with three predecessors, put

\[
x=e^{\theta T_3(d-1)},\quad y=e^{\theta T_3(d)},\quad
z=e^{\theta T_3(d+1)}.
\]

Its missing correction is therefore exactly

\[
R_d(\theta)=
\mathbb E\Big[
(\min(e^{\theta T_3(d-1)},e^{\theta T_3(d+1)})
-e^{\theta T_3(d)})_+
\Big].
\tag{3.2}
\]

There are five such endpoints, `d=-2,-1,0,1,2`. The problem is to lower-bound these genuinely three-endpoint quantities without enumerating the full four-layer max-plus chamber arrangement.

Write the first-layer iid `Exp(1)` weights as

\[
A_{-1},A_0,A_1,
\]

and the second-layer iid `Exp(1)` weights as

\[
B_{-2},B_{-1},B_0,B_1,B_2.
\]

The layer-two passage values are

\[
\begin{aligned}
Y_{-2}&=A_{-1}+B_{-2},\\
Y_{-1}&=\max(A_{-1},A_0)+B_{-1},\\
Y_0&=\max(A_{-1},A_0,A_1)+B_0,\\
Y_1&=\max(A_0,A_1)+B_1,\\
Y_2&=A_1+B_2.
\end{aligned}
\tag{3.3}
\]

Let

\[
S_e=\max\{Y_z:|z-e|\le1,\ -2\le z\le2\},
\qquad T_3(e)=S_e+C_e,
\tag{3.4}
\]

where the `C_e` are a fresh iid `Exp(1)` layer.

Two elementary exact transforms will be used repeatedly. For iid unit exponentials `X_1,...,X_m`,

\[
J_m(\theta)
:=\mathbb E\left[e^{\theta X_1}
\mathbf 1\{X_1=\max_iX_i\}\right]
=\frac{(m-1)!}{\prod_{j=1}^m(j-\theta)},
\qquad 0<\theta<1.
\tag{3.5}
\]

Indeed,

\[
J_m(\theta)=\int_0^\infty
 e^{-(1-\theta)x}(1-e^{-x})^{m-1}\,dx,
\]

and expansion or the beta integral gives (3.5).

Second, if `U=min(C_1,C_3)~Exp(2)` and `V=C_2~Exp(1)` are independent, then

\[
\kappa(\theta)
:=\mathbb E[(e^{\theta U}-e^{\theta V})_+]
=\frac{\theta}{(2-\theta)(3-\theta)}.
\tag{3.6}
\]

To verify (3.6), on `U>V`,

\[
\mathbb E[e^{\theta U};U>V]
=\frac2{2-\theta}-\frac2{3-\theta},
\]

while

\[
\mathbb E[e^{\theta V};V<U]=\frac1{3-\theta};
\]

their difference is (3.6).

## 4. B13 — find what only increases: collapse predecessor maxima by domination

The useful monotonicity is not a time monotone; it is the coordinatewise order inside the max-plus recursion: once one `Y_j` dominates all competitors feeding several adjacent `S_e`, every one of those predecessor maxima is forced to the same value. This makes the three-endpoint slack factor into a weighted order event on the first two layers and the universal one-layer factor `kappa(theta)`.

For `d=2`, define

\[
E_2=\{A_1\ge A_0\}\cap\{B_2\ge B_1\}.
\tag{4.1}
\]

On `E_2`, `Y_2\ge Y_1`; hence

\[
S_2=S_3=Y_2,\qquad S_1\ge Y_2.
\]

Therefore, pointwise on `E_2`,

\[
R_2\text{'s integrand}
\ge e^{\theta Y_2}
(e^{\theta\min(C_1,C_3)}-e^{\theta C_2})_+.
\tag{4.2}
\]

The `A`, `B`, and `C` layers are independent, and

\[
\mathbb E[e^{\theta Y_2};E_2]
=J_2(\theta)^2.
\]

Consequently

\[
R_2(\theta)\ge H_2(\theta)
:=\kappa(\theta)J_2(\theta)^2.
\tag{4.3}
\]

Reflection gives the same bound for `R_{-2}`.

**B13 outcome: successful.** A partial order event turns a three-endpoint correlation into a product of exact one-dimensional order statistics.

## 5. B23 — do the unexpected edge case first

The tempting route was to attack the central triple `d=0`, where the geometry is most symmetric. The edge triple `d=2` is actually cheaper because only two first-layer and two second-layer comparisons are needed. Equation (4.3) is thus the largest single easy correction, rather than the symmetric center.

This reverses the natural central-first strategy and shows why the four-step pair bound had more recoverable slack near `d=+/-2` than a symmetry-only analysis suggests. At the eventual rational `theta` below,

\[
H_2=0.508764531573568\ldots,
\]

so the two reflected edge triples already contribute more than one unit to the MGF subtraction before the common fourth-layer factor.

**B23 outcome: successful.** The edge geometry, not the center, supplies the strongest low-complexity correction.

## 6. B26 — hunt the three sporadic domination geometries

The remaining interior locations require different domination events rather than a single over-strong global event.

### 6.1. The `d=1` / `d=-1` pair

Set

\[
E_1=
\{A_1=\max(A_{-1},A_0,A_1)\}
\cap
\{B_1=\max(B_{-1},B_0,B_1,B_2)\}.
\tag{6.1}
\]

On `E_1`,

\[
Y_1\ge Y_{-1},Y_0,Y_2,
\]

and therefore

\[
S_0=S_1=S_2=Y_1.
\]

The same factorization as above gives

\[
R_1(\theta)\ge H_1(\theta)
:=\kappa(\theta)J_3(\theta)J_4(\theta).
\tag{6.2}
\]

Reflection gives `R_{-1}>=H_1`.

### 6.2. The central `d=0` triple

Set

\[
E_0=
\{A_0=\max(A_{-1},A_0,A_1)\}
\cap
\{B_0=\max(B_{-2},B_{-1},B_0,B_1,B_2)\}.
\tag{6.3}
\]

Then `Y_0` dominates every `Y_j`, so

\[
S_{-1}=S_0=S_1=Y_0
\]

and

\[
R_0(\theta)\ge H_0(\theta)
:=\kappa(\theta)J_3(\theta)J_5(\theta).
\tag{6.4}
\]

Thus all five three-predecessor endpoints contribute the rigorous total correction

\[
H(\theta)
:=2H_2(\theta)+2H_1(\theta)+H_0(\theta)>0.
\tag{6.5}
\]

**B26 outcome: successful.** Treating the edge, near-edge, and center as three genuinely different order events gives a strictly stronger bound than imposing one uniform domination pattern.

## 7. Refined four-step MGF bound

Retain the preceding exact notation

\[
A_3(\theta)=\sum_{e=-3}^3\mathbb E e^{\theta T_3(e)}
\]

with

\[
A_3(\theta)=
\frac{2(2268-4408\theta+3748\theta^2-1918\theta^3
+652\theta^4-143\theta^5+18\theta^6-\theta^7)}
{(3-\theta)^4(2-\theta)^3(1-\theta)^3},
\tag{7.1}
\]

and the previous adjacent-pair subtraction

\[
C(\theta)=\frac8{2-\theta}
\bigl(M_2(0;\theta)+M_2(1;\theta)+M_2(2;\theta)\bigr).
\tag{7.2}
\]

Summing the exact identity (3.1) over the fourth-step endpoints and using (4.3), (6.2), and (6.4) yields

\[
A_4^{\rm actual}(\theta)
\le U_4^{\rm tri}(\theta)
:=\frac{3A_3(\theta)-C(\theta)-H(\theta)}{1-\theta}.
\tag{7.3}
\]

The factor `(1-theta)^{-1}` is the MGF of the independent fourth-layer `Exp(1)` endpoint weight. Equation (7.3) is strictly stronger than the previous pair-only bound because `H(theta)>0` for `0<theta<1`.

## 8. Exact rational certificate and asymptotic shape consequence

Choose

\[
\theta=\frac{5877}{10000},
\qquad
 a=\frac{148461}{50000}=2.96922.
\tag{8.1}
\]

The executed exact-arithmetic checker obtains

\[
\begin{aligned}
H_2&=0.508764531573568\ldots,\\
H_1&=0.307459724124535\ldots,\\
H_0&=0.278729664007012\ldots,\\
H&=1.911178175403219\ldots,
\end{aligned}
\tag{8.2}
\]

and

\[
U_4^{\rm tri}(\theta)
=1074.958141816336592\ldots .
\tag{8.3}
\]

All quantities in the checker are exact rationals; decimals here are display only. Also

\[
4\theta a=\frac{872505297}{125000000}=6.980042376.
\tag{8.4}
\]

Let

\[
S_{21}(x)=\sum_{k=0}^{21}\frac{x^k}{k!}.
\]

For positive `x`, `S_{21}(x)<e^x`. The checker proves in exact rational arithmetic

\[
S_{21}\!\left(\frac{872505297}{125000000}\right)
-U_4^{\rm tri}(5877/10000)>0,
\tag{8.5}
\]

with decimal margin

\[
0.001120934802490\ldots .
\]

Hence

\[
U_4^{\rm tri}(\theta)e^{-4\theta a}<1.
\tag{8.6}
\]

Now concatenate independent four-time-layer blocks exactly as in the preceding two-, three-, and four-step checkpoints. For each coarse boundary sequence the blocks use disjoint new layers, while summation over all allowed block displacements is already contained in `A_4^{actual}`. Therefore

\[
\Pr\{T_1(4m,0)\ge4ma\}
\le
\left[U_4^{\rm tri}(\theta)e^{-4\theta a}\right]^m.
\tag{8.7}
\]

The right side is summable in `m`. Borel--Cantelli and the same homogeneous shape-limit theorem used in the inherited checkpoint chain give

\[
G_1(0)\le a=\frac{148461}{50000}.
\]

Combining this with the already established site-disorder plateau comparison `Delta_2(Q)>=1/(4G_1(0))` proves (2.3). This is an asymptotic theorem from an exact block-MGF inequality, not a finite-size fit or simulation.

## 9. Exact artifacts and read-back

The new idea was derived before any checker was written. Only the final finite algebra was certified by:

- `artifacts/hard7_2026-09-18/HARD7-03/four_step_triple_slack_20260919T0723Z.py`, commit `949797b423cf3082736f50296edfcca19bb26fa0`;
- `artifacts/hard7_2026-09-18/HARD7-03/four_step_triple_slack_20260919T0723Z.out`, commit `677d5c97009cb70107cd902c5355ed0258fc4a16`.

Both were read back from their exact returned commits. The code was executed in this run using exact `Fraction` arithmetic, and the archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

The checker independently verifies the closed forms for `J_m`, `kappa`, the inherited `A_3` and pair correction at the chosen rational `theta`, the positive triple-slack subtraction, the Taylor lower-bound margin, and the exact metric gain. It is a self-check, not an independent closure audit.

## 10. What this run does not prove

- It does not close Seppäläinen Problem 4 in full.
- It does not determine the exact homogeneous constant `G_1(0)`.
- It does not make the domination-event lower bounds on `R_d` sharp.
- It does not independently audit the inherited general-`K` site-disorder plateau comparison.
- It does not address particlewise disorder or every stationary ergodic environment.
- It does not infer an infinite-volume conclusion from simulation; no simulation is used in the proof.
- It does not assert worldwide novelty from a bounded literature search.

The correct status remains **PARTIAL**.

## 11. Section-I state and next mathematical route

The frozen metric moved, so the unchanged-run count resets and no stuck recovery is due.

The present correction uses only one domination event for each of the three geometric types. The next non-bookkeeping route should partition the order space into additional disjoint events on which the three `S_e` share a common baseline, or derive the conditional slack exactly after fixing the rank pattern of the five `Y_j`. That can increase `H(theta)` without changing block length. If such a partition does not improve (7.3), the next useful category change is a transfer/operator bound for the vector `(T_3(e-1),T_3(e),T_3(e+1))`, not another re-run of this certificate.

## 12. Capability / scheduler statement

The scheduler surface exposed to this environment still offers task title, prompt, schedule, timing mode and enabled state, but no model selector, reasoning-effort selector or guaranteed execution duration. Thus GPT-6/maximum remains a prompt request only. This run's actual model is **GPT-5.6 Sol** and its reasoning level is **UNVERIFIED**; GPT-6 maximum is not claimed.

The repository policy records historical modification probes returning `You cannot modify this task` for P26 and some other IDs, together with later success from a different authorized context. This run did not probe or modify any scheduler. If a task is currently non-modifiable, the compliant route is the authorized owner/account/workspace interface or platform support/ownership correction; duplicating the task or bypassing permissions is not a workaround.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  canonical_target: D0025
  owner_claim: operations/claims/D0025.md
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  fixed_metric: "rigorous certified lower bound L <= Delta_2(Q) for Q=1/2 delta_{1/2}+1/2 delta_1"
  before: 2500/29711
  after: 12500/148461
  movement: true
  exact_gain: 235000/4410924771
  methods: [13, 23, 26]
  homogeneous_bound:
    object: "K=2 homogeneous lazy-LPP central shape G_1(0)"
    before_upper: 29711/10000
    after_upper: 148461/50000
    theta: 5877/10000
    block_length: 4
    method: "pair overlap plus three-endpoint domination-event slack subtraction"
  new_correlation_bound:
    kappa: "theta/((2-theta)(3-theta))"
    H2: "kappa*J2^2"
    H1: "kappa*J3*J4"
    H0: "kappa*J3*J5"
    total: "2*H2 + 2*H1 + H0"
  exact_artifacts:
    - artifacts/hard7_2026-09-18/HARD7-03/four_step_triple_slack_20260919T0723Z.py
    - artifacts/hard7_2026-09-18/HARD7-03/four_step_triple_slack_20260919T0723Z.out
  exact_output_status: "ALL_EXACT_CHECKS_PASS = True"
  section_I_state: "metric moved; stagnation reset"
  posted_changed: false
  results_changed: false
  queue_changed: false
  claim_changed: false
```

No shared-root mutation, email, Drive write, public posting, scheduler modification, independent audit, closure claim, or other-track edit was made in this run.