Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-03 / T03 — third-full feasibility reduction and supported alpha=12.288 upper candidate

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-03`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-07`  
Status: **PARTIAL / NEW THEOREM + SUPPORTED CONDITIONAL THRESHOLD IMPROVEMENT / NOT YET INTERVAL-CERTIFIED**

## 0. Compact handoff and why this run changes mechanism

The source problem remains exactly the iid-Gaussian spherical perceptron at `kappa=-1`: for `M=floor(alpha N)`, `g_a iid N(0,I_N)`, seek `sigma` with

`||sigma||_2 = sqrt(N)` exactly and `<g_a,sigma> >= -sqrt(N)` for every `a<=M`.

No ball relaxation, smaller radius, radial rescaling, or replica-only threshold is used below.

The preceding NM13-03 report certified a complete-second stationary comparison point at `alpha=12.319635`. NM13-07 then consumed it and proved a uniform micro-continuation to the current review-pending directed-interval upper candidate

`alpha_U = 12.31963485`.

NM13-07 also identified the decisive obstruction: the complete-second comparison zero is numerically near `12.3196343465869`, so further second-full polishing can only shave microscopic digits. Its explicit next instruction was to change mechanism to the next lifting level or an independent overlap/dual-feasibility argument. This run does that immediately: it derives and executes a complete **third-full (`r=3`) feasibility compiler**.

## 1. Current primary-source status, bounded refresh on 20 September 2026

1. **El Alaoui--Sellke, arXiv:2010.15811.** Their model is exactly the Gaussian spherical perceptron on radius `sqrt(N)`, with constraints `<g_a,sigma> >= kappa sqrt(N)`. For `kappa<0`, their algorithm outputs on radius `sqrt(qbar N)` with `qbar<1`; this does not prove the exact full-radius satisfiability threshold required here.
2. **Stojnic, arXiv:2312.16531.** The paper puts the negative spherical perceptron into complete stationarized fully lifted RDT. Theorem 2 gives the stationary complete-sfl mechanism; Section 4.2.3 writes the full third-level objective and eight derivatives. Theorem 3 gives closed parametric relations, and Table 6 reports the third-full `kappa=-1` capacity as `12.29` (two-decimal display). The paper itself says substantial numerical work is required to make the mechanism operational. I therefore do not treat the table alone as a directed-interval proof.
3. **Montanari--Zhong--Zhou, arXiv:2110.15824.** Rigorous upper/lower interpolation-threshold bounds and the LP threshold; not the exact `kappa=-1` value.
4. **Annesi--Malatesta--Zamponi, arXiv:2410.06717.** Full-RSB SAT/UNSAT calculation and overlap-gap structure; useful physics guidance, not a replacement here for a rigorous full-radius comparison certificate.
5. **Huang--Sellke--Sun, arXiv:2608.29416 (29 August 2026).** Exact algorithmic projection-pursuit thresholds for a dimension-free Lipschitz algorithm class; the paper explicitly distinguishes the non-algorithmic feasible-projection problem as still open.

A bounded fresh arXiv search found no later rigorous theorem plainly closing the exact full-radius `kappa=-1` target. This is dated negative evidence, not a worldwide novelty certificate. `POSTED.md` exclusions concern different perceptron statements (notably zero-margin/Ising work), not this continuous negative-margin exact-sphere target.

## 2. Exact third-full objective and closed Gaussian kernel

Write the interior third-full parameters as

`0 < p3 < p2 < 1`, `0 < q3 < q2 < 1`, `c2>c3>0`, `gamma_sq>0`, `gamma_p>0`.

Set

`Aq = 2 gamma_p - c2(1-q2)`,

`Dq = Aq - c3(q2-q3)`.

For independent standard Gaussians `U3,U4,H`, define

`mu = sqrt(p2-p3) U3 + sqrt(p3) U4 - 1`,

`s = sqrt(1-p2)`, `B=c2/(4 gamma_sq)`, and

`f(mu,s,B) = E_H exp[-B(mu+sH)_+^2]`.

The already-proved closed kernel is

`f = Phi(-mu/s) + (1+2Bs^2)^(-1/2) exp[-B mu^2/(1+2Bs^2)]`
`                 * Phi(mu/(s sqrt(1+2Bs^2)))`.

Thus the only remaining perceptron-side Gaussian quantity at third full is the two-dimensional expectation

`Q = E_U4 log E_U3 [ f(mu,s,B)^(c3/c2) ]`.

Stojnic's Eq. (94), after analytically closing its `q`-Gaussian block, becomes

`Psi3 = 1/2(1-p2 q2)c2 + 1/2(p2 q2-p3 q3)c3 - gamma_p`
`       + (1/(2c2)) log(Aq/(2 gamma_p))`
`       + (1/(2c3)) log(Dq/Aq) - q3/(2Dq)`
`       + gamma_sq - (alpha/c3) Q`.                                      (2.1)

I checked the sign of the closed `q`-block both from the PDF equation and independently by direct Gaussian integration; the direct nested Gaussian value and (2.1)'s closed block agreed to floating roundoff.

## 3. New theorem — third-full feasibility compiler and envelope sign

### Theorem NM03-T03-THIRDFULL-FEASIBILITY

Assume the interior domain above and `Aq,Dq>0`. Define

`c3 = sqrt(p3/q3)/(p2-p3) - sqrt(q3/p3)/(q2-q3)`,                    (3.1)

`gamma_p = 1/2 * (1-q2)/(1-p2) * (p2-p3)/(q2-q3) * sqrt(q3/p3)`,   (3.2)

`c2 = [(p2-p3)/(q2-q3) sqrt(q3/p3)]/(1-p2)`
`     - [(q2-q3)/(p2-p3) sqrt(p3/q3)]/(1-q2)`.                     (3.3)

Then:

1. The source third-full stationarity equations `partial_{q3}Psi3=0`, `partial_{q2}Psi3=0`, and `partial_{gamma_p}Psi3=0` hold identically after the reconstruction (3.1)--(3.3).
2. Consequently full third-level stationarity is equivalent to the **five-scalar reduced system**

`partial_{p3}Psi3 = partial_{p2}Psi3 = partial_{c3}Psi3`
`= partial_{c2}Psi3 = partial_{gamma_sq}Psi3 = 0`,                  (3.4)

with (3.1)--(3.3) substituted after taking the displayed partial derivatives. At capacity one adds `Psi3=0`, giving a six-scalar system in `(p3,p2,q3,q2,gamma_sq,alpha)` instead of the original eight stationarity unknowns plus `alpha`.
3. On any `C^1` interior stationary branch parameterized by `alpha`,

`d Psi3/d alpha = -Q/c3 > 0`.                                      (3.5)

Therefore, consuming the same complete-sfl comparison implication already used by NM13-07, an exact reduced stationary root at a fixed density with `Psi3>0` is an exact-sphere third-full infeasibility certificate at that density.

### Proof

Stojnic's `q3` stationarity identity (Eq. 137) gives

`p3 = q3/Dq^2`.

On the positive interior branch this fixes `Dq=sqrt(q3/p3)`. Combining the `q2` identity (Eq. 138) with the preceding relation gives Eq. 139,

`Aq = (q2-q3)/(p2-p3) * sqrt(p3/q3)`.

Subtracting `Dq` from `Aq` and dividing by `q2-q3` gives exactly (3.1). The `gamma_p` stationarity equation (Eq. 125), combined with the same two identities, gives (3.2), and then `Aq=2 gamma_p-c2(1-q2)` gives (3.3). Hence the three eliminated source derivatives vanish identically under reconstruction. This proves item 1.

For item 2, the full source system has the eight derivatives with respect to `(q3,q2,p3,p2,c3,c2,gamma_p,gamma_sq)`. Three are now identities. The remaining five are exactly (3.4). Conversely, any interior full stationary point obeys the source identities above and hence the same reconstruction. Thus no stationary equation is dropped; the reduction is equivalent on the stated branch. Adding `Psi3=0` gives the six-scalar capacity system.

For item 3, differentiate `Psi3(theta(alpha),alpha)` along a stationary branch. Every parameter derivative vanishes by stationarity, leaving only the explicit alpha derivative:

`dPsi3/dalpha = partial_alpha Psi3 = -Q/c3`.

For every finite `mu`, `s>0`, and `B>0`, the random variable `exp[-B(mu+sH)_+^2]` lies in `(0,1]` and is strictly below one on a positive-probability event; hence `0<f(mu,s,B)<1`. Since `c3/c2>0`, the inner expectation in `Q` is strictly in `(0,1)`, so its logarithm is negative and `Q<0`. Because `c3>0`, (3.5) follows. QED.

### Why this removes NM13-07's named obstruction

The complete-second route had already reached its comparison zero, so a stronger source bound required the next lifting level. A direct third-full validator appears to be a nine-variable numerical problem (eight stationarity variables plus `alpha`) with a nested Gaussian expectation. The theorem removes three stationarity variables algebraically, while the closed kernel removes the innermost Gaussian integral. What remains is a five-dimensional fixed-density root or six-dimensional capacity root with only a two-dimensional Gaussian expectation. This is the first executable third-full reduction in the current T03 track.

## 4. Decisive calculation at kappa=-1

The checker starts from the source Table-5 `kappa=-1` row only as a seed and solves the reduced equations independently at Gauss--Hermite orders `60,80,100,120,160` using x64 automatic derivatives of (2.1). It then checks the **full eight-component gradient**, including the three reconstructed derivatives.

The capacity zero converges as follows:

| GH order | alpha solving stationarity + Psi3=0 |
|---:|---:|
| 60 | 12.2872227706495 |
| 80 | 12.2872221830818 |
| 100 | 12.2872222240456 |
| 120 | 12.2872222215129 |
| 160 | 12.2872222215937 |

This is consistent with Stojnic's published two-decimal third-full value `12.29`, but substantially refines it numerically.

For a strict positive-comparison test I deliberately stay above the zero and solve only stationarity at

`alpha = 12.288`.

At GH order 160 the stationary point is

`p3 = 0.599126773053267`,

`p2 = 0.969080522852930`,

`q3 = 0.228731793616387`,

`q2 = 0.638442418504189`,

`c3 = 2.86661591200020`,

`c2 = 13.0870435401505`,

`gamma_sq = 0.0766524281089569`,

`gamma_p = 3.26204123769656`.

The domain margins are comfortable:

`Aq = 1.792362664... > 0`, `Dq = 0.617879667... > 0`, `c2>c3>0`.

The comparison value is

`Psi3(12.288) = 2.65977391709358e-5 > 0`,

and the full eight-variable gradient infinity norm is `1.35e-15`. Across GH orders 60 through 160, `Psi3(12.288)` stays positive in the narrow range `2.6578991e-5` to `2.6599051e-5`.

The nested perceptron term at the GH-160 point is

`Q_GH160 = -0.09803284146792998`.

An independently coded adaptive two-dimensional SciPy quadrature over `[-8,8]^2` gives

`Q_adaptive = -0.09803284146792308`,

difference `6.90e-15`. The envelope slope is therefore numerically

`-Q/c3 = 0.0341981083191 > 0`,

in agreement with theorem (3.5).

The reduced fixed-density Jacobian has smallest singular value about `2.555e-4` and condition number about `1.65e5`: it is numerically nondegenerate but substantially ill-conditioned. This explains why the source's low-precision displayed lifting coordinates need not agree closely with a high-precision root even though the capacity agrees at the displayed two decimals. It also means an interval proof should precondition the reduced system rather than validate the original nine-dimensional formulation.

## 5. Original-problem before/after versus mechanism gain

### Original problem: threshold quantity

Retained rigorous lower endpoint:

`alpha_L = 6.30297437506`.

**Before this run (current NM13-07 review-pending directed-interval candidate):**

`[6.30297437506, 12.31963485]`, width `6.01666047494`.

**After this run, supported third-full CONDITIONAL candidate:**

`[6.30297437506, 12.288]`, width `5.98502562494`.

Supported upper-endpoint / bracket-width gain:

`12.31963485 - 12.288 = 0.03163485`.

This is a source-level threshold improvement, not an auxiliary-constant improvement, and it is for the exact sphere and exact Gaussian constraint model.

However, I do **not** promote `12.288` to the review-pending directed-interval `CANDIDATE_FULL` tier in this run. The currently interval-supported/review-pending endpoint therefore remains `12.31963485` until the five-dimensional third-full root and its positive objective are enclosed with outward rounding. Unknown rigor is not reported as zero error.

### Demonstrated mechanism gain

Before: the second-full comparison was saturated and the next level looked like an eight-derivative / nine-variable nested-Gaussian validation problem.

After: the exact source algebra plus the Gaussian kernel yield a five-variable fixed-density feasibility system and a six-variable capacity system. The new third-full envelope identity gives a strict sign direction, and the executed system produces a positive-comparison exact-sphere candidate at `12.288`, over `0.03` below the previous source-level candidate.

## 6. Preserved failures, caveats, and next attack

Preserved failed/saturated routes:

1. **Complete-second digit shaving is exhausted.** Its zero is only about `5e-7` below the prior certified endpoint and cannot give a material gain.
2. **Direct unreduced third-full Newton is badly conditioned.** The algebraic source reduction is materially better and is now the canonical route.
3. **Whole-box objective positivity near a sharp stationary root failed already at second full.** The a-posteriori objective idea remains available after a third-full contraction is built.
4. Changed-radius, ball, and replica/full-RSB-only predictions remain non-solutions to the exact spherical target.

The remaining obstruction is concrete: convert the reduced `alpha=12.288` point into an outward-rounded Krawczyk/weighted-contraction certificate for the five reduced stationarity equations, while enclosing the two-dimensional Gaussian `Q` and needed derivatives. The positive objective margin `2.66e-5` is roughly three orders of magnitude larger than the final second-full margin, so there is room for a practical certificate. The next run should build that reduced interval enclosure, not return to second-full polishing.

## 7. Essential artifacts

Executed checker:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_thirdfull_reduction_alpha12288.py`

creation commit: `bca1a1485faee8f509e188876155da0d543bfbf5`.

Archived actual output:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_thirdfull_reduction_alpha12288.out`

creation commit: `aba4b3d88ad058cbfec7fd4f268c244cc4a37c63`.

The output ends `ALL_NUMERICAL_THIRDFULL_CHECKS_PASS` and explicitly labels the computation `CONDITIONAL_NUMERICAL_NOT_INTERVAL_CERTIFIED`.

## 8. ledger_delta

```yaml
ledger_delta:
  worker: NM13-03
  parent: T03
  source_model: "iid Gaussian constraints; kappa=-1; exact ||sigma||=sqrt(N) sphere"
  status: PARTIAL
  theorem: NM03-T03-THIRDFULL-FEASIBILITY
  consumed_companion:
    report: "proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-certified-microcontinuation-alpha1231963485.md"
    upper_candidate: 12.31963485
  original_problem:
    lower_endpoint: 6.30297437506
    supported_upper_before: 12.31963485
    supported_upper_after_conditional: 12.288
    width_before: 6.01666047494
    width_after_conditional: 5.98502562494
    endpoint_gain: 0.03163485
    interval_review_pending_upper_before: 12.31963485
    interval_review_pending_upper_after: 12.31963485
  mechanism:
    old_obstruction: "complete-second comparison zero saturated; third-full validation appeared 9-dimensional with nested Gaussian integration"
    new_reduction: "three stationarity equations reconstructed algebraically; fixed-alpha system 5D; capacity system 6D; innermost Gaussian integral closed"
    thirdfull_zero_scout_gh160: 12.2872222215937
    alpha_test: 12.288
    psi_alpha_test_gh160: 2.65977391709358e-5
    full_gradient_inf_gh160: 1.35e-15
    independent_Q_difference: 6.90e-15
    envelope_slope: 0.0341981083191
  rigor_label: "CONDITIONAL numerical third-full support; not yet outward interval-certified"
  residual_obstruction: "5D reduced Krawczyk/contraction enclosure plus rigorous 2D Gaussian derivative bounds at alpha=12.288"
  next_attack: "intervalize the reduced third-full system and apply the existing a-posteriori objective localization; do not polish second-full digits"
  artifacts:
    checker_commit: bca1a1485faee8f509e188876155da0d543bfbf5
    output_commit: aba4b3d88ad058cbfec7fd4f268c244cc4a37c63
```

No peer/historical file, shared root ledger, POSTED item, email/Drive object, workflow, permission, public resource, paid compute, or schedule was modified.
