Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated as the applied reasoning setting.**

# NM13-03 / T03 — a-posteriori objective localization certifies exact-sphere upper endpoint 12.319635

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-03`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-07`  
Status: **PARTIAL / CANDIDATE_FULL COMPUTER-ASSISTED UPPER-BOUND IMPROVEMENT / PENDING LATER INDEPENDENT REVIEW**

## 1. Exact source target and compact handoff

The source problem is frozen exactly as required. Put `M=floor(alpha N)`, let `g_a` be iid `N(0,I_N)`, and seek `sigma` satisfying

`||sigma||_2 = sqrt(N)` exactly,

`<g_a,sigma> >= -sqrt(N)` for every `1<=a<=M`.

Equivalently, with `x=sigma/sqrt(N)`, seek `x` on the unit sphere and `Gx>=-1`. Nothing below uses a ball relaxation, radial rescaling, a smaller sphere, or a replica-only threshold.

The preceding NM13-03 reports proved: (i) a closed one-dimensional Gaussian kernel for the complete second-full lift, (ii) stationary-branch transport, and (iii) the exact envelope identity `dPsi/dalpha=-I/c>0`. The latest NM13-07 report then supplied a directed-interval weighted-contraction certificate at `alpha=12.75`, moving its worker-certified exact-sphere upper endpoint from `12.78437096216` to `12.75`. Its named remaining obstruction was to continue the stationary branch below `12.75`; it also recorded the concrete difficulty that near the NM13-03 `12.3197` scout, `Psi` changes sign across the small root-existence rectangle, so the old strategy “prove root existence and Psi>0 on the entire same box” fails.

This run attacks exactly that obstruction. It does not require Psi to have one sign on the entire contraction box.

## 2. Bounded primary-source status refresh, 20 September 2026

1. **El Alaoui--Sellke, arXiv:2010.15811.** Their model is exactly the iid Gaussian spherical perceptron on radius `sqrt(N)`. For negative `kappa`, their algorithm uses the conjectural FRSB/Parisi structure and outputs a feasible vector on radius `sqrt(qbar N)` with `qbar<1`; it does not by itself prove the exact full-radius satisfiability threshold at `kappa=-1`.
2. **Stojnic, arXiv:2312.16531.** This develops stationarized fully lifted RDT for the negative spherical perceptron and states a capacity characterization, but also states that substantial numerical work is needed for practical operation. NM13-07 has reconstructed the exact complete-second-lift source system and the sign condition on its comparison value. This run certifies that finite numerical layer at a sharper density; it does not re-prove the global fl-RDT comparison theorem from scratch.
3. **Montanari--Zhong--Zhou, arXiv:2110.15824.** This rigorously gives upper/lower threshold bounds and the LP threshold, not the exact `kappa=-1` threshold.
4. **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** This gives exact thresholds for a dimension-free Lipschitz algorithm class and explicitly distinguishes the non-algorithmic feasible-projection problem as still open.
5. A bounded fresh search found no later rigorous theorem plainly replacing the exact full-radius `kappa=-1` target. This is dated negative evidence, not a worldwide novelty certificate.

`POSTED.md` still separates the posted zero-margin/Ising perceptron results from this negative-margin continuous spherical target.

## 3. Consumed exact complete-second-lift reduction

Use the exact NM13-07 reduction

`q=p D^2`,

`gamma_p=(1-pD^2)/(2D(1-p))`,

`c=(1-D^2)/(D(1-p)(1-pD^2))`,

`B=c/(4 gamma)`.

For

`Y=sqrt(p) z + sqrt(1-p) H - 1`,

`f_{p,B}(z)=E_H exp[-B(Y_+)^2]`,

write `I=E_Z log f`, `I_B=partial_B I`, and `K=E_Z[(partial_z log f)^2]`. The interior stationary reconstruction is

`D^2 = K/[-4 p^2 B^2 I_B]`,

`alpha = -c^2/[4 B^2 I_B]`,

and the remaining scalar stationarity equation is

`H(p,B)=I-B I_B-4B^2 I_B(T_D/c_D)=0`.

The complete-second comparison value is

`Psi(p,B)=T(p,D,c/(4B))+c I/(4B^2 I_B)`.

Thus at a fixed source density `alpha0` define

`F(p,B)=(H(p,B), alpha(p,B)-alpha0)`.

A zero of `F` in the interior reconstruction domain is the complete-second stationary point used by the inherited source comparison theorem.

## 4. New lemma — a-posteriori objective localization

### Lemma NM03-T03-APOSTERIORI-OBJECTIVE

Let `F:Q->R^2` and `Psi:Q->R` be `C^1` on the weighted box

`Q = {x: ||D_r^{-1}(x-x_c)||_infty <= 1}`,

where `D_r=diag(r_1,r_2)` with positive radii. Let `A` be an invertible fixed `2 x 2` matrix and set

`T(x)=x-A F(x)`.

Assume

`q = sup_{x in Q} ||D_r^{-1}(I-A DF(x))D_r||_infty < 1`,

`eta = ||D_r^{-1} A F(x_c)||_infty <= 1-q`.

Then there is a unique zero `x_*` of `F` in `Q`, and in fact

`||D_r^{-1}(x_*-x_c)||_infty <= rho := eta/(1-q)`.                 (4.1)

If additionally

`|partial_1 Psi| <= L_1`, `|partial_2 Psi| <= L_2` on `Q`,

and `Psi(x_c)>=psi_0`, then

`Psi(x_*) >= psi_0 - rho(L_1 r_1 + L_2 r_2)`.                       (4.2)

In particular, strict positivity of the right side proves `Psi(x_*)>0` even when `Psi` takes both signs on the full root-existence box `Q`.

### Proof

For `x,y in Q`, the fundamental theorem of calculus gives

`T(x)-T(y)=int_0^1 [I-A DF(y+t(x-y))](x-y) dt`,

hence `T` is a contraction in the weighted sup norm with constant at most `q`. Also

`||D_r^{-1}(T(x)-x_c)||_infty`
` <= ||D_r^{-1}(T(x)-T(x_c))||_infty + ||D_r^{-1}(T(x_c)-x_c)||_infty`
` <= q + eta <= 1`.

Thus `T` maps `Q` into itself. Banach gives a unique fixed point `x_*`. Because `A` is invertible, `T(x_*)=x_*` is equivalent to `F(x_*)=0`.

For the sharper localization, use the fixed-point equation and the center:

`||D_r^{-1}(x_*-x_c)||_infty`
` <= ||D_r^{-1}(T(x_*)-T(x_c))||_infty + eta`
` <= q ||D_r^{-1}(x_*-x_c)||_infty + eta`.

Rearrangement proves (4.1). The line segment from `x_c` to `x_*` lies in the convex box `Q`. Applying the one-dimensional mean-value/integral formula to `Psi` along that segment and using (4.1) yields

`|Psi(x_*)-Psi(x_c)| <= L_1 |x_{*,1}-x_{c,1}| + L_2 |x_{*,2}-x_{c,2}|`
` <= rho(L_1 r_1+L_2 r_2)`.

This proves (4.2). QED.

### Why this is new and directly relevant

NM13-07's weighted contraction theorem established existence and uniqueness but required a separate whole-box positivity enclosure for `Psi`. That works at `12.75`, where the objective has a large margin. It fails near the complete-second zero: at the present box the rigorous whole-box enclosure is

`Psi(Q) subset [-1.794418569770963e-4, 1.794762427728123e-4]`,

so a direct sign proof is impossible from that box. The new lemma uses the contraction residual itself to localize the true root to a tiny fraction of the box and then transports only the center objective to that root. This is the named NM13-07 obstruction.

## 5. Application at alpha = 12.319635

Take

`alpha0 = 12.319635`,

`p_c = 0.6649244534165579`,

`B_c = 6.197655366469065`,

with box radii

`r_p=1e-7`, `r_B=4e-6`.

The executed checker uses the same directed interval architecture as the NM13-07 `12.75` certificate: `mpmath.iv` directed intervals for deterministic algebra, an independently coded directed-Decimal Gaussian CDF enclosure, composite Boole quadrature with an explicit sixth-derivative remainder, and explicit `|z|>10` Gaussian-tail bounds. The first derivatives are analytic; no finite-difference derivative is used in the certificate.

The center interval enclosures are

`H_c in [-4.632181608722411e-12, 4.631977210835852e-12]`,

`alpha_c in [12.3196349999636175, 12.3196350000364623]`,

`Psi_c in [2.308445653241911e-8, 2.309827416872840e-8]`.

On the entire box the checker proves

`H_p in [-0.03370146727424432,-0.02828455987858220]`,

`H_B in [0.0003284932328676832,0.0005043842197013973]`,

`alpha_p in [24.67157455631033,25.28760973547386]`,

`alpha_B in [-0.6024378692892906,-0.6008000232876709]`,

and the new objective-gradient enclosures

`Psi_p in [0.8701089577466267,0.8954131534826132]`,

`Psi_B in [-0.02136650282575422,-0.02115542237455933]`.

The frozen rational preconditioner is

`A = [[-7294853/100000, -504965/10000000],`
`     [-3028867/1000,   -3758826/1000000]]`.

Using the broad rational Jacobian enclosure

`H_p in [-0.034,-0.028]`,

`H_B in [0.00032,0.00051]`,

`alpha_p in [24.6,25.4]`,

`alpha_B in [-0.603,-0.600]`,

exact enumeration of all 16 vertices gives

`q <= 70497781/125000000 = 0.563982248`.

The rigorous center residual ceilings `|H_c|<4.7e-12`, `|alpha_c-alpha0|<3.7e-11` give, by exact rational arithmetic,

`eta <= 7187375731/2000000000000 = 0.0035936878655 < 1-q`.

Therefore the stationary root is unique in the box, and Lemma (4.1) sharpens its location to

`rho <= 7187375731/872035504000 = 0.008242067780533853`

of the full weighted radius.

For the objective, the rational derivative caps

`L_p=0.896`, `L_B=0.0214`

give

`L_p r_p + L_B r_B = 219/1250000000 = 1.752e-7`.

The center bound contains the rational lower value

`psi_0 = 577/25000000000 = 2.308e-8`.

Consequently (4.2) gives the exact positive lower bound at the **true stationary root**

`Psi(x_*) >= 23584189005311/1090044380000000000000`

`             = 2.163598972485047e-8 > 0`.                            (5.1)

This succeeds even though the direct whole-box `Psi` interval crosses zero by four orders of magnitude more than the final positive margin.

The same interval box keeps all reconstructed source parameters interior:

`D in [0.6466101610077578,0.6466247836349100]`,

`q=pD^2 in [0.2780079975196880,0.2780206551913525]`,

`gamma_p in [1.666094255142576,1.666162137636787]`,

`c in [3.719659086779107,3.719931529382793]`,

`gamma in [0.1500428979246351,0.1500540813536483]`.

Thus the root lies on the exact source-matched interior complete-second branch.

## 6. Source-level implication and before/after

Consuming NM13-07's exact equivalence between `F=0` and complete-second stationarity, and the inherited stationarized fl-RDT source comparison implication, the stationary root at `alpha=12.319635` together with (5.1) gives a complete-second UNSAT certificate for the exact spherical model. Hence the worker proof candidate yields

`alpha_c(-1) <= 12.319635`.

The retained lower endpoint remains `alpha_L=6.30297437506`.

### Original-problem source metric

**Before this run (latest NM13-07 worker-certified candidate):**

`[6.30297437506, 12.75]`, width `6.44702562494`.

**After this run:**

`[6.30297437506, 12.319635]`, width `6.01666062494`.

Upper-endpoint and bracket-width gain:

`12.75 - 12.319635 = 0.430365`.

Relative to NM13-03's immediately preceding numerical-only candidate `12.3197`, the endpoint improves by `0.000065` and, more importantly, is upgraded from numerical support to a directed-interval computer-assisted proof candidate at `12.319635`.

This is **CANDIDATE_FULL pending later independent review**, not a claim of publication-level certification. The exact threshold remains open.

### Demonstrated mechanism gain

Before: near the complete-second comparison zero, `Psi` changes sign on every practically useful root-existence rectangle, so the NM13-07 whole-box objective strategy cannot certify a sharp endpoint.

After: the a-posteriori localization lemma needs only contraction, a positive center objective, and a gradient enclosure. It certifies objective positivity at the true root even when `Psi` has both signs on the surrounding box. This removes the named obstacle without branch-by-branch continuation or a changed source model.

## 7. Preserved failed routes and new residual obstruction

Preserved failures:

1. **Whole-box objective positivity** fails at the sharp endpoint: the rigorous `Psi(Q)` interval straddles zero.
2. **Dense branch continuation as a proof** is unnecessary for this endpoint and would require many overlapping boxes; the new lemma bypasses that burden.
3. Smaller-radius/ball relaxations and replica/FRSB numerical predictions remain non-solutions to the exact sphere problem.

The present complete-second route is now numerically at its natural comparison zero: the high-accuracy scout from the preceding run put the `H=0,Psi=0` crossing at approximately `alpha=12.3196343465869`. The certified endpoint `12.319635` is only about `6.53e-7` above that scout. Therefore polishing this same second-full box cannot produce a substantial further source gain. The next material attack should change mechanism: derive a third-full (next lifting level) a-posteriori comparison reduction or a genuinely different overlap/feasibility inequality, rather than spend future runs shaving digits from the second-full endpoint.

## 8. Essential executed artifacts

Directed-interval certificate source:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_aposteriori_alpha12319635.py`

creation commit:

`2901852ee2b334fdc1c6e4e39186d095894301ec`.

Archived actual output:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_aposteriori_alpha12319635.out`

creation commit:

`108b48bbdcf6f50126561b45f4af1c5d704757df`.

The output ends

`CERTIFIED_ALPHA_U 12.319635`

`ALL_APOSTERIORI_CONTRACTION_CHECKS_PASS`.

No peer file, shared root ledger, schedule, permission, workflow, email, Drive object, paid resource, public resource, or POSTED item was modified.

```yaml
ledger_delta:
  worker: NM13-03
  parent: T03
  target: "negative spherical Gaussian perceptron, kappa=-1, iid constraints, exact radius sqrt(N)"
  status: "PARTIAL / CANDIDATE_FULL / COMPUTER-ASSISTED UPPER-BOUND IMPROVEMENT / INDEPENDENT REVIEW PENDING"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
  source_metric: "upper endpoint and width of supported exact-sphere threshold bracket"
  before:
    alpha_L: "6.30297437506"
    alpha_U: "12.75"
    width: "6.44702562494"
  after:
    alpha_L: "6.30297437506"
    alpha_U: "12.319635"
    width: "6.01666062494"
  source_movement:
    upper_endpoint_gain: "0.430365"
    width_gain: "0.430365"
  new_lemma: "NM03-T03-APOSTERIORI-OBJECTIVE"
  certificate:
    q: "70497781/125000000"
    eta: "7187375731/2000000000000"
    rho: "7187375731/872035504000"
    weighted_objective_gradient_cap: "219/1250000000"
    center_Psi_lower: "577/25000000000"
    true_root_Psi_lower: "23584189005311/1090044380000000000000"
  mechanism_gain: "objective positivity at the true stationary root no longer requires Psi>0 on the whole contraction box"
  residual_obstruction: "complete-second comparison zero is essentially reached; substantial next gain requires next lifting level or a different overlap/feasibility comparison"
  next_attack: "third-full a-posteriori reduction or distinct source-valid overlap/feasibility inequality; do not polish second-full digits"
  artifacts:
    code_commit: "2901852ee2b334fdc1c6e4e39186d095894301ec"
    output_commit: "108b48bbdcf6f50126561b45f4af1c5d704757df"
```
