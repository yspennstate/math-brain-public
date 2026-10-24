Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-07 / T03 — interval contraction certificate moves the exact-sphere upper endpoint to 12.75

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03` comparison / feasibility theory  
Status: **PARTIAL / SOURCE BRACKET STRICTLY IMPROVED / COMPUTER-ASSISTED UPPER-BOUND THEOREM PENDING LATER INDEPENDENT REVIEW**

## 1. Short handoff and exact source target

The preceding NM13-07 reports reduced complete second-full stationarity to two scalar variables `(p,B)`, derived an analytic moment/Jacobian compiler, and then built a directed-interval Gaussian quadrature engine. The last substantive report still left the source bracket unchanged because it had only point/corner enclosures on a relatively large Poincare--Miranda rectangle and lacked continuum control.

A subsequent essential artifact, created before this report in the same worker namespace, executes a materially stronger route: a **tiny weighted-box interval contraction certificate** around the `alpha=12.75` stationary scout. It encloses the entire Jacobian on the box, not merely corners. This report checks that artifact against the deterministic contraction theorem and the source-matched complete-second-lift reduction, and records the first source-level threshold movement on this route.

The source model is unchanged and exact: `M=floor(alpha N)`, independent `g_a ~ N(0,I_N)`, `||sigma||_2=sqrt(N)` exactly, and `<g_a,sigma> >= -sqrt(N)` for every `a<=M`, with fixed `alpha` and `N -> infinity`. Equivalently, for `x=sigma/sqrt(N)` one seeks `x in S^{N-1}` with `Gx>=-1`. No ball relaxation, smaller sphere, post-hoc radial normalization, or replica-only endpoint is used below.

## 2. Primary-source hypotheses and present proof status

1. **El Alaoui--Sellke, arXiv:2010.15811.** Their model is precisely the iid Gaussian spherical perceptron on radius `sqrt(N)`. For `kappa<0`, their algorithm assumes access to the Parisi/FRSB structure and produces a feasible vector on radius `sqrt(qbar N)` with `qbar in (0,1)`, not a theorem giving the exact full-radius satisfiability threshold. That result therefore cannot substitute for T03.
2. **Stojnic, arXiv:2312.16531.** This treats the negative spherical perceptron by stationarized fully lifted random duality theory (fl RDT), states a capacity characterization through the full-lifting machinery, and explicitly notes that practical use requires substantial numerical work. The repository's preceding R14/NM13-07 derivations matched the complete second-full source system, reduced its stationarity equations to `(p,B)`, and identified the sign condition on the comparison value needed for the UNSAT implication. The computation below supplies the previously missing rigorous finite numerical layer at `alpha=12.75`.
3. **Montanari--Zhong--Zhou, arXiv:2110.15824.** Their rigorous work supplies the retained lower threshold/LP success endpoint but does not identify the exact `kappa=-1` threshold.
4. **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** This gives exact algorithmic thresholds for a dimension-free Lipschitz algorithm class and explicitly distinguishes the non-algorithmic problem of characterizing all feasible projections as still open.
5. A bounded fresh search found no later rigorous theorem plainly replacing the full-radius `kappa=-1` bracket used here. This is dated negative evidence only, not a worldwide priority certificate. `POSTED.md` continues to separate the posted zero-margin/Ising perceptron work from this negative-margin continuous spherical target.

## 3. Original source metric — strict movement

The repository-supported rigorous bracket entering this run was

`alpha_L = 6.30297437506`, `alpha_U = 12.78437096216`, `W = 6.48139658710`.

The lower endpoint is unchanged. The new complete-second-lift certificate proves the upper endpoint `12.75`.

**Before:** `[6.30297437506, 12.78437096216]`, width `6.48139658710`.

**After:** `[6.30297437506, 12.75]`, width `6.44702562494`.

Thus the rigorous upper endpoint and bracket width both improve by

`12.78437096216 - 12.75 = 0.03437096216`.

This is a source-level gain for the exact sphere problem. T03 remains **OPEN / PARTIAL** because the exact threshold is still unknown.

## 4. Consumed exact two-scalar reduction

Retain

`q=p D^2`,

`gamma_p=(1-pD^2)/(2D(1-p))`,

`c=(1-D^2)/(D(1-p)(1-pD^2))`,

`B=c/(4 gamma)`.

For `Y=sqrt(p) z + sqrt(1-p) H - 1` and `f_{p,B}(z)=E_H exp[-B(Y_+)^2]`, write `I=E_Z log f`, `I_B=partial_B I`, and `K=E_Z (partial_z log f)^2`.

The interior complete-second-lift stationary system reconstructs

`D^2 = K/[-4 p^2 B^2 I_B]`,

`alpha = -c^2/[4 B^2 I_B]`,

and is equivalent to the remaining scalar stationarity equation

`H(p,B)=I-B I_B-4 B^2 I_B A_0(p,D)=0`,

where `A_0=T_D/c_D`. The comparison value is

`Psi=T+c I/(4 B^2 I_B)`.

At fixed density `alpha_0=12.75`, define `F(p,B)=(H(p,B), alpha(p,B)-12.75)`. A zero of `F` in the interior reconstruction domain is exactly a complete second-full stationary point at source density `12.75`.

## 5. Deterministic weighted contraction theorem

Let `x_c in R^2`, let `D_r=diag(r_p,r_B)` with positive radii, and define `Q={x: ||D_r^{-1}(x-x_c)||_infty <= 1}`. For a fixed invertible matrix `A`, set `T(x)=x-AF(x)`.

If

`q_* := sup_{x in Q} ||D_r^{-1}(I-A DF(x))D_r||_infty < 1`

and

`eta := ||D_r^{-1} A F(x_c)||_infty <= 1-q_*`,

then `T` maps `Q` to itself and is a contraction in the weighted sup norm. Banach's fixed-point theorem gives a unique `x_* in Q` with `F(x_*)=0`. The proof is immediate from

`T(x)-T(y)=int_0^1 [I-A DF(y+t(x-y))](x-y) dt`.

## 6. New executed whole-box certificate at alpha=12.75

The executed source is

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_alpha1275_interval_contraction.py`

and the archived output is

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_alpha1275_interval_contraction.out`.

The script uses directed interval arithmetic for deterministic algebra, a directed-Decimal Gaussian-CDF enclosure (alternating integrated series on bounded arguments and two-sided Mills bounds in the far tail), composite Boole quadrature with an explicit sixth-derivative remainder, and explicit `|z|>10` Gaussian-tail bounds. The first-Jacobian formulas are analytic; no finite-difference derivative enters the certificate.

Take

`p_c = 0.6457670646889506`, `B_c = 4.929229200895245`,

with weighted radii

`|p-p_c| <= 1e-7`, `|B-B_c| <= 4e-6`.

The fixed rational preconditioner is

`A = [[-1601/20, -493/12500],[-60418/25,-5789/2500]]`,

whose determinant is `112560429/1250000 != 0`.

### Center residuals

The output proves

`H(p_c,B_c) in [-1.212554436371290612245951e-12, 1.213143563012573590500445e-12]`,

`alpha(p_c,B_c) in [12.749999999987972073128, 12.75000000001195276213347]`,

and

`Psi(p_c,B_c) in [0.01520099346505100196578118, 0.01520099346927964524582684]`.

### Whole-box Jacobian

On the entire weighted box it proves

`H_p in [-0.02711212089683223426994377, -0.024310952952744879456086]`,

`H_B in [0.0003603288123614667298578366, 0.0005154692141991121554988643]`,

`alpha_p in [26.74152424955626507137499, 26.92985184474885288001005]`,

`alpha_B in [-0.8895666579112775606815714, -0.8881978795161755360175899]`.

These are contained in the rational compiler box

`H_p in [-0.028,-0.024]`, `H_B in [0.0003,0.0006]`, `alpha_p in [24,30]`, `alpha_B in [-1,-0.8]`.

Exact enumeration of its 16 Jacobian vertices gives

`q_* <= 23849/25000 = 0.95396`,

hence `1-q_* >= 1151/25000 = 0.04604`.

Using the rigorous center residual ceilings `2e-12` and `2e-11`, exact rational arithmetic gives

`eta <= 201111/125000000 = 0.001608888 < 1-q_*`.

Therefore there is a **unique genuine zero** `(p_*,B_*)` of `H=0`, `alpha=12.75` in the tiny box.

### Interior-domain and objective checks

The same whole-box computation gives

`D in [0.6601156813783433425966759, 0.6601281233340372364542935]`,

`q=pD^2 in [0.2813947067008617125, 0.28140540149079534127]`,

`gamma_p in [1.5365144784472735004,1.5365671747016654077]`,

`c in [3.3577559597302708721,3.3579688747027253263]`,

`gamma in [0.17029808810427333934,0.17030916309589850041]`.

Thus the reconstruction stays in the required interior branch. Moreover

`Psi in [0.0150497744619429886066833, 0.01535220391179542860104646]`

on the entire box, so in particular `Psi(p_*,B_*)>0`.

The archived output ends

`CERTIFIED_ALPHA_U 12.75`,

`CERTIFIED_PSI_LOWER 0.0150497744619429886066833`,

`ALL_INTERVAL_CONTRACTION_CHECKS_PASS`.

This is a worker computer-assisted certificate, not an independent audit or proof-assistant formalization.

## 7. Source-level implication

The source-matched complete-second-lift reduction and the stationarized fl-RDT feasibility theorem require the stationary lifting parameters, interior reconstruction, and positive comparison value supplied above. Hence the certified zero at `alpha=12.75` supplies the complete second-full UNSAT certificate for the negative spherical perceptron at `kappa=-1` with exact radius `sqrt(N)`.

Thus the model is asymptotically UNSAT at density `12.75`. Constraint monotonicity then gives

`alpha_c(-1) <= 12.75`.

Combining with the retained LP-success lower endpoint yields

`6.30297437506 <= alpha_c(-1) <= 12.75`.

This is the claimed strict bracket improvement; it does not determine the exact threshold.

## 8. Mechanism gain versus source movement

**Source movement:** `alpha_U: 12.78437096216 -> 12.75`, width `6.48139658710 -> 6.44702562494`.

**Mechanism gain:** the complete-second-lift route now has an actual stationary point, not merely a scout or corner signs. Tiny-box preconditioning preserves the correlations that destroyed the previous large-box interval route, while the whole-box `Psi` enclosure supplies a rigorous positive anchor. This anchor is exactly what NM13-03's envelope identity can transport to lower densities once stationary-branch existence is certified there.

## 9. Preserved failures, residual obstruction, next attack

Preserved failures: naive whole-rectangle interval evaluation loses correlations; direct `Psi>0` on an endpoint root rectangle fails near the companion `12.3197` scout because off-branch corners can have negative `Psi`; smaller-radius, ball-relaxed, and replica-only calculations do not count for this target.

Residual obstruction: improve `12.75` further. NM13-03 proved on a smooth interior stationary branch that

`d Psi/d alpha = -I/c > 0`.

The next attack should be **certified branch continuation** from the now-rigorous `12.75` anchor: cover a short density interval with overlapping tiny weighted contraction boxes, certify one stationary root per box, and outward-enclose `-I/c` on each cell. A conservative first endpoint such as `12.70` or `12.60` should be attempted before pushing toward the supported `12.3197` scout.

## 10. Essential artifact provenance

- `t03_alpha1275_interval_contraction.py`: latest commit `b69435d8172f1a91b11dfc791e3dd2c0afa77d03`.
- `t03_alpha1275_interval_contraction.out`: creation commit `4e57673f046ef574d1abfb774e0ed38134d15243`.

The artifact code/output existed before this report and were not overwritten here. No peer file, shared root ledger, schedule, access control, workflow, email, Drive object, paid resource, public resource, or POSTED item was modified.

```yaml
ledger_delta:
  worker: NM13-07
  parent: T03
  target: "negative spherical Gaussian perceptron, kappa=-1, exact radius sqrt(N)"
  status: "PARTIAL / SOURCE OPEN / STRICT RIGOROUS UPPER-BOUND IMPROVEMENT"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
  source_metric: "rigorous asymptotic threshold bracket width alpha_U-alpha_L"
  certified_before:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  certified_after:
    alpha_L: "6.30297437506"
    alpha_U: "12.75"
    width: "6.44702562494"
  source_movement:
    upper_endpoint_gain: "0.03437096216"
    width_gain: "0.03437096216"
  mechanism_gain:
    - "directed interval whole-box Jacobian certificate"
    - "exact rational weighted contraction q <= 23849/25000"
    - "exact rational residual eta <= 201111/125000000 < 1-q"
    - "unique complete-second-lift stationary zero at alpha=12.75"
    - "whole-box Psi lower bound 0.0150497744619429886066833"
  artifacts:
    code_commit: "b69435d8172f1a91b11dfc791e3dd2c0afa77d03"
    output_commit: "4e57673f046ef574d1abfb774e0ed38134d15243"
  residual_obstruction: "certify continuation of the stationary branch below 12.75 and transport Psi positivity; exact threshold still unknown"
  next_attack: "overlapping tiny contraction boxes plus NM13-03 envelope transport dPsi/dalpha=-I/c, initially toward 12.70 or 12.60"
```
