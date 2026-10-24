Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-07 / T03 — strict bracket microextension and prescribed-positive-gap four-overlap compiler

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03`  
Status: **PARTIAL / STRICT SOURCE-BRACKET IMPROVEMENT / NEW EXACT THIRD-FULL COMPILER / THIRD-FULL WAYPOINT STILL CONDITIONAL**

## 0. Short handoff and exact source target

The source problem remains frozen exactly as required. Let `M=floor(alpha N)`, let `g_a iid N(0,I_N)`, and ask for `sigma` satisfying

`||sigma||_2=sqrt(N)` exactly,

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`,

with fixed `alpha` and `N->infinity`.

No changed sphere radius, ball relaxation, radial rescaling, Ising replacement, or replica-only value is used as a source implication.

The entering repository-supported bracket was

`alpha_L = 6.30297437506`,

`alpha_U = 12.31963485`,

`W = 6.01666047494`.

The preceding NM13-07 run changed mechanism from complete-second to complete-third lifting and proved exact score-overlap identities reducing third-full stationarity. Since then, two essential neighboring advances appeared and are consumed here rather than rederived:

1. the complementary R14 route proved the strict-interior stationary scale-Euler identity

`Psi3 = 2 gamma_sq - r1/(r0 sqrt(r2))`

and reduced the third-full capacity problem to four overlap variables;
2. NM13-03 proved entropy/KL forms for the two c-stationarity equations and a one-dimensional power-mean comparison for the nested objective slope. Its newest `alpha=12.28723` point remains explicitly CONDITIONAL because no directed-interval four-dimensional root certificate has yet been completed.

This run does two things. First, it uses the already certified complete-second local branch only as the bookkeeping-sized final step needed to obtain a **strict new rigorous source endpoint**. Second, most of the mathematical work develops a new third-full positive-gap compiler designed to avoid both the ill-conditioned fixed-density system and a separate objective-positivity enclosure.

## 1. Primary-source hypotheses and current proof status

Fresh bounded checks on 20 September 2026 remain consistent with the repository state.

- **El Alaoui--Sellke, arXiv:2010.15811.** Their model is exactly the iid-Gaussian spherical perceptron on radius `sqrt(N)`, with constraints `<g_a,sigma> >= kappa sqrt(N)`. For `kappa<0`, however, their algorithm outputs a feasible vector on radius `sqrt(qbar N)` with `qbar<1`, conditional on the Parisi/FRSB structure. That is not the exact-radius satisfiability-threshold theorem required here.
- **Stojnic, arXiv:2312.16531.** The paper treats the negative spherical perceptron through complete stationarized fully lifted RDT. Its Theorem 2 explicitly requires the non-fixed lifting parameters to solve the stationarity equations before the complete-sfl characterization is invoked; its numerical section also states that substantial numerical work is required to make the characterization operational. Thus displayed finite-lift table values are not imported here as certified endpoints.
- **Montanari--Zhong--Zhou, arXiv:2110.15824.** This rigorously proves interpolation upper/lower bounds and characterizes the LP threshold, not the exact `kappa=-1` threshold. The retained lower endpoint `6.30297437506` is the repository-normalized consequence of that rigorous LP-success result.
- **Annesi--Malatesta--Zamponi, arXiv:2410.06717.** Their SAT/UNSAT value is computed under a full-RSB ansatz and is used only as structural guidance, not as a rigorous exact-radius replacement.
- **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** This gives exact thresholds for a dimension-free Lipschitz algorithm class and explicitly distinguishes the unrestricted feasible-projection problem as still outstanding.

A bounded fresh search did not surface a later theorem plainly closing the unrestricted exact-radius `kappa=-1` threshold. This is dated negative evidence, not a worldwide novelty certificate. `POSTED.md` continues to separate the owner's zero-margin / Ising perceptron work from this continuous negative-margin exact-sphere target.

## 2. Strict source-level movement: `12.31963485 -> 12.31963484`

This subsection is deliberately short because it reuses a previously certified complete-second box rather than reopening that saturated mechanism.

### 2.1 Inherited certified local data

The directed-interval complete-second certificate at the anchor

`alpha0 = 12.319635`

already established on one fixed `(p,B)` box:

- a rational preconditioner;
- whole-box Jacobian ranges;
- weighted contraction constant

`q = 70497781/125000000 = 0.563982248 < 1`;

- center residual bounds

`|H_c| < 4.7e-12`, `|alpha_c-alpha0| < 3.7e-11`;

- a certified true-root comparison lower bound

`Psi(alpha0) >= 23584189005311 / 1090044380000000000000`

`              = 2.163598972485047e-8`;

- and the exact envelope bound, throughout the same stationary box,

`0 < dPsi/dalpha < 2/15`.

For completeness, the slope bound came from the exact stationary envelope identity `dPsi/dalpha=-I/c`, Jensen's inequality

`-I <= B E[(G-1)_+^2]`,

the elementary Gaussian estimate

`E[(G-1)_+^2] < 2/25`,

and the whole-box algebraic bound `B/c < 5/3`.

### 2.2 Uniform contraction at the new target

Set

`alpha1 = 12.31963484 = alpha0 - 1.6e-7`.

Only the constant target component `alpha(p,B)-a` changes when `a` changes; the Jacobian box is identical. Accounting for the inherited `3.7e-11` center enclosure, the safe exact target-residual ceiling is

`EA = 1.601e-7`.

The executed rational checker gives

`eta = 246409487/1600000000 = 0.154005929375`,

and therefore

`rho = eta/(1-q)`
`    = 1232047435/3488142016`
`    = 0.35321022749321457 < 1`.

Hence the same preconditioned map is a strict contraction for every target density in the interval

`[12.31963484, 12.319635]`.

Banach's theorem gives a unique genuine stationary root for each density in that interval. Since `||I-A DF||<1`, the stationary Jacobian is invertible throughout the box, so the roots form a `C^1` branch and the envelope identity applies along the interval.

### 2.3 Objective remains positive

Transporting the certified anchor value down by `1.6e-7` and using `dPsi/dalpha < 2/15` gives the exact lower bound

`Psi(alpha1)`
` >= 23584189005311/1090044380000000000000`
`    - (2/15)(1.6e-7)`
` = 989726695933/3270133140000000000000`
` = 3.026563915171356e-10 > 0`.

Thus the genuine stationary complete-second point at `alpha=12.31963484` still has strictly positive comparison value. Under the same source-matched complete-sfl RDT implication already used by the preceding directed-interval certificate, the exact-sphere Gaussian perceptron is asymptotically UNSAT at this density. Constraint monotonicity therefore yields

`boxed: alpha_c(-1) <= 12.31963484`.

This is a strict source-level improvement of `1e-8` over the entering endpoint. It is intentionally microscopic: complete-second is saturated, and the substantive route below is the one intended to deliver the next non-microscopic gain.

### 2.4 Source bracket before / after

Before:

`[6.30297437506, 12.31963485]`, width `6.01666047494`.

After:

`boxed: [6.30297437506, 12.31963484]`,

width

`boxed: 6.01666046494`.

Source-level width gain:

`boxed: 0.00000001`.

T03 remains **OPEN / PARTIAL**. This does not identify the exact threshold.

## 3. New exact theorem: prescribed-positive-gap four-overlap compiler

The main mathematical work of the invocation is a different third-full formulation.

Work on the strict third-full interior branch

`0<p3<p2<1`, `0<q3<q2<1`, `c2>c3>0`, `gamma_sq,gamma_p>0`.

Define the secant slopes

`r2=q3/p3`,

`r1=(q2-q3)/(p2-p3)`,

`r0=(1-q2)/(1-p2)`,

and

`S = r1/(r0 sqrt(r2))`.

As in the preceding reports, reconstruct the q-sector algebraically from `(p2,p3,q2,q3)`:

`c3 = sqrt(p3/q3)/(p2-p3) - sqrt(q3/p3)/(q2-q3)`,

`gamma_p = 1/2 * (1-q2)/(1-p2) * (p2-p3)/(q2-q3) * sqrt(q3/p3)`,

`c2 = [(p2-p3)/(q2-q3) sqrt(q3/p3)]/(1-p2)`
`     - [(q2-q3)/(p2-p3) sqrt(p3/q3)]/(1-q2)`.

Let `delta>0` be prescribed. Define

`boxed: gamma_sq(delta) = (S+delta)/2`,

`boxed: B(delta) = c2/[2(S+delta)] = c2/(4 gamma_sq)`.

For the exact nested third-full kernel, retain the score moments `M1,M2,MB` from the preceding NM13-07 theorem and reconstruct

`alpha = c2^2/(4 B^2 MB)`.

Define

`R3 = q3 - M1/(4B^2 MB)`,

`R2 = q2 - M2/(4B^2 MB)`,

and let `Rc3,Rc2` be the two exact c-stationarity residuals from the preceding score compiler. Equivalently, by NM13-03's newest entropy theorem, they may be replaced by the sign-stable KL residuals

`RU = A_c3 - alpha D_U/c3^2`,

`RH = A_c2 - alpha D_H/(c2 c3)`.

### Theorem NM07-T03-POSGAP-4D

On the strict interior branch, zeros of

`(R3,R2,Rc3,Rc2)=0`

with the prescribed reconstruction above are exactly the complete-third stationary points having

`Psi3 = delta`.

Equivalently one may use `(R3,R2,RU,RH)=0`.

### Proof

The algebraic q-sector reconstruction makes the source `q3`, `q2`, and `gamma_p` stationarity equations identities. The score-overlap theorem proved by NM13-07 gives

`q3=M1/(4B^2MB)`, `q2=M2/(4B^2MB)`

as exactly the two p-stationarity equations once the `gamma_sq` equation is used. The reconstruction

`alpha=c2^2/(4B^2MB)`

is exactly that `gamma_sq` stationarity equation. Therefore `R3=R2=0` enforces the p-sector plus `gamma_sq` stationarity, while `Rc3=Rc2=0` enforces the remaining c-sector stationarity. All eight source stationarity equations consequently hold.

At every strict-interior full stationary point, the already proved scale-Euler identity is

`Psi3 = 2 gamma_sq - S`.

By construction `2 gamma_sq-S=delta`, hence every zero of the four residuals has

`boxed: Psi3=delta>0`.

Conversely, every strict-interior full stationary point with `Psi3=delta` satisfies the scale-Euler identity and therefore has `gamma_sq=(S+delta)/2`; the q-sector, score-sector, gamma-sector and c-sector equations then reproduce exactly the four residual equations above. This proves equivalence. QED.

### Why this compiler is materially better for certification

The fixed-density third-full system used earlier required five unknowns and was numerically ill-conditioned. The capacity compiler reduced to four variables but sat exactly at `Psi3=0`, so a source upper certificate still needed a continuation or separate positive-objective argument.

The new compiler keeps the better four-overlap parameterization **and builds a strictly positive comparison margin into the equations algebraically**. A validated four-dimensional root automatically has `Psi3=delta`; there is no cancellation-prone direct objective enclosure afterward. Using the entropy form `(RU,RH)` also replaces the two difficult c-sector differences with positive KL quantities.

## 4. Decisive numerical scout for the certification waypoint `delta=10^-3`

The executed checker solves the prescribed-gap four-overlap system at Gauss--Hermite orders `60,80,100,120,160,200`. This section is explicitly **NUMERICAL_ONLY / CONDITIONAL**; it is not used in the rigorous endpoint of Section 2.

The reconstructed density converges as

- order 60: `12.3164338713703`;
- order 80: `12.3164333240432`;
- order 100: `12.3164333588465`;
- order 120: `12.3164333568797`;
- order 160: `12.3164333569314`;
- order 200: `12.3164333569308`.

At order 200 the point is approximately

`p2=0.967828984055228`,

`p3=0.597722018031788`,

`q2=0.638663550092673`,

`q3=0.229918637629570`,

with reconstructed

`B=39.26289564113617`,

`gamma_sq=0.07977032633637680`,

`c2=12.52805599281815`,

`c3=2.839127862412615`,

`gamma_p=3.153765242988234`.

The directly evaluated objective is

`Psi3 = 0.00100000000000577`,

agreeing with the prescribed exact scale gap `delta=0.001` to the numerical integration error. The four-residual infinity norm is `4.15e-16`.

A finite-difference conditioning diagnostic gives

`sigma_min(J) ~= 2.787964e-4`,

`cond(J) ~= 2.704e3`.

If an outward-rounded four-dimensional root certificate validates this waypoint, it would give the exact-sphere source upper bound

`alpha_U <= 12.31643335693...`,

which is about

`0.00320148307`

below the newly rigorous `12.31963484` endpoint. The candidate is intentionally farther above the third-full capacity zero than `12.28723`: the built-in comparison margin `10^-3` is designed to make the first rigorous third-full certificate robust rather than maximally sharp.

Again, **this `12.316433...` endpoint is CONDITIONAL in this report** because the two-dimensional nested Gaussian moment map has not yet been outward-enclosed on a four-dimensional overlap box.

## 5. Residual obstruction and next attack

The remaining third-full obstruction is now narrow and computationally explicit. The next run should not return to complete-second digit shaving. It should validate the `delta=10^-3` four-overlap root by a weighted Krawczyk or contraction argument, preferably using the entropy-stable residuals `(R3,R2,RU,RH)`.

The only genuinely non-algebraic part left is outward enclosure of the nested Gaussian score/KL moments on a small overlap box. The objective itself no longer needs a separate enclosure because the theorem forces `Psi3=delta` at the certified root. The companion power-mean collapse also supplies one-dimensional checks on the nested comparison slope and should be used as a sanity envelope for the two-dimensional evaluator.

A practical validation route is: small overlap box around the order-200 point; analytic/rational preconditioner from the numerical Jacobian; directed quadrature for the closed one-step Gaussian kernel; whole-box strict-domain checks; Krawczyk inclusion. If that passes, promote `12.316433...` before attempting the sharper `12.28723` / capacity-zero regime.

## 6. Essential executed artifacts

Checker:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_posgap4d_microextend.py`

creation commit `7c2ecd90d23daaf00cfd06492811693d68a17d3a`.

Executed output:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_posgap4d_microextend.out`

creation commit `ea490a52e046e45940cf0f5ccac53c20994b8d9d`.

The output terminates

`ALL_EXACT_CHECKS_PASS`

`ALL_NUMERICAL_SCOUTS_PASS`.

The first label covers the rational complete-second continuation arithmetic and symbolic prescribed-gap identity. The third-full Gauss--Hermite/root section is explicitly labeled numerical-only and is not used to claim the rigorous endpoint.

## 7. Structured ledger_delta

```yaml
ledger_delta:
  task: NM13-07
  parent: T03
  status: PARTIAL
  exact_target: "negative spherical perceptron, kappa=-1, iid Gaussian constraints, ||sigma||_2=sqrt(N) exactly"
  source_metric_before:
    alpha_L: "6.30297437506"
    alpha_U: "12.31963485"
    width: "6.01666047494"
  source_metric_after:
    alpha_L: "6.30297437506"
    alpha_U: "12.31963484"
    width: "6.01666046494"
  source_movement:
    upper_endpoint_gain: "0.00000001"
    proof: "uniform exact contraction from alpha0=12.319635 plus envelope transport; Psi lower bound 3.026563915171356e-10"
  new_exact_mechanism:
    theorem: NM07-T03-POSGAP-4D
    statement: "prescribing delta>0 reduces strict-interior third-full positive-comparison stationarity to four overlap residuals and forces Psi3=delta algebraically"
    certification_benefit: "no separate objective-positivity enclosure after a validated root; entropy/KL c-residuals available"
  conditional_waypoint:
    delta: "0.001"
    alpha_GH200: "12.3164333569308"
    implied_gain_if_interval_certified: "~0.00320148307 below the new rigorous endpoint"
    jacobian_condition_numerical_only: "~2.704e3"
  consumed_neighbors:
    - "NM13-03 entropy/KL c-sector and power-mean collapse"
    - "R14 scale-Euler and four-overlap capacity reduction"
  residual_obstruction: "outward enclosure of nested Gaussian score/KL moments on a small four-dimensional overlap box"
  next_attack: "directed quadrature + entropy-stable 4D Krawczyk at delta=1e-3"
  artifacts:
    checker_commit: "7c2ecd90d23daaf00cfd06492811693d68a17d3a"
    output_commit: "ea490a52e046e45940cf0f5ccac53c20994b8d9d"
  runtime_model: "GPT-5.6 Sol"
  runtime_reasoning: UNVERIFIED
```
