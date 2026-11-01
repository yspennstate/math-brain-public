Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-07 / T03 — multi-affine branch-slope certificate and exact-sphere upper endpoint 12.31963454

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03`  
Status: **PARTIAL / STRICT COMPUTER-ASSISTED SOURCE-BRACKET IMPROVEMENT / PENDING LATER INDEPENDENT REVIEW**

## 0. Short handoff and frozen source problem

The source target is unchanged. Let `M=floor(alpha N)`, let `g_1,...,g_M` be iid `N(0,I_N)`, and ask whether there exists `sigma` with

`||sigma||_2 = sqrt(N)` exactly,

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`,

as `N->infinity` at fixed density `alpha`.

No radius change, ball relaxation, radial rescaling, Ising restriction, or replica-only threshold is used as a source implication.

The entering repository-supported review-pending bracket is

`alpha_L = 6.30297437506`,

`alpha_U = 12.3196348278`,

`width = 6.01666045274`.

The latest NM13-07 run changed the substantive route to complete-third lifting and proved cancellation-free entropy-dissipation representations for both c-sector entropies. The latest companion NM13-03 report then supplied a curvature-overlap sandwich and a supported, but still non-interval-certified, complete-third candidate near `alpha=12.28722223`. The present run does not promote that candidate. Instead it extracts a new rigorous local consequence from the already archived directed-interval complete-second box: the stationary comparison slope can be bounded by the Jacobian geometry itself, much more sharply than the previous Jensen envelope bound. This produces a strict source-level improvement in the same run while preserving the third-full route as the next substantial attack.

## 1. Primary-source hypotheses and current proof status, refreshed 20 September 2026

- **El Alaoui--Sellke, arXiv:2010.15811.** Their ambient model is exactly the iid-Gaussian spherical perceptron on `S^{N-1}(sqrt(N))`, with constraints `<g_a,sigma> >= kappa sqrt(N)`. For `kappa<0` their algorithmic construction, given access to the Parisi solution, outputs a feasible vector on radius `sqrt(qbar N)` with `qbar in (0,1)`. Their abstract explicitly presents the full-radius capacity as a statistical-physics prediction rather than a theorem supplied by that algorithm. Thus this is not an exact-radius `kappa=-1` threshold result.
- **Stojnic, arXiv:2312.16531.** This fits the negative spherical perceptron into stationarized fully lifted random duality theory and states a capacity characterization. Its abstract also says that making the fl-RDT machinery practically operational requires substantial numerical work. The project therefore continues to distinguish source-matched stationarity plus a directed numerical certificate from a floating-point finite-lift table value.
- **Montanari--Zhong--Zhou, arXiv:2110.15824.** This rigorously proves upper and lower bounds for the negative-perceptron threshold and characterizes the linear-programming threshold; it does not identify the exact `kappa=-1` threshold. The retained lower endpoint `6.30297437506` is the repository-normalized consequence of its rigorous LP-success side.
- **Annesi--Malatesta--Zamponi, arXiv:2410.06717.** This computes the SAT/UNSAT transition within a full-RSB ansatz. It is useful overlap guidance, not substituted for a rigorous exact-radius certificate.
- **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** This gives exact thresholds for a dimension-free Lipschitz algorithmic class and explicitly separates the unrestricted feasible-projection problem as a major outstanding non-algorithmic problem.

A bounded fresh search on 20 September 2026 did not surface a later theorem plainly closing the unrestricted exact-radius `kappa=-1` target. This is dated negative evidence only. `POSTED.md` explicitly says the posted/restricted zero-margin perceptron results do not close their negative-margin counterparts.

## 2. Consumed directed-interval complete-second box

The earlier NM13-03/NM13-07 directed certificate works at

`alpha0 = 12.319635`,

with center

`p_c = 0.6649244534165579`,

`B_c = 6.197655366469065`,

and weighted radii

`r_p=1e-7`, `r_B=4e-6`.

Write the two stationary equations at target density `a` as

`F_a(p,B) = (H(p,B), alpha(p,B)-a)=0`,

and let `Psi(p,B)` be the complete-second comparison value. The archived directed computation proves on the whole fixed box the derivative enclosures

`H_p in [-0.03370146727424432,-0.02828455987858220]`,

`H_B in [0.0003284932328676832,0.0005043842197013973]`,

`alpha_p in [24.67157455631033,25.28760973547386]`,

`alpha_B in [-0.6024378692892906,-0.6008000232876709]`,

`Psi_p in [0.8701089577466267,0.8954131534826132]`,

`Psi_B in [-0.02136650282575422,-0.02115542237455933]`.

It also gives the frozen rational preconditioner

`A = [[-7294853/100000, -504965/10000000],`
`     [-3028867/1000,   -3758826/1000000]]`,

the uniform weighted contraction bound

`q <= 70497781/125000000 = 0.563982248`,

center residual ceilings

`|H_c| < 4.7e-12`,

`|alpha_c-alpha0| < 3.7e-11`,

and the true-root objective lower bound

`Psi(alpha0) >= 23584189005311 / 1090044380000000000000`

`             = 2.163598972485047e-8`.

The previous continuation used the exact stationary envelope identity plus a coarse global bound `dPsi/dalpha < 1507/12000 ~= 0.12558`. The new observation is that the already certified local derivative box contains much more information.

## 3. New theorem — multi-affine tangent bound for the stationary branch

### Theorem NM07-T03-MULTIAFFINE-BRANCH-SLOPE

Let `H, A, P` be `C^1` on a rectangle `Q subset R^2`; write the second stationary equation at parameter `a` as `A(p,B)=a`. Suppose every `a` in an interval has a unique zero `(p(a),B(a)) in Q` of

`H(p,B)=0`, `A(p,B)=a`,

and suppose the six first derivatives lie in independent compact intervals.

Define

`Delta = H_p A_B - H_B A_p`,

`N = -P_p H_B + P_B H_p`.

If `Delta>0` throughout the derivative rectangle, then the stationary branch is `C^1` and

`d/da P(p(a),B(a)) = N/Delta`.                                (3.1)

Moreover, for any rational `s`, the functions `Delta`, `N`, and `N-s Delta` are multi-affine functions of the six derivative variables. Therefore their extrema on the derivative rectangle occur at vertices. In particular, if every vertex satisfies

`Delta>0`, `N>0`, `N-s Delta<0`,

then throughout the whole stationary branch

`boxed: 0 < dP/da < s`.                                      (3.2)

### Proof

The Jacobian of `(H,A)` is

`J = [[H_p,H_B],[A_p,A_B]]`,

with determinant `Delta`. If `Delta>0`, the implicit-function theorem applies. Differentiating

`H(p(a),B(a))=0`, `A(p(a),B(a))=a`

gives

`J [p'(a),B'(a)]^T = [0,1]^T`.

Hence

`p'=-H_B/Delta`, `B'=H_p/Delta`,

and therefore

`P' = P_p p' + P_B B'`

`   = (-P_p H_B + P_B H_p)/Delta = N/Delta`,

which is (3.1).

For the vertex assertion, freeze all variables but one. Each of `Delta`, `N`, and `N-s Delta` is affine in that coordinate, so its extremum over the corresponding interval is attained at an endpoint. Repeating coordinate by coordinate moves an extremizer to a vertex of the full hyperrectangle. This proves the multi-affine vertex principle and (3.2). QED.

### Why this helps here

A naive interval quotient `N/Delta` loses the cancellation between numerator and determinant and gives a poor bound. Checking the sign of `N-s Delta` retains that dependence exactly. It is a small finite exact-arithmetic problem once the directed derivative box is known.

## 4. Exact application: the local comparison slope is below 1/25

Use the following rational widenings of the archived directed intervals:

`H_p in [-3371/100000,-2828/100000]`,

`H_B in [3284/10^7,5044/10^7]`,

`alpha_p in [24671/1000,25288/1000]`,

`alpha_B in [-60244/100000,-6008/10000]`,

`Psi_p in [8701/10000,8955/10000]`,

`Psi_B in [-2137/100000,-2115/100000]`.

The executed exact checker enumerates all `2^6=64` vertices. It proves

`Delta >= 1323549/312500000 = 0.0042353568 > 0`,

`N >= 732159/5000000000 = 0.0001464318 > 0`,

and for `s=1/25`,

`N - (1/25) Delta <= -493639/125000000000`

`                    = -3.949112e-6 < 0`.

Therefore, not just at the center but at every stationary root in this certified box,

`boxed: 0 < dPsi/dalpha < 1/25 = 0.04`.                       (4.1)

This is more than a factor three sharper than the preceding global Jensen envelope `1507/12000` and it uses only already certified local variational derivative data.

The checker prints the vertex ratios only as diagnostics: the rigorous proof of the whole-box ratio bound is the sign test on the multi-affine quantity `N-(1/25)Delta`, not the assertion that a ratio itself has a vertex extremum.

## 5. Uniform continuation to alpha=12.31963454

Set

`alpha1 = 12.31963454 = alpha0 - 4.6e-7`.

For any target `a in [alpha1,alpha0]`, only the constant second residual `alpha(p,B)-a` changes. Thus the same derivative box and contraction constant remain valid. At the worst endpoint the center residual ceiling is

`E_alpha = 4.6e-7 + 3.7e-11 = 4.60037e-7`.

With the inherited exact preconditioner and weighted radii, the executed rational arithmetic gives

`eta = 871717355731/2000000000000`

`    = 0.4358586778655`,

while

`1-q = 54502219/125000000`

`    = 0.436017752`.

Hence

`eta < 1-q`,

and the Banach map is a contraction for every target density in the full interval. Its endpoint localization factor is

`rho = 871717355731/872035504000`

`    = 0.9996351659220976 < 1`.

Thus every `a in [alpha1,alpha0]` has a unique genuine stationary root in the fixed directed box. Section 4 gives `Delta>0`, so these roots form a `C^1` branch.

Transporting the already certified objective lower bound with (4.1),

`Psi(alpha1)`
` >= Psi(alpha0) - (alpha0-alpha1)/25`
` >= 23584189005311/1090044380000000000000 - (23/50000000)/25`
` = 3527372413311/1090044380000000000000`
` = 3.235989724850469e-9 > 0`.                                (5.1)

Therefore the true stationary point at `alpha1` still has strictly positive complete-second comparison value.

Consuming the already source-matched stationarized fl-RDT implication used in the earlier directed certificates, this gives asymptotic UNSAT for the exact spherical model at `alpha1`; monotonicity in the number of constraints yields

`boxed: alpha_c(-1) <= 12.31963454`.                          (5.2)

This is a computer-assisted proof candidate pending later independent review, not a claim that the exact threshold itself has been solved.

## 6. Source threshold before / after, separately from mechanism gain

### Source-level rigorous/review-pending bracket

Before:

`[6.30297437506, 12.3196348278]`,

width `6.01666045274`.

After:

`boxed: [6.30297437506, 12.31963454]`,

width

`boxed: 6.01666016494`.

Upper-endpoint and bracket-width gain:

`boxed: 12.3196348278 - 12.31963454 = 2.878e-7`.

### Demonstrated mechanism gain

Before, the only rigorous transport slope available to NM13-07 in this local box was the global estimate

`dPsi/dalpha < 1507/12000 ~= 0.12558`.

After, the new multi-affine tangent theorem turns the already archived local Jacobian/objective derivative ranges into

`boxed: 0 < dPsi/dalpha < 1/25 = 0.04`

through a finite exact 64-vertex sign certificate. This is a local variational/overlap-parameter statement, not an auxiliary decimal bound: it directly controls the stationary comparison value under a source-density change and produces (5.2).

## 7. Sanity checks, preserved failures, and residual obstruction

The essential checker is pure exact rational arithmetic after consuming the prior directed intervals. It independently verifies the determinant sign, numerator sign, the multi-affine slope inequality, the continuation inequality, the transported objective margin, and the bracket arithmetic. Its archived stdout ends

`ALL_EXACT_BRANCH_TANGENT_CHECKS_PASS`.

Preserved failures / limitations:

1. **Whole-box objective positivity near the complete-second zero** still fails; the earlier root-localization argument remains necessary.
2. **Global Jensen transport** is valid but much too loose; it was replaced here by the local branch tangent calculation.
3. The new continuation nearly exhausts the existing box geometrically: `rho ~= 0.999635`. Extending the same complete-second branch materially farther would require a new directed interval box, and the high-accuracy scout already places the complete-second comparison zero near `12.3196343465869`. This route should therefore not consume another substantive run merely to shave digits.
4. The complete-third candidates near `12.3164` and `12.28722223` remain **CONDITIONAL** because no outward four-overlap Krawczyk/root inclusion has yet been completed. Floating-point Gauss--Hermite convergence is not promoted to a source endpoint.

## 8. Next attack

Return to the materially stronger complete-third route, not another complete-second microextension. On a small four-overlap box around the supported `alpha ~= 12.28722223` point, combine:

1. NM13-03's curvature-overlap sandwich for the `q2-q3` residual;
2. its variance-matched KL/Fisher cage for the c-sector;
3. NM13-07's positive entropy-dissipation representations only on subboxes surviving those cheap filters;
4. the prescribed-positive-gap four-overlap compiler, so comparison positivity is algebraic once the root is certified.

The decisive goal is an outward weighted Krawczyk inclusion. A successful inclusion would give a non-microscopic source improvement; another floating-point refinement is not enough.

## 9. Essential executed artifacts

Created in this run:

- exact checker: `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_branch_tangent_continue.py`
  - creation commit `b153049fdec6dc889d5ff17ec2879c9bd09d8624`
- executed stdout: `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_branch_tangent_continue.out`
  - creation commit `08393a35c8576b22b9000f16af52da618ee01f4a`

Key executed output:

`DET_MIN 1323549/312500000 0.0042353568`

`NUM_MIN 732159/5000000000 0.0001464318`

`SLOPE_CAP 1/25 0.04`

`MAX_NUM_MINUS_CAP_DET -493639/125000000000 -3.949112e-06`

`ETA 871717355731/2000000000000 0.4358586778655`

`ONE_MINUS_Q 54502219/125000000 0.436017752`

`RHO 871717355731/872035504000 0.9996351659220976`

`PSI_NEW_LOWER 3527372413311/1090044380000000000000 3.235989724850469e-09`

`RIGOROUS_ALPHA_U_AFTER 12.31963454`

`ALL_EXACT_BRANCH_TANGENT_CHECKS_PASS`

## 10. ledger_delta

```yaml
ledger_delta:
  worker: NM13-07
  parent: T03
  status: PARTIAL
  source_model:
    kappa: -1
    constraints: iid Gaussian
    sphere_radius: sqrt(N) exactly
  source_metric:
    quantity: rigorous/review-pending threshold bracket
    before: "[6.30297437506, 12.3196348278]"
    after: "[6.30297437506, 12.31963454]"
    width_before: 6.01666045274
    width_after: 6.01666016494
    upper_endpoint_gain: 2.878e-7
  mechanism_gain:
    theorem: NM07-T03-MULTIAFFINE-BRANCH-SLOPE
    old_local_transport_cap: "1507/12000"
    new_local_transport_cap: "1/25"
    determinant_lower: "1323549/312500000"
    numerator_lower: "732159/5000000000"
    cap_gap_upper: "-493639/125000000000"
    new_endpoint_objective_lower: "3527372413311/1090044380000000000000"
  third_full_frontier:
    supported_conditional_upper: 12.28722223
    directed_interval_certified: false
    residual_obstruction: "outward four-overlap root inclusion"
  next_step: "hybrid third-full Krawczyk using curvature-overlap, variance-matched KL/Fisher, positive entropy dissipation, and prescribed-positive-gap compiler"
  code_commit: b153049fdec6dc889d5ff17ec2879c9bd09d8624
  output_commit: 08393a35c8576b22b9000f16af52da618ee01f4a
```
