Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 3125000/36511391 -> 50000/584101`. Methods tried: B4 / B13 / B30.**

# HARD7-03 — structural zero-gap edge triple slack improves the D0025 plateau certificate

Status: **PARTIAL**. Seppäläinen Problem 4 remains open in its full source scope.

## 1. Continuity, ownership, required reads, and current status

This run resumes the exclusive canonical claim

`operations/claims/D0025.md`, owner `HARD7-03`, canonical key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`.

At run start I re-read the governing files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the D0025 claim/intake trail; the newest own checkpoint `20260919T1824Z__d0025-theta-reoptimization.md`; and the newest visible neighboring HARD7-02 / HARD7-04 state. HARD7-02 is on the distinct Campbell--O'Rourke heavy-tailed elliptic-matrix Question 1.9 line, and HARD7-04 is on the distinct heavy-tailed growing-random-graph/MST line. Repository-wide canonical-key search still names HARD7-03 as the D0025 owner; no release, collision, or posted equivalent was found. Shared root ledgers were not modified.

The primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1--15, Problem 4, arXiv `math/9906194`, DOI `10.11606/resimeusp.v4i1.74889`. The source asks whether disordered asymmetric finite-capacity `K`-exclusion exhibits the analogous phase transition, in particular a flat macroscopic-flux segment around density `K/2`.

A fresh bounded literature refresh on **19 September 2026** used the exact source title and the queries `disordered K-exclusion plateau K=2 site disorder asymmetric` and `partial exclusion random environment asymmetric flux site disorder K-exclusion`. It recovered the 1999 source, Floreani--Redig--Sau (`arXiv:1911.12564`), whose random environment is random maximal site occupancy, and Gonçalves--Hayashi--Sasada (`arXiv:2405.15142`), whose asymmetric partial-exclusion rates are in a different product-rate/gradient class. No theorem closing the exact iid site-rate `K>=2` residual surfaced. The honest label remains **OPEN_BY_BOUNDED_SEARCH**, not a worldwide-openness or novelty certificate.

The frozen case is unchanged:

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

The fixed source-relevant metric remains a rigorous lower bound `L <= Delta_2(Q)`.

### Runtime capability honesty

The exposed scheduler surface still has prompt/title, schedule/timing and enabled-state controls, but **no binding model selector, no reasoning-effort selector, no authenticated reasoning telemetry and no guaranteed run-duration field**. GPT-6/maximum is therefore only prompt-requested here. This run actually identifies as GPT-5.6 Sol; the reasoning level is unavailable and is recorded as `UNVERIFIED`.

Changing that requires a product/backend or other authorized scheduler interface that actually exposes model and effort controls; a repository edit cannot create them. The historical P26 `You cannot modify this task` response is an authorization/context restriction. The compliant workaround is modification from the owning/authorized account/workspace context or platform support/ownership remediation, never a duplicate schedule or permission bypass. No schedule was created, modified, reactivated, or disabled in this run.

## 2. Carry-in and the new obstruction chosen

The preceding checkpoint certified, at

\[
\theta=\frac{57343}{100000},
\]

the exact all-adjacent-pair four-step envelope

\[
U_{4,\mathrm{prev}}
=812.204849843116108\ldots
\]

and hence

\[
G_1(0)\le A_{\rm prev}:=\frac{36511391}{12500000}=2.92091128,
\]

so the inherited D0025 transfer gives

\[
L_{\rm prev}
=\frac{1}{4A_{\rm prev}}
=\frac{3125000}{36511391}
=0.085589727326466\ldots .
\tag{2.1}
\]

That run made the edge, near-edge and centre **pair-minimum** terms exact. The remaining four-step loss is in the triple-slack/global-envelope layer. This run does not re-optimize the pair terms or the Chernoff parameter. It isolates one omitted positive-measure triple configuration and computes it exactly.

Before writing the checker, the route was committed to

`artifacts/hard7_2026-09-18/HARD7-03/20260919T1921Z__idea-edge-boundary-triple-slack.md`

at commit

`c22c859e0e3f569cdbcab5e0ca3f6d45a3263d94`,

and read back successfully.

The previous run used B3/B5/B20. This run uses the distinct triple **B4/B13/B30**.

## 3. B4 — complete one omitted structural boundary class

Recall the exact conditional fresh-layer triple-slack kernel

\[
\Phi_\theta(u,v)
=\theta\int_0^\infty e^{\theta t}(1-e^{-t})
 e^{-(t-u)_+-(t-v)_+}\,dt,
\tag{3.1}
\]

where `u=S_{d-1}-S_d` and `v=S_{d+1}-S_d` are the two predecessor gaps. Put

\[
a=1-\theta,\qquad b=2-\theta,\qquad c=3-\theta,
\qquad \kappa=\frac{\theta}{bc}.
\]

The global envelope used earlier gives `Phi_theta(u,v)>=kappa exp(min(u,0)+min(v,0))`. Later mixed-sign work improves that on strict opposite-sign branches. However a structural boundary stratum survives at the outer edge because two consecutive sliding maxima can be *identically equal* on an event of positive probability.

Use the layer-two variables

\[
\begin{aligned}
Y_0&=\max(A_{-1},A_0,A_1)+B_0,\\
Y_1&=\max(A_0,A_1)+B_1,\\
Y_2&=A_1+B_2,
\end{aligned}
\tag{3.2}
\]

with all displayed fresh `B` variables independent unit exponentials. At the right edge,

\[
S_1=\max(Y_0,Y_1,Y_2),\qquad
S_2=\max(Y_1,Y_2),\qquad
S_3=Y_2.
\tag{3.3}
\]

On the strict event

\[
\mathcal E=\{Y_0>Y_2>Y_1\},
\tag{3.4}
\]

we have

\[
S_1=Y_0,\quad S_2=S_3=Y_2,
\quad u=Y_0-Y_2>0,\quad v=0.
\tag{3.5}
\]

This event was not in the previous strict mixed-sign edge correction, which used the disjoint ordering `Y_0>Y_1>Y_2`. It lies inside the local-minimum edge event and therefore had only the baseline `kappa` subtraction before this run.

For `u>=0`, splitting (3.1) at `t=u` gives exactly

\[
\boxed{
\Phi_\theta(u,0)
=\frac{\theta}{ab}(1-e^{-au})
+\frac{\theta}{bc}e^{-bu}.}
\tag{3.6}
\]

Hence the unused bonus over the old local-minimum baseline is

\[
\boxed{
B_0(u):=\Phi_\theta(u,0)-\kappa
=\frac{\theta}{ab}(1-e^{-au})
-\kappa(1-e^{-bu}).}
\tag{3.7}
\]

It is strictly positive for `u>0`: `B_0(0)=0` and

\[
B_0'(u)=\frac{\theta}{b}(e^{-au}-e^{-bu})>0
\qquad(u>0),
\tag{3.8}
\]

because `0<a<b`.

Thus one reflected edge contributes the exact positive correction

\[
C_{\rm edge}^{(0)}
=\mathbb E[e^{\theta Y_2}B_0(Y_0-Y_2);\mathcal E].
\tag{3.9}
\]

Define

\[
T_r=
\mathbb E\!\left[
 e^{\theta Y_2-r(Y_0-Y_2)};
 Y_0>Y_2>Y_1
\right],\qquad r\in\{0,a,b\}.
\tag{3.10}
\]

Then

\[
\boxed{
C_{\rm edge}^{(0)}
=\frac{\theta}{ab}(T_0-T_a)-\kappa(T_0-T_b).}
\tag{3.11}
\]

### Exact evaluation of `T_0,T_a,T_b`

Condition on the first layer and put

\[
s_0=\max(A_{-1},A_0,A_1),\qquad
s_1=\max(A_0,A_1),\qquad
s_2=A_1.
\]

Then `s_0>=s_1>=s_2`. Let `Delta=s_0-s_1`. Conditioning on `Y_2=y`, the lower event contributes

\[
\Pr\{Y_1<y\mid A\}=1-e^{s_1-y},\qquad y\ge s_1,
\]

while the weighted upper tail is

\[
\mathbb E[e^{-rY_0};Y_0>y\mid A]
=\begin{cases}
 e^{-rs_0}/(1+r),&s_1\le y<s_0,\\
 e^{s_0-(1+r)y}/(1+r),&y\ge s_0.
\end{cases}
\tag{3.12}
\]

Splitting the `y` integral at `s_0` and simplifying gives

\[
T_0\mid A
=e^{s_2}\left[
\frac{e^{-as_1}-e^{-as_0}}{ab}
+\frac{e^{s_1-bs_0}}{bc}
\right],
\tag{3.13}
\]

\[
T_a\mid A
=e^{s_2}\left[
\frac{\Delta e^{-as_0}}{b}
-\frac{a e^{-as_0}}{b^2}
+\frac{e^{s_1-bs_0}}{c}
\right],
\tag{3.14}
\]

and

\[
T_b\mid A
=e^{s_2}\left[
\frac{e^{-as_0}}{b}
-\frac{e^{s_1-bs_0}}{c}
\left(1+\Delta+\frac1c\right)
\right].
\tag{3.15}
\]

On each of the six strict order cones of `(A_{-1},A_0,A_1)`, every `s_j` is an order statistic and `Delta` is an order-statistic gap. With

\[
x_{\rm low}=z_1,\quad
x_{\rm mid}=z_1+z_2,\quad
x_{\rm high}=z_1+z_2+z_3,
\]

the iid exponential density is `exp(-3z_1-2z_2-z_3)`. Therefore every monomial in (3.13)--(3.15) integrates to a product of three reciprocal positive rational rates, and every `Delta` term is obtained by one derivative/equivalently one additional reciprocal gap rate. At rational `theta`, the calculation is exact rational arithmetic.

At the inherited

\[
\theta=\frac{57343}{100000},
\tag{3.16}
\]

the exact checker obtains

\[
T_0=0.764155668138375\ldots,
\quad
T_a=0.507884413065127\ldots,
\quad
T_b=0.282807974036226\ldots,
\tag{3.17}
\]

and

\[
\boxed{C_{\rm edge}^{(0)}=0.161752946554880\ldots>0.}
\tag{3.18}
\]

Reflection supplies exactly two such edge strata.

**B4 outcome: successful.** One previously omitted positive-measure triple class is now proved and integrated completely, not sampled.

## 4. B13 — monotone correction hierarchy and no double counting

The four-step deterministic max/min identity separates the adjacent-pair minima from the triple slack, so this correction does not overlap the all-pair improvement from the preceding run.

Within the triple term itself there is also no branch collision:

- the global separable envelope applies to all gap configurations;
- the existing strict mixed-sign edge improvement is localized to `Y_0>Y_1>Y_2`, equivalently the branch where the edge local-minimum condition fails;
- the new correction is localized to the disjoint event `Y_0>Y_2>Y_1`, where one sliding-window gap is structurally zero.

Consequently the hierarchy is monotone: each new term is a nonnegative additional subtraction from the previous upper envelope. No old certificate is weakened or replaced by an incomparable approximation.

**B13 outcome: successful.** The structural equality strata form a new correction level between the coarse local-minimum baseline and a fully exact triple kernel. This also identifies the next likely gains: the analogous near-edge and central local-minimum strata where one exterior winner creates a positive gap while the other side remains inherited from a shared window.

## 5. B30 — localize to the two reflected edges and move the metric

There are two reflected copies of (3.4), so the triple-slack subtraction increases by

\[
\Delta H=2C_{\rm edge}^{(0)}.
\tag{5.1}
\]

The preceding exact four-step envelope is

\[
U_{4,\rm prev}
=\frac{44218621253097337675520630615938362481617650843715385324269439414717371037400000000000000000000}
{54442695413156570473578553858609910677406260157304013873650482583987300880543061947950013587}.
\tag{5.2}
\]

Because the triple subtraction enters divided by `q=1-theta`, the refined envelope is

\[
U_{4,\rm new}
=U_{4,\rm prev}-\frac{2C_{\rm edge}^{(0)}}{1-\theta}
=811.446461083686813\ldots .
\tag{5.3}
\]

Thus the new structural idea lowers the four-step moment envelope by

\[
0.758388759429307\ldots .
\tag{5.4}
\]

No Chernoff-parameter reoptimization is used here. Keep (3.16) fixed and choose

\[
A_{\rm new}=\frac{584101}{200000}=2.920505.
\tag{5.5}
\]

Then

\[
x=4\theta A_{\rm new}=\frac{33494103643}{5000000000}.
\]

For

\[
S_{32}(x)=\sum_{k=0}^{32}\frac{x^k}{k!},
\]

the exact checker proves

\[
S_{32}(x)-U_{4,\rm new}>0
\tag{5.6}
\]

with decimal margin

\[
1.881805479520770\times10^{-3}.
\]

Since every omitted exponential-series term is positive,

\[
U_{4,\rm new}<S_{32}(x)<e^x=e^{4\theta A_{\rm new}}.
\tag{5.7}
\]

The already established four-block Chernoff/subadditive argument therefore yields

\[
\boxed{G_1(0)\le\frac{584101}{200000}=2.920505.}
\tag{5.8}
\]

Using the inherited D0025 transfer,

\[
\boxed{
\Delta_2(Q)\ge\frac1{4G_1(0)}
\ge\frac{50000}{584101}
=0.085601633963989\ldots .}
\tag{5.9}
\]

Hence the fixed metric moves rigorously from

\[
\boxed{
L:\quad
\frac{3125000}{36511391}
\longrightarrow
\frac{50000}{584101}.}
\tag{5.10}
\]

The exact gain is

\[
\frac{50000}{584101}-\frac{3125000}{36511391}
=\frac{36275000}{3046619999213}>0.
\tag{5.11}
\]

**B30 outcome: successful.** A single structural boundary class moves the source-relevant plateau certificate without another parameter fit or a longer brute-force block.

## 6. Exact artifact and self-check

The exact checker is

`artifacts/hard7_2026-09-18/HARD7-03/edge_boundary_triple_slack_20260919T1921Z.py`

at commit

`0876d5a630c2079068d7b71c4b8374ec9b46a9ca`.

Its executed output is archived as

`artifacts/hard7_2026-09-18/HARD7-03/edge_boundary_triple_slack_20260919T1921Z.out`

at commit

`7ee444a5dbb35b324636c5cf00156c8d9ba9db61`.

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

The idea, checker and output were each read back at their returned commit SHA. This is a **self-check**, not an independent closure audit. The source problem remains open, so no closure audit or paper folder is triggered.

## 7. Remaining obligation and next route

This run resets the stagnant counter because the frozen metric moved. The full source problem is still far broader than the binary `K=2` slice, and even within the four-step comparator the triple kernel is not globally exact.

The next non-bookkeeping target should be the **near-edge structural local-minimum strata**, not more digits on (5.9). Their geometry has a shared-window equality on one branch and an exterior winner on the other, so the same exact `Phi_theta(u,0)-kappa` mechanism should survive but the winner decomposition is larger. A second candidate is the central stratum where `Y_0` wins the middle window and one or both exterior endpoints exceed it.

Next planned method triple: **B15 / B18 / B25** — break the near-edge symmetry by branch, rewrite the zero-gap correction as a shifted-exponential operator kernel, and count the same winner event through two exact decompositions as an anti-double-counting check.

```yaml
ledger_delta:
  track: HARD7-03
  canonical_claim: D0025
  source_key: disordered_asep_open_1999::problem_4
  status: PARTIAL
  metric: "rigorous lower bound L <= Delta_2(Q) for K=2, Q=(delta_1/2+delta_1)/2"
  before: "3125000/36511391 = 0.085589727326466..."
  after: "50000/584101 = 0.085601633963989..."
  movement: true
  methods: [4, 13, 30]
  idea_commit: c22c859e0e3f569cdbcab5e0ca3f6d45a3263d94
  checker_commit: 0876d5a630c2079068d7b71c4b8374ec9b46a9ca
  output_commit: 7ee444a5dbb35b324636c5cf00156c8d9ba9db61
  exact_checker_tail: "ALL_EXACT_CHECKS_PASS = True"
  source_status: OPEN_BY_BOUNDED_SEARCH
  closure_claim: false
  stagnant_count_after: 0
  next_methods: [15, 18, 25]
```
