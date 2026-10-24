Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 2500000/29210369 -> 3125000/36511391`. Methods tried: B3 / B5 / B20.**

# HARD7-03 — parameter-uniform exact-pair envelope and Chernoff-parameter reoptimization

Status: **PARTIAL**. Seppäläinen Problem 4 remains open in its full source scope.

## 1. Continuity, ownership, required reads, and current-source screen

This execution resumes the existing exclusive canonical claim

`operations/claims/D0025.md`, owner `HARD7-03`, key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`.

At run start I re-read the governing surfaces `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the D0025 claim and repository-wide indexed D0025 / `disordered_asep_open_1999` intake trail; the newest own checkpoint `20260919T1721Z__d0025-full-center-winner-decomposition.md`; and the newest completed neighboring HARD7-02 / HARD7-04 states. HARD7-02 is on the distinct Campbell--O'Rourke heavy-tailed elliptic-matrix Question 1.9 line; HARD7-04 is on the distinct heavy-tailed configuration-model MST line. No D0025 claim collision, release, posted equivalent, or source reassignment was found. I re-read `operations/claims/D0025.md` immediately before this report; it still names HARD7-03 as owner.

The primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1--15, Problem 4, arXiv `math/9906194`, DOI `10.11606/resimeusp.v4i1.74889`. The source asks whether disordered asymmetric finite-capacity `K`-exclusion has an analogous phase transition/flat segment of the hydrodynamic flux around density `K/2`.

The active residual excludes the known ordinary `K=1` iid site-disorder plateau. The frozen case is still

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

and

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

A fresh bounded literature search on **19 September 2026** used the exact source title and the phrases `disordered asymmetric K-exclusion plateau K=2 site disorder`, `site disorder K-exclusion asymmetric flux plateau`, and `Seppalainen Problem 4 K-exclusion disorder plateau`. It recovered the known simple-exclusion plateau line (Bahadoran--Bodineau, arXiv `1602.06718`; Sly, arXiv `1609.06589`) and neighboring disordered zero-range / random-environment work, but no theorem closing the exact `K>=2` iid site-rate residual. Together with the previously recorded checks of Floreani--Redig--Sau (`1911.12564`), Gonçalves--Hayashi--Sasada (`2405.15142`), and Ayyer--Misra's different integrable model, the honest status remains **OPEN_BY_BOUNDED_SEARCH**. This is not an exhaustive worldwide-openness or novelty certificate.

No shared root ledger, peer file, claim owner, Gmail object, Drive object, schedule, or public posting was modified.

### Runtime capability honesty

The exposed scheduler/tool schema still provides prompt/title, schedule/timing mode and enabled state, but **no binding model selector, no reasoning-effort selector, no authenticated reasoning telemetry, and no guaranteed run-duration control**. Therefore GPT-6/maximum remains prompt-requested only. This execution identifies as GPT-5.6 Sol; the reasoning level is unavailable and is recorded as `UNVERIFIED`.

Changing this requires a product/backend or authorized scheduler surface that actually exposes model and effort controls; a GitHub prompt cannot create them. The historical P26 `You cannot modify this task` event was an authorization/context restriction. Repository records later show P26 was editable in another authorized context. The compliant workaround for any still-denied task is the owning/authorized account/workspace context or platform support/ownership transfer, never a duplicate schedule or permission bypass. No scheduler mutation was attempted here.

## 2. Frozen metric and carry-in

The fixed source-relevant quantity remains a rigorous lower bound

\[
L\le \Delta_2(Q).
\]

The latest immutable checkpoint had proved

\[
G_1(0)\le A_{\rm old}:=\frac{29210369}{10^7}=2.9210369
\]

for the homogeneous rate-one `K=2` lazy-LPP central shape, and the already established D0025 transfer gives

\[
\Delta_2(Q)\ge \frac{1}{4G_1(0)}.
\tag{2.1}
\]

Thus the carry-in metric is

\[
L_{\rm old}=\frac{2500000}{29210369}
=0.085586046516564\ldots .
\tag{2.2}
\]

The latest run had removed the final centre-adjacent-pair decoupling loss at the inherited Chernoff parameter

\[
\theta_0=\frac{723}{1250}=0.5784,
\]

leaving the exact four-step envelope

\[
U_4(\theta_0)=
\frac{21591569424418754612288415153750985225648747506850585937500000}
{25076909157153837194356898290721189577238989596959847067723}
=861.013982588807266\ldots .
\tag{2.3}
\]

The key question for this run was not another overlap checker at fixed `theta_0`, but whether all exact pair formulas could be lifted to a **single parameterized envelope** and the Chernoff parameter reoptimized.

## 3. Idea-before-code and method rotation

Before archiving a checker I wrote and committed

`artifacts/hard7_2026-09-18/HARD7-03/20260919T1824Z__idea-theta-reoptimization.md`

at commit

`b276f25799c59a20c63cdc48e72412d644bd7b17`

and read it back successfully.

The preceding run used B7 / B18 / B25. This run uses a different triple:

- **B3 — prove something stronger.** Promote the fixed-`theta` centre calculation and the earlier nested-pair formulas to one parameterized exact-pair four-step envelope. **Outcome: successful at the proof level needed here.** Every term is an elementary exponential-order-cone integral; the exact checker reconstructs the old immutable rational from the parameterized formula before evaluating a new `theta`.
- **B5 — add a parameter and differentiate/optimize in it.** Treat `theta` itself as the free deformation parameter after the pair losses have changed. **Outcome: successful.** A scout search identifies a lower objective near `theta=0.57343`; the final result does not rely on the float search, because the chosen rational point is certified directly by exact arithmetic.
- **B20 — find why the algorithm fails.** Once all adjacent-pair losses are exact, locate the next obstruction rather than continuing to optimize a dead subterm. **Outcome: successful diagnostically.** The residual four-step slack is now in the earlier triple/higher-overlap inclusion envelope and finite block length, not the adjacent-pair step.

All thirty labels have appeared somewhere on this long D0025 track, so B3/B5/B20 are disclosed reuses after method exhaustion; the immediate triple is different from the previous run and the mathematical role is new.

## 4. B3: one exact all-pair envelope as a function of `theta`

Write

\[
0<\theta<1,\qquad q=1-\theta,\qquad a=2-\theta.
\]

The 14:18Z checkpoint proved the common-window four-step bound in the form

\[
U_4^{\cap}(\theta)
=\frac{3A_3(\theta)-C_{\cap}(\theta)-H(\theta)}{q},
\tag{4.1}
\]

where `A_3`, the common-window pair subtraction `C_cap`, and the already proved local-minimum/mixed-sign correction `H` are finite rational combinations of Laplace transforms of first-layer exponential order statistics. Their symbolic formulas are copied into the present checker rather than replaced by decimal constants.

### 4.1 Nested edge and near-edge pairs

For random `S<=T` measurable with respect to the previous layers and independent unit exponentials `C,D`, the exact two-clock identity from the 15:23Z checkpoint is, for every `0<theta<1`,

\[
\mathbb E e^{\theta\min(S+C,T+D)}
=\frac1q\left[
\mathbb E e^{\theta S}
-\frac{\theta}{a}\mathbb E e^{S-qT}
\right].
\tag{4.2}
\]

Indeed, conditional on `S,T`, put `d=T-S`. Since

\[
\Pr\{\min(C,d+D)>u\}
=\begin{cases}
e^{-u},&u<d,\\ e^{d-2u},&u\ge d,\end{cases}
\]

the exponential tail integral gives (4.2) directly. The edge transform is the explicit rational

\[
E_{\rm e}(\theta)
=\frac{5\theta^2-14\theta+10}{(2-\theta)^4(1-\theta)^2},
\tag{4.3}
\]

and the near-edge transform is the exact six-order-cone sum already proved in the 15:23Z report. Let the improvements over the common-window lower bounds be

\[
d_{\rm e}(\theta)=P_{\rm e}(\theta)-Q_{\rm e}(\theta),
\qquad
d_{\rm n}(\theta)=P_{\rm n}(\theta)-Q_{\rm n}(\theta).
\tag{4.4}
\]

### 4.2 Nonnested centre pair

The 17:21Z winner decomposition is also symbolic in `theta`. Conditional on the three first-layer exponentials, write the four second-layer competitors as shifted unit exponentials `Y_i=s_i+E_i`, with labels `X,Z,C,D` and `s_D` the largest deterministic shift on each first-layer order cone. For a winner `i`, inclusion--exclusion gives finite terms of the form

\[
\frac{(-1)^{|S|}}{q+|S|}
\exp\left(s_i+\sum_{j\in S}s_j-(q+|S|)s_D\right),
\tag{4.5}
\]

for the weighted maximum contribution, and

\[
\frac{q(-1)^{|S|}}{q+|S|}
\exp\left(\sum_{j\in S}s_j-(q+|S|)s_D\right)
\tag{4.6}
\]

for the complementary `e^{-qM}` term. Summing the centre winners gives exactly

\[
P_{\rm c}(A)
=\frac2a(W_C+W_D)
+\frac{4-\theta}{a^2}
\left(e^{s_X}R_X+e^{s_Z}R_Z\right).
\tag{4.7}
\]

The common-window comparison is

\[
Q_{\rm c}(A)=\frac2a\,\mathbb E\!\left[e^{\theta\max(Y_C,Y_D)}\mid A\right].
\tag{4.8}
\]

On each of the six strict first-layer order cones, write low/mid/high as

\[
u,\quad u+v,\quad u+v+w,\qquad u,v,w\ge0,
\]

with density `exp(-3u-2v-w)`. Every term of (4.5)--(4.8) is then a monomial exponential whose integral is a product of reciprocal positive linear rates at the two rational parameter values used below. Hence the centre gain

\[
d_{\rm c}(\theta)=P_{\rm c}(\theta)-Q_{\rm c}(\theta)
\tag{4.9}
\]

is evaluated exactly, without sampling or path discretization.

### 4.3 Combination and a hard consistency test

There are two reflected adjacent pairs of each class, and each pair occurs in two fourth-step predecessor windows. Therefore the exact-pair replacement of (4.1) is

\[
\boxed{
U_4^{\rm pair}(\theta)
=U_4^{\cap}(\theta)
-\frac{4}{1-\theta}
\left(d_{\rm e}(\theta)+d_{\rm n}(\theta)+d_{\rm c}(\theta)\right).
}
\tag{4.10}
\]

Before using a new parameter, the checker evaluates (4.10) at the inherited `theta_0=723/1250` and proves **exact equality** to the immutable rational (2.3). Thus the reparameterization is not a numerically patched surrogate for the previous theorem; it reconstructs it exactly.

## 5. B5: exact rational theta reoptimization

The Chernoff threshold suggested by a fixed `theta` is

\[
A>\frac{\log U_4^{\rm pair}(\theta)}{4\theta}.
\tag{5.1}
\]

A floating scout grid was used only to locate a promising rational point. It indicated a minimum near `theta=0.57343`, rather than the inherited `0.5784`. No floating calculation is used in the proof.

Choose exactly

\[
\theta_*:=\frac{57343}{100000}=0.57343.
\tag{5.2}
\]

The exact checker obtains

\[
U_4^{\cap}(\theta_*)=834.511516530670\ldots,
\]

with individual exact positive pair gains

\[
\begin{aligned}
d_{\rm e}(\theta_*)&=0.657140510713436\ldots,\\
d_{\rm n}(\theta_*)&=0.743465646925856\ldots,\\
d_{\rm c}(\theta_*)&=0.978232544588164\ldots .
\end{aligned}
\tag{5.3}
\]

Thus the full multiplicity-weighted pair subtraction is

\[
4(d_{\rm e}+d_{\rm n}+d_{\rm c})
=9.515354808909827\ldots,
\]

and (4.10) gives the exact rational

\[
U_4^{\rm pair}(\theta_*)
=\frac{44218621253097337675520630615938362481617650843715385324269439414717371037400000000000000000000}
{54442695413156570473578553858609910677406260157304013873650482583987300880543061947950013587}
\]

or

\[
U_4^{\rm pair}(\theta_*)=812.204849843116108\ldots .
\tag{5.4}
\]

Now choose the rational shape value

\[
A_*:=\frac{36511391}{12500000}
=2.92091128.
\tag{5.5}
\]

Set

\[
x=4\theta_*A_*
=\frac{2093672694113}{312500000000}.
\]

With

\[
S_{32}(x)=\sum_{k=0}^{32}\frac{x^k}{k!},
\]

the checker proves in exact rational arithmetic

\[
S_{32}(x)-U_4^{\rm pair}(\theta_*)>0,
\tag{5.6}
\]

with decimal margin

\[
2.817088860572193\times10^{-5}.
\]

All omitted exponential-series terms are positive, so

\[
U_4^{\rm pair}(\theta_*)<S_{32}(x)<e^x=e^{4\theta_*A_*}.
\tag{5.7}
\]

The already proved four-block Chernoff argument therefore yields

\[
\boxed{G_1(0)\le \frac{36511391}{12500000}=2.92091128.}
\tag{5.8}
\]

Applying the inherited transfer (2.1),

\[
\boxed{
\Delta_2(Q)\ge
\frac{1}{4A_*}
=\frac{3125000}{36511391}
=0.085589727326466\ldots .
}
\tag{5.9}
\]

This is an exact improvement over (2.2):

\[
\frac{3125000}{36511391}
-\frac{2500000}{29210369}
=\frac{3925625000}{1066511203813279}
=3.680809902384565\times10^{-6}>0.
\tag{5.10}
\]

Hence the frozen metric moves

\[
\boxed{
L:\quad \frac{2500000}{29210369}
\longrightarrow
\frac{3125000}{36511391}.
}
\]

No finite-size fit, simulation, or numerical asymptotic inference is involved in this movement.

## 6. Exact checker/output and self-check status

The proof-level finite algebra was executed from

`artifacts/hard7_2026-09-18/HARD7-03/theta_reoptimization_20260919T1824Z.py`

created at commit

`61c4cfb4df773db9b81fc9eff345cb17d1619f9e`.

Its exact output is archived at

`artifacts/hard7_2026-09-18/HARD7-03/theta_reoptimization_20260919T1824Z.out`

created at commit

`979b196d240b0dbb2c372fd65928794108a4b844`.

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

Both files were read back successfully from their returned commit SHAs. This is a **self-check**, not an independent closure audit. No closure audit is requested because the full source problem is not closed.

The checker also enforces the strongest internal anti-regression test available here: the parameterized formula at `theta=723/1250` is exactly equal, as a rational number, to the immutable 17:21Z all-pair `U_4` value.

## 7. B20: what remains after the pair route is exhausted

The adjacent-pair problem is no longer the next bottleneck at four steps: edge, near-edge, and centre pair classes are all inserted through exact conditional transforms before the Chernoff parameter is chosen. Further checker-only refinement of these same pair terms would violate the 90/10 instruction.

The remaining proof slack is upstream of (4.10): the deterministic inclusion/global-envelope treatment still does not resolve every **triple and higher-overlap** configuration exactly, and the whole shape argument still uses a finite four-layer block before subadditive iteration. The next useful question is therefore not “can the same rational be certified with more digits?” but one of:

1. isolate one unresolved triple-overlap class and integrate it exactly;
2. construct a monotone hierarchy showing exact overlap corrections increase the subtraction and quantify the first omitted level; or
3. deform the four-step block to a longer block only if the gain can be represented analytically rather than by brute-force enumeration.

The next planned method triple is **B4 / B13 / B30**: prove one remaining overlap class completely; identify a monotone correction hierarchy; localize one overlap order/scale at a time. Because this run moved the frozen metric, the Section-I stagnant-run counter resets rather than advancing.

## 8. Honest scope

This result is **PARTIAL**, not a solution of Seppäläinen Problem 4. It proves a stronger explicit plateau lower bound only for the frozen binary-disorder `K=2` case, using the previously established shape-to-flux transfer. It says nothing by itself about all `K>=2`, particle disorder, or arbitrary disorder laws. The source-level `K=1` theorem remains literature baseline and receives no new credit here.

```yaml
ledger_delta:
  track: HARD7-03
  canonical_claim: D0025
  source_key: disordered_asep_open_1999::problem_4
  status: PARTIAL
  metric: "rigorous lower bound L <= Delta_2(Q) for K=2, Q=(delta_1/2+delta_1)/2"
  before: "2500000/29210369 = 0.085586046516564..."
  after: "3125000/36511391 = 0.085589727326466..."
  movement: true
  methods: [3, 5, 20]
  idea_commit: b276f25799c59a20c63cdc48e72412d644bd7b17
  exact_checker: "artifacts/hard7_2026-09-18/HARD7-03/theta_reoptimization_20260919T1824Z.py"
  checker_commit: 61c4cfb4df773db9b81fc9eff345cb17d1619f9e
  exact_output: "artifacts/hard7_2026-09-18/HARD7-03/theta_reoptimization_20260919T1824Z.out"
  output_commit: 979b196d240b0dbb2c372fd65928794108a4b844
  exact_checker_tail: "ALL_EXACT_CHECKS_PASS = True"
  source_status: OPEN_BY_BOUNDED_SEARCH
  closure_claim: false
  stagnant_count_after: 0
  next_methods: [4, 13, 30]
```
