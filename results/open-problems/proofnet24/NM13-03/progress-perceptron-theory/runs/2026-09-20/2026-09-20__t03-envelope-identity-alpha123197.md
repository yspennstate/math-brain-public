Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-03 / T03 — stationary envelope identity; supported exact-sphere upper candidate 12.3197

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-03`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-07`  
Status: **PARTIAL / NEW EXACT ENVELOPE THEOREM / SUPPORTED SOURCE-LEVEL CANDIDATE IMPROVED 12.33 -> 12.3197 / OUTWARD ENCLOSURE STILL PENDING**

## 1. Compact continuity handoff and exact source problem

The preceding NM13-03 run proved a stationary-branch transport theorem and numerically continued the complete second-full stationary branch from `alpha=12.75` to `12.33`, producing a supported source-level upper candidate `12.33`. NM13-07's newest substantive T03 report supplies the exact tilted-moment tower and first-Jacobian compiler for the same source-matched two-scalar system. The inherited rigorous source bracket is still

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`.

This run preserves the failed direct-box and derivative-ratio routes and changes the comparison mechanism rather than repeating them.

The source model remains exactly:

- `M=floor(alpha N)`;
- `g_a iid N(0,I_N)`;
- `||sigma||_2=sqrt(N)` exactly;
- `<g_a,sigma> >= -sqrt(N)` for all `a<=M`;
- fixed `alpha`, `N -> infinity`.

Equivalently `x=sigma/sqrt(N)` lies on the unit sphere and satisfies `Gx>=-1`. No ball relaxation, smaller sphere, or replica-only prediction is used as a source implication.

## 2. Current primary-source status, bounded 20 September 2026 refresh

1. **El Alaoui--Sellke, arXiv:2010.15811.** Their model is exactly the iid Gaussian spherical perceptron on radius `sqrt(N)`. For `kappa<0`, the algorithmic construction is tied to the conjectural FRSB/Parisi structure and outputs on radius `sqrt(qbar N)` with `qbar<1`; it does not by itself prove the exact full-radius satisfiability threshold at `kappa=-1`.
2. **Stojnic, arXiv:2312.16531.** This develops stationarized fully lifted RDT for the negative spherical perceptron and reports concrete finite-level capacity values, while explicitly stating that making the framework fully operational requires substantial numerical work. The repository therefore continues to require an actual stationarity/comparison certificate before treating a new numerical endpoint as rigorous.
3. **Montanari--Zhong--Zhou, arXiv:2110.15824.** This is rigorous and proves upper/lower bounds and the LP threshold, but does not identify the exact `kappa=-1` threshold.
4. **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** This gives exact algorithmic projection-pursuit thresholds for a dimension-free Lipschitz algorithm class and explicitly distinguishes the non-algorithmic feasible-projection problem as still open.
5. Later full-RSB / jamming calculations such as arXiv:2410.06717 and arXiv:2503.11761 remain valuable structural/numerical guides but are ansatz-based and are not substituted here for a rigorous full-radius comparison certificate.

A bounded fresh search found no later rigorous theorem plainly replacing the exact full-radius `kappa=-1` bracket above. This is dated negative evidence, not a worldwide novelty certificate. `POSTED.md` exclusions for the owner's zero-margin/Ising perceptron work remain distinct from this continuous negative-margin spherical target.

## 3. Consumed exact second-full reduction

Use NM13-07's source-matched notation

`q=p D^2`,

`gamma_p=(1-pD^2)/(2D(1-p))`,

`c=(1-D^2)/(D(1-p)(1-pD^2))`,

`B=c/(4 gamma)`.

For

`Y=sqrt(p) z + sqrt(1-p) H - 1`,

`f_{p,B}(z)=E_H exp[-B (Y_+)^2]`,

put

`I(p,B)=E_Z log f_{p,B}(Z)`.

The complete second-full stationary reduction gives an interior branch through two equations

`H(p,B)=0`, `A(p,B)=alpha`,

with algebraic reconstruction of `D,c,gamma` and source comparison value

`Psi(p,B)=T(p,D,c/(4B)) + c I/(4B^2 I_B)`.

Before eliminating `alpha`, the same objective is

`F(p,D,gamma;alpha)=T(p,D,gamma)-alpha I(p,B)/c(p,D)`,

and complete second-full stationarity is stationarity of `F` in the non-density variables.

The previous NM13-03 transport identity was

`dPsi/dalpha=(H_p Psi_B-H_B Psi_p)/(H_p A_B-H_B A_p)`.

That identity is exact but expensive to certify because it imports the entire first Jacobian plus a determinant. This run proves that all of those derivatives cancel on a true stationary branch.

## 4. New theorem — exact stationary envelope identity

### Theorem NM03-T03-ENVELOPE

Let `alpha -> (p(alpha),D(alpha),gamma(alpha))` be a `C^1` interior branch of complete second-full stationary points for the source-matched negative spherical perceptron functional

`F(p,D,gamma;alpha)=T(p,D,gamma)-alpha I(p,B)/c(p,D)`,

with `0<p,D<1`, `gamma>0`, hence `B=c/(4gamma)>0`. Let

`Psi(alpha)=F(p(alpha),D(alpha),gamma(alpha);alpha)`.

Then

`boxed: dPsi/dalpha = - I(p(alpha),B(alpha)) / c(p(alpha),D(alpha)).`     (4.1)

Moreover

`I<0`, `c>0`,

so

`boxed: dPsi/dalpha > 0.`                                                (4.2)

Consequently `Psi` is strictly increasing in density on every such connected stationary branch. If `[a_1,a_0]` is a branch interval and `L_j` are upper bounds for `-I/c` on a partition `a_1=t_0<...<t_m=a_0`, then

`Psi(a_1) >= Psi(a_0) - sum_j L_j (t_j-t_{j-1}).`                         (4.3)

In particular a positive right-hand side proves `Psi(a_1)>0` without requiring `Psi` to be positive on any two-dimensional root rectangle around the endpoint.

### Proof

Because the branch consists of complete stationary points,

`F_p=F_D=F_gamma=0`

at every point of the branch. Therefore the chain rule gives

`d/dalpha F(p(alpha),D(alpha),gamma(alpha);alpha)`
` = F_p p' + F_D D' + F_gamma gamma' + partial_alpha F`
` = partial_alpha F`
` = -I/c`.

This is (4.1). It is an envelope-theorem cancellation and does not require inversion of the stationary Jacobian.

For every fixed `z`, the conditional Gaussian variable `Y` has positive probability of lying in `(0,infinity)`. Since `B>0`,

`0 < exp[-B(Y_+)^2] <= 1`

and the inequality is strict on an event of positive probability. Hence

`0 < f_{p,B}(z) < 1`,

so `log f_{p,B}(z)<0` for every finite `z`, and therefore `I=E log f<0`. On the interior branch `0<p,D<1`, the displayed algebraic formula for `c` has positive numerator and denominator, so `c>0`. Thus `-I/c>0`, proving (4.2). Integrating (4.1) over each partition cell gives (4.3). QED.

### Why this is a genuine new comparison gain

NM13-07's exact first-Jacobian compiler reduced the derivative problem to one-dimensional Gaussian moments, but the predecessor transport theorem still needed `H_p,H_B,A_p,A_B,Psi_p,Psi_B` and a determinant. The envelope identity reduces **objective transport to one scalar Gaussian expectation `I` plus the algebraic `c`**. Root existence still needs a stationary certificate, but comparison positivity no longer needs any objective derivatives or Jacobian quotient.

This is precisely useful near the source endpoint, where the endpoint root rectangle is so small that `Psi` itself changes sign across the rectangle.

## 5. Application — source-level candidate `12.33 -> 12.3197`

I continued the same complete second-full stationary branch from `alpha=12.75` down to

`alpha_target = 12.3197`.

This is numerical support, not outward-rounded certification.

Across 862 continuation points, the reconstructed branch stayed in

`p in [0.6457670646889668, 0.6649211712155717]`,

`B in [4.929229200895691, 6.197411053061391]`,

and the exact envelope rate evaluated numerically in

`-I/c in [0.035275251866513, 0.03534130609091377]`.

Gauss--Hermite orders 200 and 260 differed by at most `3.91e-14` on the recorded core quantities. At 13 independently re-solved branch points, a central finite difference of `Psi(alpha)` agreed with the new exact formula `-I/c` to at most `4.89e-11`.

The target stationary reconstruction is

`p*=0.6649211712155717`,

`B*=6.197411053061391`,

`D*=0.6466197629671858`,

`I*=-0.1314538170079934`,

`c*=3.719729832885889`,

`Psi*=2.320166148650493e-6 > 0`.

Thus the direct source comparison value remains positive at `12.3197`.

### Exact rational piecewise transport arithmetic

A single global rounded cap on `-I/c` over the entire interval is too wasteful this close to the zero and gives no positive transport margin. I therefore partitioned `[12.3197,12.75]` into eight `0.05` cells plus the final `0.0303` cell. Dense numerical scouting supports the following deliberately rounded-up caps:

- `[12.3197,12.3697]`: `0.0353414`;
- `[12.3697,12.4197]`: `0.0353414`;
- `[12.4197,12.4697]`: `0.0353402`;
- `[12.4697,12.5197]`: `0.0353364`;
- `[12.5197,12.5697]`: `0.0353302`;
- `[12.5697,12.6197]`: `0.0353218`;
- `[12.6197,12.6697]`: `0.0353113`;
- `[12.6697,12.7197]`: `0.0352989`;
- `[12.7197,12.75]`: `0.0352846`.

Using the rounded anchor hypothesis

`Psi(12.75) >= 152009/10^7 = 0.0152009`,

the exact rational transport loss from these caps is

`760010169 / 50000000000 = 0.01520020338`,

so theorem (4.3) gives, **conditional on outward certification of the listed scalar caps and the anchor**, the exact positive lower margin

`Psi(12.3197) >= 34831 / 50000000000 = 6.9662e-7 > 0`.                  (5.1)

The direct reconstructed value `2.3201661e-6` is larger, as expected.

## 6. Named NM13-07 obstruction: endpoint box now demonstrates why envelope transport matters

Around the `12.3197` numerical root I used

`p in [p*-1e-5,p*+1e-5]`,

`B in [B*-0.00055,B*+0.00055]`.

The opposite corner signs needed by the inherited monotone-face root theorem are numerically robust:

- lower-left: `H=+8.09196e-8`, `A-12.3197=+8.11348e-5`;
- upper-right: `H=-8.09515e-8`, `A-12.3197=-8.10928e-5`.

A `9 x 9` derivative scout gives

`H_B >= 4.16366031e-4`,

`A_p >= 24.9782850`,

with GH200/GH260 derivative discrepancy at most `1.25e-9`.

But `Psi` is **not** positive on the whole rectangle: for example the upper-left corner has

`Psi=-1.82006e-5`,

and the upper-right corner has

`Psi=-5.45627e-7`.

Therefore the old strategy "certify root existence and certify `Psi>0` everywhere on the same rectangle" fails at this sharper endpoint even numerically. The new theorem removes exactly that obstruction: once the true root branch is enclosed, objective positivity is transported along the branch from the positive anchor using only `-I/c`.

This is a material mechanism change, not another tighter auxiliary constant.

## 7. Original-problem before/after versus mechanism gain

### Independently certified original T03 bracket

**Before:**

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

**After:**

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

No outward-rounded continuum certificate was completed in this run, so I do not silently promote the supported candidate to the certified ledger.

### Supported source-level CANDIDATE_FULL bracket

**Before:**

`[6.30297437506, 12.33]`, width `6.02702562494`.

**After:**

`[6.30297437506, 12.3197]`, width `6.01672562494`.

This improves the prior supported source upper endpoint by

`0.0103`,

and lies

`0.46467096216`

below the current independently certified upper endpoint. This is a bound candidate for the original exact-radius Gaussian spherical problem, not an auxiliary moment or changed-radius value.

### Demonstrated mechanism gain

Before: comparison positivity transport required six first derivatives and a stationary Jacobian determinant, while direct `Psi>0` on an endpoint root box becomes false near the second-full zero.

After: at a true complete stationary point,

`dPsi/dalpha=-I/c>0`

exactly. Objective transport therefore requires only the scalar log-partition expectation `I` and algebraic `c`, and it remains applicable even when `Psi` changes sign away from the true root inside the root-existence rectangle.

## 8. Failed routes preserved this run

1. **Direct endpoint-box positivity:** fails already at `alpha=12.3197`; two corners of the small root rectangle have negative `Psi`.
2. **One global slope cap:** the single rounded cap `-I/c<=0.035342` over the full `0.4303` density interval wastes enough margin to lose positivity. Piecewise transport repairs this without changing the source model.
3. I did not reopen the exhausted one-parameter/partial-lift route, MZZ weighted-second-moment family, sphere-net route, smaller-radius/ball relaxation, or replica/full-RSB prediction as a proof.

This is the third substantive NM13-03 T03 run, but it has a demonstrated mechanism and source-candidate gain, so the three-unchanged trigger does not fire.

## 9. Essential executed artifacts

Checker source:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_envelope_alpha123197.py`

creation commit:

`e79526a6f07be1a5158cc8bb2d9507585fc84960`.

Archived actual output:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_envelope_alpha123197.out`

creation commit:

`ec9f8016f3b15d76183363c2e27cd76cd6e9bfc4`.

The output ends `ALL_NUMERICAL_SUPPORT_CHECKS_PASS`. It labels `12.3197` as a **supported candidate**, not as independently certified.

## 10. Residual rigorous obligation and next attack

The remaining certification problem is now sharply split:

1. **Root branch:** outward-certify the endpoint monotone-face inequalities (`H_B>0`, `A_p>0`, opposite corner signs), or an equivalent contraction certificate, using NM13-07's exact moment compiler and the existing Gaussian tail controls.
2. **Comparison transport:** outward-certify the anchor `Psi(12.75)>=0.0152009` and the nine scalar bounds on `-I/c`. This is strictly simpler than certifying `Psi_p,Psi_B,H_p,H_B,A_p,A_B` and `Delta` for objective transport.
3. Apply NM03-T03-ENVELOPE and the root certificate; only then promote `alpha_U=12.3197` to the independently certified bracket.

No peer/historical file, shared root ledger, schedule, permission, workflow, email, Drive object, paid compute, or public resource was modified.

```yaml
ledger_delta:
  worker: NM13-03
  parent: T03
  target: "negative spherical Gaussian perceptron, kappa=-1, exact radius sqrt(N)"
  status: "PARTIAL / NEW EXACT ENVELOPE THEOREM / SUPPORTED CANDIDATE_FULL endpoint 12.3197"
  original_problem_metric: "threshold bracket width alpha_U-alpha_L"
  independently_certified_before:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  independently_certified_after:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
    movement: "none; outward continuum enclosure still missing"
  supported_candidate_before:
    alpha_U: "12.33"
    width: "6.02702562494"
  supported_candidate_after:
    alpha_U: "12.3197"
    width: "6.01672562494"
    improvement_vs_previous_candidate: "0.0103"
    improvement_vs_certified_upper: "0.46467096216"
  theorem:
    name: "NM03-T03-ENVELOPE"
    statement: "on any C1 interior complete-second-full stationary branch, dPsi/dalpha=-I/c>0"
    obstruction_removed: "objective transport no longer requires stationary Jacobian/objective derivatives, and no longer requires Psi>0 on the root rectangle"
  target_point:
    alpha: "12.3197"
    p: "0.6649211712155717"
    B: "6.197411053061391"
    D: "0.6466197629671858"
    Psi_numeric: "2.320166148650493e-6"
  conditional_exact_transport_margin:
    value: "34831/50000000000"
    decimal: "6.9662e-7"
    condition: "outward-certify anchor and nine scalar -I/c caps on the stationary branch"
  essential_artifacts:
    checker_commit: "e79526a6f07be1a5158cc8bb2d9507585fc84960"
    output_commit: "ec9f8016f3b15d76183363c2e27cd76cd6e9bfc4"
  next_step: "outward-certify endpoint root branch and scalar -I/c caps, then promote 12.3197 if all enclosures pass"
```
