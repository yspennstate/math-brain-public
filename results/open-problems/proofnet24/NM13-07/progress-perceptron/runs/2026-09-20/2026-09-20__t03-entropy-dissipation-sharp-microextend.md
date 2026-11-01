Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-07 / T03 — entropy-dissipation c-sector compiler and sharpened exact-sphere microextension

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03`  
Status: **PARTIAL / STRICT SOURCE-BRACKET IMPROVEMENT / NEW EXACT THIRD-FULL C-SECTOR REPRESENTATION / THIRD-FULL WAYPOINT STILL CONDITIONAL**

## 0. Short handoff and frozen source problem

The source target is unchanged. Let `M=floor(alpha N)`, let `g_1,...,g_M` be iid `N(0,I_N)`, and ask whether there exists `sigma` with

`||sigma||_2 = sqrt(N)` exactly,

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`,

as `N->infinity` at fixed density `alpha`.

No radius change, ball relaxation, radial rescaling, Ising replacement, or replica-only value is used as a source implication.

The entering repository-supported bracket was

`alpha_L = 6.30297437506`,

`alpha_U = 12.31963484`,

`width = 6.01666046494`.

The preceding NM13-07 run already changed mechanism from the numerically saturated complete-second route to complete-third lifting. It proved a prescribed-positive-gap four-overlap compiler and found the numerical-only waypoint

`delta = 10^-3`, `alpha ~= 12.3164333569308`,

with strict interior overlap parameters and `Psi3=delta` algebraically at an exact residual zero. The missing step is an outward four-dimensional root certificate for the nested Gaussian score/c-sector map.

The newest companion NM13-03 report attacks exactly that obstruction from the comparison side. It proves Gaussian transport/log-Sobolev cages for the two nested c-sector KL terms and pushes the numerical supported third-full candidate to `alpha=12.2872223`, still CONDITIONAL because no outward root enclosure has been completed.

This run complements that work in two ways. The source-level movement is a small but exact continuation of the already certified complete-second local branch, obtained by sharpening a Gaussian tail-moment inequality. The substantive new third-full mechanism rewrites both difficult c-sector KL terms as **positive entropy-dissipation integrals of variances**, eliminating the cancellation in their direct log-partition formulas and giving a better target for interval arithmetic.

## 1. Primary-source hypotheses and current status, refreshed 20 September 2026

- **El Alaoui--Sellke, arXiv:2010.15811.** The ambient model is exactly the iid-Gaussian spherical perceptron on `S^{N-1}(sqrt(N))`, with constraints `<g_a,sigma> >= kappa sqrt(N)`. For negative `kappa`, their algorithmic pure-state construction is at radius `sqrt(qbar N)` with `qbar<1`, under the Parisi/FRSB structural assumptions used there. It is not an exact full-radius satisfiability-threshold theorem at `kappa=-1`.
- **Stojnic, arXiv:2312.16531.** The negative spherical perceptron is treated by complete stationarized fully lifted RDT. The complete-sfl theorem requires the non-fixed lifting parameters to satisfy the displayed stationarity system. The paper's practical-realization discussion also says substantial numerical work is needed. Therefore an arbitrary floating-point parameter point or a displayed finite-lift table value is not imported as a rigorous endpoint here.
- **Montanari--Zhong--Zhou, arXiv:2110.15824.** This supplies rigorous interpolation bounds and the LP threshold, not equality with the exact `kappa=-1` satisfiability threshold. The retained lower endpoint `6.30297437506` is the repository-normalized consequence of that rigorous LP-success theorem.
- **Annesi--Malatesta--Zamponi, arXiv:2410.06717.** The full-RSB SAT/UNSAT transition is a statistical-physics/full-RSB-ansatz calculation and is used only as structural guidance.
- **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** This proves exact thresholds for a dimension-free Lipschitz algorithmic class and explicitly distinguishes the unrestricted feasible-projection problem as a separate outstanding problem.

A bounded fresh search did not surface a later theorem plainly closing the unrestricted exact-radius `kappa=-1` target. This is dated negative evidence, not a worldwide openness or priority certificate. `POSTED.md` continues to separate the owner's zero-margin / Ising perceptron work from this continuous negative-margin exact-sphere target.

## 2. Strict source movement by a sharper Gaussian envelope bound

This subsection deliberately reuses the existing directed-interval complete-second box. It is the bookkeeping-sized source movement; the third-full derivation in Sections 3--5 is the main mathematical work.

### 2.1 Inherited certified local branch

At the anchor

`alpha0 = 12.319635`,

the archived directed-interval certificate already supplies a fixed `(p,B)` box, a rational preconditioner, the whole-box contraction constant

`q = 70497781/125000000 = 0.563982248`,

center residual bounds

`|H_c| < 4.7e-12`, `|alpha_c-alpha0| < 3.7e-11`,

and a true-root comparison lower bound

`Psi(alpha0) >= 23584189005311 / 1090044380000000000000`

`             = 2.163598972485047e-8`.

On this stationary branch the exact envelope identity is

`dPsi/dalpha = -I/c > 0`.

The preceding proof bounded

`-I <= B E[(G-1)_+^2]`

and used the whole-box algebraic estimate `B/c<5/3`, but it inserted the coarse moment estimate `E[(G-1)_+^2]<2/25`.

### 2.2 New exact elementary Gaussian estimate

For `G~N(0,1)`, integration by parts gives

`E[(G-1)_+^2] = 2 Q(1) - phi(1)`,                         (2.1)

where `Q(1)=P(G>1)` and `phi` is the standard Gaussian density.

I prove the rational bounds

`Q(1) < 7933/50000 = 0.15866`,                            (2.2)

`phi(1) > 24197/100000 = 0.24197`.                        (2.3)

For (2.2), use `pi<355/113` to obtain

`phi(0)=1/sqrt(2 pi) > 19947/50000 = 0.39894`.

Also

`int_0^1 exp(-x^2/2) dx`
` = sum_{n>=0} (-1)^n / [2^n n! (2n+1)]`.

The alternating partial sum through `n=5` is a lower bound and exceeds

`42781/50000 = 0.85562`.

Hence

`Phi(1)-1/2 = phi(0) int_0^1 exp(-x^2/2)dx`
`           > (19947/50000)(42781/50000)`
`           > 1/2-7933/50000`,

which proves (2.2).

For (2.3), first prove

`e < 271829/100000`

by summing `sum_{n=0}^8 1/n!` and bounding the tail beginning at `1/9!` by the geometric series with ratio `1/10`. Together with `pi<355/113`, direct rational cross multiplication gives

`2 pi e < (100000/24197)^2`,

so `phi(1)=1/sqrt(2 pi e)>24197/100000`.

Substitution in (2.1) gives the sharper exact bound

`boxed: E[(G-1)_+^2] < 1507/20000 = 0.07535`.              (2.4)

Therefore, throughout the inherited stationary box,

`boxed: 0 < dPsi/dalpha < 1507/12000`                      (2.5)

because `B/c<5/3`.

### 2.3 Exact micro-continuation

Set

`alpha1 = 12.3196348278`
`       = alpha0 - 1.722e-7`.

The target residual ceiling

`EA = 1.723e-7`

safely includes the inherited `3.7e-11` center uncertainty. With the same exact preconditioner and whole-box Jacobian bounds, the executed rational checker obtains

`eta = 6618813947/40000000000`
`    = 0.165470348675`,

and

`rho = eta/(1-q)`
`    = 6618813947/17440710080`
`    = 0.3795036966178386 < 1`.

Thus the same fixed-point map remains a contraction on the certified box for every target density between `alpha1` and `alpha0`. The Jacobian is invertible there, so the stationary roots form the same `C^1` local branch and the envelope identity applies.

Using (2.5), the comparison value at the new endpoint obeys the exact lower bound

`Psi(alpha1)`
` >= 23584189005311/1090044380000000000000`
`    - (1507/12000)(861/5000000000)`
` = 71804799/6812777375000000000`
` = 1.0539724850468932e-11 > 0`.                            (2.6)

Under the same source-matched stationarized complete-sfl RDT implication used by the inherited directed-interval certificate, the exact-sphere model is therefore asymptotically UNSAT at `alpha1`; monotonicity in the number of constraints yields

`boxed: alpha_c(-1) <= 12.3196348278`.                      (2.7)

This is a strict improvement of `1.22e-8` over the entering endpoint `12.31963484`. Complete-second lifting is now treated as saturated; further digit shaving is not the next substantive route.

### 2.4 Source threshold before / after

Before:

`[6.30297437506, 12.31963484]`, width `6.01666046494`.

After:

`boxed: [6.30297437506, 12.3196348278]`,

width

`boxed: 6.01666045274`.

Source-level width gain:

`boxed: 0.0000000122`.

T03 remains **OPEN / PARTIAL**. This is an upper-bound improvement, not determination of the exact threshold, and it remains subject to the project's later independent review requirement.

## 3. New theorem: outer-tilt entropy as positive variance dissipation

Return to the strict complete-third interior branch

`0<p3<p2<1`, `0<q3<q2<1`, `c2>c3>0`, `gamma_sq,gamma_p>0`.

Use the source-matched notation

`m=c3/c2`, `B=c2/(4 gamma_sq)`,

`X=sqrt(p2-p3) U + sqrt(p3) V - 1`,

`u(x)=log E_H exp[-B(x+sqrt(1-p2)H)_+^2]`.

For fixed `V=v` and `a in [0,m]`, define

`phi_v(a) = log E_U exp[a u(X)]`,

and let `nu_{v,a}` be the corresponding tilted `U` law. The c-sector outer entropy at the final tilt is

`D_U = E_V KL(nu_{V,m} || gamma_U)`.

### Theorem NM07-T03-OUTER-ENTROPY-DISSIPATION

Exactly,

`boxed:`
`D_U = E_V int_0^m a Var_{nu_{V,a}}(u(X)) da`.              (3.1)

### Proof

For fixed `v`,

`KL(nu_{v,a}||gamma_U) = a phi_v'(a)-phi_v(a)`

because `phi_v(0)=0`. Differentiating in `a` gives

`d/da [a phi_v'(a)-phi_v(a)]`
` = a phi_v''(a)`
` = a Var_{nu_{v,a}}(u(X))`.

The entropy vanishes at `a=0`, so integration from `0` to `m` proves (3.1), and averaging over `V` completes the proof. QED.

The key certification feature is that the integrand in (3.1) is pointwise nonnegative. The direct identity

`D_U = m E_V< u >_V - E_V log E_U e^{m u}`

subtracts two quantities of similar size; (3.1) does not.

## 4. New theorem: inner Gaussian entropy as positive score-energy dissipation

Fix `x`, set

`Y=x+sH`, `s^2=1-p2`,

and for `b in [0,B]` define

`psi_x(b)=log E_H exp[-b(Y_+)^2]`.

Let `rho_{x,b}` be the corresponding tilted `H` law. The inner c-sector entropy appearing in NM13-03's entropy form is

`D_H = m E_V < KL(rho_{X,B}||gamma_H) >_V`,

where the outer bracket is the **final** `a=m` tilt.

### Theorem NM07-T03-INNER-ENTROPY-DISSIPATION

Exactly,

`boxed:`
`D_H = m E_V < int_0^B b Var_{rho_{X,b}}((Y_+)^2) db >_V`.  (4.1)

### Proof

For fixed `x`,

`KL(rho_{x,b}||gamma_H)=b psi_x'(b)-psi_x(b)`,

and

`psi_x''(b)=Var_{rho_{x,b}}((Y_+)^2)`.

Therefore

`d/db [b psi_x'(b)-psi_x(b)]`
` = b Var_{rho_{x,b}}((Y_+)^2)`.

At `b=0` the tilted law is the standard Gaussian and the KL divergence is zero. Integrating to `B`, then averaging under the final outer tilt and multiplying by `m`, proves (4.1). QED.

Again the integrand is nonnegative, whereas the direct formula for the KL divergence is a cancellation of `-B E_rho(Y_+)^2` against `-log f`.

## 5. Finite moment recurrence and interval-certificate consequence

The inner variance in (4.1) can be evaluated without a second numerical differentiation. Put

`K_r(x,b)=E_H[(Y_+)^r exp(-b(Y_+)^2)]`,

`f(x,b)=P(Y<=0)+K_0(x,b)`,

`A=1+2b s^2`.

Integration by parts gives the exact recurrence

`K_1 = [x K_0 + s phi(x/s)]/A`,

`K_r = [x K_{r-1} + (r-1)s^2 K_{r-2}]/A`, `r>=2`.         (5.1)

Consequently

`Var_{rho_{x,b}}((Y_+)^2)`
` = K_4/f - (K_2/f)^2`.                                     (5.2)

Equations (3.1), (4.1), and (5.1)--(5.2) give a cancellation-free c-sector compiler. In the entropy formulation of the two source c-stationarity equations, use

`R_U = A_c3 - alpha D_U/c3^2`,

`R_H = A_c2 - alpha D_H/(c2 c3)`.                           (5.3)

The only new integration variables are one-dimensional `a in [0,m]` and `b in [0,B]`, and every entropy integrand is nonnegative. This is directly complementary to NM13-03's transport-LSI cage: the LSI theorem supplies cheap algebraic outer bounds, while (3.1)/(4.1) supply a stable positive exact representation on the small boxes that survive pruning.

This attacks the named third-full obstruction more directly than evaluating the nested KL expressions themselves. A directed interval implementation can enclose the positive integrands with the same closed Gaussian kernel/moment tower already used by the overlap equations, subdivide only where necessary, and then feed `(R3,R2,R_U,R_H)` to the existing four-overlap positive-gap Krawczyk formulation.

### Numerical-only falsification check

I evaluated both sides of (3.1) and (4.1) independently at the previously archived `delta=10^-3` waypoint (`alpha ~= 12.31643335693`). This is **NUMERICAL_ONLY** and is not used in the source endpoint of Section 2.

At quadrature orders 40, 60, and 80 the direct and dissipation forms agree as follows:

- order 40: `D_U=0.0442057663102661`, difference `-2.082e-17`; `D_H=0.0347008915783486`, difference `-9.021e-17`;
- order 60: `D_U=0.0442057025101657`, difference `-2.359e-16`; `D_H=0.0347010631274716`, difference `-1.041e-16`;
- order 80: `D_U=0.0442057044885399`, difference `+1.943e-16`; `D_H=0.0347010574381123`, difference `+1.388e-17`.

The agreement is only a self-check of the identities and implementation; it is not an interval root certificate. The third-full waypoint therefore remains **CONDITIONAL**.

## 6. What moved, what did not, and next attack

### Source-threshold movement

Strict movement:

`alpha_U: 12.31963484 -> 12.3196348278`.

Lower endpoint unchanged:

`alpha_L = 6.30297437506`.

### Demonstrated mechanism gain

The new exact third-full gain is independent of that microscopic complete-second continuation:

1. both c-sector entropies are now positive variance-dissipation integrals;
2. the difficult inner entropy needs only the finite moments `K_0,...,K_4`, generated by the exact recurrence (5.1);
3. direct cancellation in `m QM-Q` and the inner `B u_B-u` entropy expression is eliminated;
4. NM13-03's new LSI cages and the present positive integrals form a two-stage rigorous enclosure strategy for the exact four-overlap positive-gap system.

### Residual obstruction

No outward-rounded four-dimensional root inclusion has yet been executed at the `delta=10^-3` third-full waypoint. Therefore

`alpha ~= 12.31643335693`

remains **CONDITIONAL** and is not entered into the source bracket.

### Next attack

Do **not** spend another run shaving complete-second decimals. Build the actual third-full interval evaluator around the `delta=10^-3` overlap point. Use NM13-03's algebraic LSI inequalities to prune/subdivide the outer box; use (3.1)/(4.1) plus the exact `K_r` recurrence for the final c-sector enclosure; then run a weighted Krawczyk or contraction inclusion on `(R3,R2,R_U,R_H)`. A successful inclusion would automatically have `Psi3=10^-3` by the already proved positive-gap compiler and would move the exact-sphere upper endpoint from `12.3196348278` to approximately `12.31643335693`, a non-microscopic gain of about `0.00320147`.

## 7. Executed artifacts

Essential source:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_entropy_dissipation_sharp_micro.py`

Essential archived output:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_entropy_dissipation_sharp_micro.out`

The exact section ends `EXACT_MICROCONTINUATION_PASS`; the entire archived output ends `ALL_EXACT_CHECKS_PASS` and `ALL_NUMERICAL_DISSIPATION_CHECKS_PASS`. The numerical entropy-dissipation lines are explicitly labeled numerical-only.

## 8. `ledger_delta`

```yaml
ledger_delta:
  worker: NM13-07
  target: T03
  source_model: "kappa=-1; iid Gaussian constraints; ||sigma||_2=sqrt(N) exactly"
  status: PARTIAL
  source_threshold_before:
    alpha_L: "6.30297437506"
    alpha_U: "12.31963484"
    width: "6.01666046494"
  source_threshold_after:
    alpha_L: "6.30297437506"
    alpha_U: "12.3196348278"
    width: "6.01666045274"
  source_gain: "1.22e-8 on the upper endpoint"
  mechanism_gain:
    - "Exact outer c-sector entropy representation D_U = E int_0^m a Var_{nu_a}(u) da"
    - "Exact inner c-sector entropy representation D_H = m E< int_0^B b Var_{rho_b}(Y_+^2) db >"
    - "Exact K_0..K_4 recurrence for the inner positive variance integrand"
    - "Sharper exact Gaussian moment bound E[(G-1)_+^2] < 1507/20000"
  third_full_waypoint:
    status: CONDITIONAL
    delta: "1e-3"
    alpha_numerical: "12.3164333569308"
  residual_obstruction: "Outward-rounded 4D root inclusion for (R3,R2,R_U,R_H)"
  next_attack: "LSI-pruned positive-integral interval evaluator plus weighted 4D Krawczyk at the delta=1e-3 waypoint"
  runtime_model: "GPT-5.6 Sol"
  runtime_reasoning: "UNVERIFIED"
```
