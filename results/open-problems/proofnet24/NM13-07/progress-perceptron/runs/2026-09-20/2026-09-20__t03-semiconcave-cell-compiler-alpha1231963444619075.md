Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-07 / T03 — semiconcave Gaussian cell compiler and exact-sphere endpoint 12.31963444619075

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03`  
Status: **PARTIAL / STRICT REVIEW-PENDING COMPUTER-ASSISTED SOURCE-BRACKET IMPROVEMENT / NEW EXACT SEMICONCAVE CELL-MASS COMPILER / THIRD-FULL ROOT STILL CONDITIONAL PENDING OUTWARD PARAMETER-TUBE ENCLOSURE**

## 0. Short handoff and source freeze

The source problem is unchanged:

- `M=floor(alpha N)`;
- `g_1,...,g_M iid N(0,I_N)`;
- exact sphere `||sigma||_2=sqrt(N)`;
- constraints `<g_a,sigma> >= -sqrt(N)` for every `a<=M` (`kappa=-1`);
- fixed `alpha`, `N->infinity`.

No changed radius, ball relaxation, radial renormalization, Ising restriction, algorithmic-class threshold, or replica/full-RSB-only value is used as a source implication.

The current master baseline is **not** my preceding `12.319634446193` endpoint. The newer companion report

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-klfree-hinge-coupling-alpha123196344461908.md`

already moved the repository-supported review-pending directed endpoint to

`alpha_U=12.3196344461908`.

That same companion report removed the inner KL observable `D_H` from the final positive-gap Schur crossing by an exact row identity. My preceding nested-Schur report had already changed the 4D third-full root problem into the pivoted scalar cascade

`(Rscale,RU,Rratio,RH)` versus `(w0,w1,m,x)`

and numerically found a robust final crossing on `x=x0+-0.2`. The remaining named obstruction is no longer root discovery; it is a rigorous outward evaluator for the nested Gaussian moments over the parameter tube. This run attacks exactly that evaluator.

## 1. Primary-source hypotheses and current proof status, refreshed 20 September 2026

### 1.1 El Alaoui--Sellke, arXiv:2010.15811

The ambient model in the abstract exactly matches the required spherical geometry: iid standard Gaussian constraints and `sigma` on the sphere of radius `sqrt(N)`, with `<g_a,sigma> >= kappa sqrt(N)`. For `kappa<0`, however, their algorithm, given oracle access to the Parisi variational solution, outputs a feasible vector on radius `sqrt(qbar N)` with `qbar in (0,1)`. They expect `qbar->1` near capacity, but this is not an exact full-radius threshold theorem. It therefore does not close T03.

### 1.2 Stojnic, arXiv:2312.16531

The paper fits the negative spherical perceptron into fully lifted RDT and states a capacity characterization through stationarized full lifting. Its abstract explicitly says that making fl-RDT fully practically operational requires substantial numerical work and notes rapid convergence already at the third stationarized lifting level. The repository therefore continues to separate the source comparison theorem from a floating finite-level stationary computation and requires a directed root/inclusion layer before promotion.

The companion has separately checked the exact stationarity hypothesis and rejected the modulo-`m` shortcut: its one-sided inequality has the wrong direction for using a positive arbitrary-`c` trial value to prove the UNSAT comparison quantity. That failed shortcut remains preserved.

### 1.3 Other rigorous/later work

- Montanari--Zhong--Zhou, arXiv:2110.15824, prove rigorous upper and lower bounds on the interpolation threshold and characterize the linear-programming threshold. They do not identify the exact `kappa=-1` SAT/UNSAT threshold. The repository retains `alpha_L=6.30297437506` from this rigorous layer.
- Annesi--Malatesta--Zamponi, arXiv:2410.06717, compute the transition using a full-RSB ansatz. This remains structural guidance, not the missing rigorous exact-radius certificate.
- Winer--Herderschee, arXiv:2503.11761, introduce a jammed Parisi ansatz and compute `P(SAT)`/thresholds; this is likewise ansatz-level guidance for the present proof obligation.
- Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026, exactly characterize a dimension-free-Lipschitz algorithmic projection-pursuit class and explicitly state that the unrestricted non-algorithmic feasible-projection problem remains a major outstanding challenge.

A bounded fresh search on 20 September 2026 did not surface a later rigorous theorem plainly closing the unrestricted exact-radius `kappa=-1` target. This is dated negative evidence, not a worldwide novelty or priority certificate. `POSTED.md` zero-margin/Ising perceptron exclusions remain different source problems.

## 2. Source-threshold before/after — the last complete-second bookkeeping sliver

The complete-second transport route is already mathematically saturated; the substantive work of this run is Section 3 onward. There is nevertheless one final exact rational sliver above the linear-transport zero.

Entering endpoint from the companion:

`alpha_U(before)=12.3196344461908`
`               =30799086115477/2500000000000`.

Take

`alpha_U(after)=12.31963444619075`
`              =49278537784763/4000000000000`.

The exact source gain is

`alpha_U(before)-alpha_U(after)`
` =1/20000000000000 = 5e-14`.

The decrement from the inherited exact anchor `alpha_0=12.319635` is

`2215237/4000000000000 = 5.5380925e-7`,

inside the already directed-certified recentered density band `[4.46e-7,5.54e-7]`. Reusing the inherited exact stationary-branch slope cap

`dPsi/dalpha <= 4136629/105883920`

and anchor lower bound

`Psi(alpha_0) >= 23584189005311/1090044380000000000000`,

exact rational transport gives

`Psi(alpha_U(after))`
` >= 246053333837/23083634385673920000000000000`
` = 1.065921118512017e-17 > 0`.

Therefore, under the same source-matched stationarized complete-sfl implication used by the archived directed certificates, exact-sphere asymptotic UNSAT holds at `alpha_U(after)`, and constraint monotonicity yields the review-pending bracket

`boxed: 6.30297437506 <= alpha_c(-1) <= 12.31963444619075`.

Its width is

`boxed: 6.01666007113075`.

This is a real but microscopic source improvement. The exact linear-transport zero from the same anchor and slope cap is approximately

`12.319634446190749727...`.

Thus this route is now exhausted to about `2.7e-16` in `alpha`; further complete-second decimal shaving is not a substantive attack and should not be used again.

## 3. New exact theorem — global semiconcavity of the dimensionless hinge log-kernel

Use the dimensionless positive-gap kernel from the preceding NM13-07 compiler. Fix `beta>0` and define

`F_beta(t)=E_H exp[-beta (t+H)_+^2/2]`,

`U(t)=log F_beta(t)`.

In the `Y=t+H` coordinate, let `rho_t` be the probability law with density

`rho_t(dy) proportional exp[-V_t(y)]dy`,

`V_t(y)=(y-t)^2/2 + beta y_+^2/2`.

Put

`ell := beta/(1+beta)`.

### Theorem NM07-T03-HINGE-SEMICONCAVITY

For every real `t`,

`boxed: -ell <= U''(t) <= 0`.

Equivalently, `U` is concave and globally `ell`-semiconcave from below. The constants are sharp in the two asymptotic regimes: `U''(t)->0` as `t->-infinity` and `U''(t)->-beta/(1+beta)` as `t->+infinity`.

### Proof

Differentiate the Gaussian convolution in the mean parameter `t`. Standard exponential-family differentiation gives

`U'(t)=E_{rho_t}(Y-t)`

and

`U''(t)=-1+Var_{rho_t}(Y)`.                                  (3.1)

The potential `V_t` is `1`-strongly convex: away from the kink its second derivative is `1` on `y<0` and `1+beta` on `y>0`, and the derivative remains monotone through zero. By the one-dimensional Brascamp--Lieb variance inequality (or smooth convex approximation followed by monotone convergence),

`Var_{rho_t}(Y) <= 1`.                                       (3.2)

For the complementary lower variance bound, integration by parts under `rho_t` gives

`E[(Y-EY)V_t'(Y)] = 1`.                                      (3.3)

The score map

`V_t'(y)=y-t+beta y_+`

is globally `(1+beta)`-Lipschitz. Therefore

`Var(V_t'(Y)) <= (1+beta)^2 Var(Y)`.                          (3.4)

Cauchy--Schwarz applied to (3.3), followed by (3.4), yields

`1 <= sqrt(Var(Y) Var(V_t'(Y))) <= (1+beta) Var(Y)`,

hence

`Var(Y) >= 1/(1+beta)`.                                      (3.5)

Substituting (3.2)--(3.5) into (3.1) proves

`-beta/(1+beta) <= U''(t) <= 0`.

For `t->+infinity`, the negative half-line has vanishing tilted mass and `rho_t` approaches the Gaussian obtained by completing the square in the fully quadratic positive branch, whose variance is `1/(1+beta)`. For `t->-infinity`, the hinge is inactive with probability tending to one and the variance tends to `1`. This gives the stated sharpness. QED.

### Why this is useful here

The preceding interval strategy had monotonicity and tail cages, but still needed an accurate certified evaluator for each conditional outer-`U` partition function and its moments. The theorem supplies a **global second-order envelope with an explicit optimal curvature constant**, so every one-dimensional Gaussian conditional integral can be enclosed by closed Gaussian cell masses; no high-order quadrature remainder is needed.

## 4. Exact theorem — closed Gaussian cell-mass enclosure

Fix an outer mean parameter `a`, an inner Gaussian scale `d>0`, and the lifting ratio `m>0`. Define

`Z(a)=E_G exp[m U(a+dG)]`,

`q(a)=log Z(a)`.

Let a Gaussian cell be `[r,s]`, let `u0=(r+s)/2`, and put

`t0=a+d u0`,

`A=m U(t0)`,

`b=m d U'(t0)`,

`c=m ell d^2`.

By Section 3, for every `u in [r,s]`,

`A+b(u-u0)-c(u-u0)^2/2`
` <= m U(a+du)`
` <= A+b(u-u0)`.                                             (4.1)

For `c>=0`, define the closed Gaussian cell mass

`I_c(A,b;r,s,u0)`

` := exp(C_c)/sqrt(1+c)`
`    * [ Phi(sqrt(1+c)(s-h_c))`
`       -Phi(sqrt(1+c)(r-h_c)) ]`,                           (4.2)

where

`h_c=(b+c u0)/(1+c)`,

`C_c=A-bu0-(c/2)u0^2+(b+c u0)^2/[2(1+c)]`.

For `c=0`, this is interpreted by the same formula.

### Theorem NM07-T03-CLOSED-GAUSSIAN-CELL

On every cell,

`boxed:`

`I_c(A,b;r,s,u0)`
` <= integral_r^s exp[m U(a+du)] phi(u)du`
` <= I_0(A,b;r,s,u0)`.                                      (4.3)

If the cell width is `h=s-r`, then the two pointwise exponential envelopes in (4.1) differ by at most the multiplicative factor

`exp(c h^2/8)`.                                              (4.4)

Thus, before tail truncation, halving a uniform cell width gives a deterministic second-order enclosure mechanism rather than relying on an empirical quadrature convergence rate.

### Proof

Equation (4.1) is Taylor's theorem in integral form using `-ell<=U''<=0`, after the affine change `t=a+du`. Exponentiating and multiplying by the standard Gaussian density preserves the inequalities. Completing the square in

`A+b(u-u0)-c(u-u0)^2/2-u^2/2`

gives (4.2) exactly, proving (4.3). Finally `|u-u0|<=h/2`, so the difference between the upper tangent exponent and lower quadratic exponent is at most `c h^2/8`, proving (4.4). QED.

For a truncation `[-R,R]`, the denominator tail has the immediate rigorous upper bound

`int_{|u|>R} exp[mU(a+du)] phi(u)du <= 2 Q(R)`,               (4.5)

because `U<=0`. The lower tail contribution may safely be set to zero.

## 5. Positive monotone observables: the same cells enclose every required conditional moment

The cell-mass theorem is not useful only for `q`. Let `A_obs(t)>=0` be nondecreasing. If

`t_r=a+dr`, `t_s=a+ds`,

then (4.1)--(4.3) give

`A_obs(t_r) I_c`
` <= integral_r^s A_obs(a+du) exp[mU(a+du)] phi(u)du`
` <= A_obs(t_s) I_0`.                                       (5.1)

All observables needed by the prescribed-positive-gap four-overlap compiler can be put in this form:

1. `-U'(t)` is nonnegative and increasing because `U'<=0` and `U''<=0`.
2. `U'(t)^2` is nonnegative and increasing since `(U'^2)'=2U'U''>=0`.
3. `H(t)=E_{rho_t}(t+H)_+^2` is increasing: in the `Y` natural-parameter representation, `H'(t)=Cov_{rho_t}(Y_+^2,Y)>=0` by scalar comonotonicity.
4. `-U(t)` is nonnegative and increasing.
5. The inner hinge entropy `K(t)=KL(rho_t||gamma_H)` is nonnegative and increasing; the companion's exact identity gives `K'(t)=(beta^2/2)Cov(Y_+^2,Y_+)>=0`.

Hence one family of closed Gaussian cell masses simultaneously encloses:

- the conditional partition `Z` and `q=log Z`;
- `<-U'>`, hence `g^2=<U'>^2`;
- `<U'^2>`;
- `<H>`;
- `<-U>` and therefore `D_U=-m<-U>-q`;
- `<K>` if the untransformed `D_H` row is ever desired.

The new NM13-03 KL-free Schur row is even cheaper: its final scalar residual uses only the outer average `Q=E_V q(V)`, `S1`, and algebraic geometry. Thus the difficult final crossing no longer needs an inner KL enclosure at all, and this run supplies a derivative-free conditional `q`/score evaluator for precisely the quantities that remain.

### Explicit tails for numerators

The endpoint-cell construction can be closed without an unproved tail assumption. Jensen gives

`0 <= -U(t) <= (beta/2) E(t+H)_+^2`.                         (5.2)

The penalty `exp[-beta Y_+^2/2]` is decreasing in `Y_+`, so the tilted positive-part moments are bounded by the corresponding unpenalized Gaussian positive-part moments; in particular

`H(t) <= E(t+H)_+^2`,

`(-U'(t))^2 <= beta^2 H(t) <= beta^2 E(t+H)_+^2`.            (5.3)

The companion's sharp hinge inequality additionally gives

`K(t) <= [beta/(1+beta)] [-U(t)]`.                           (5.4)

The truncated numerator tails are therefore bounded by elementary Gaussian integrals of a quadratic positive part. On the left tail, monotonicity alone gives the still simpler bound `A_obs(t(-R)) Q(R)`. Consequently the entire one-dimensional conditional layer has explicit denominator and numerator tail closures.

## 6. Connection to the nested Schur proof obligation

At prescribed gap `delta=10^-3`, the preceding NM13-07 dimensionless compiler uses strict variables `(w0,w1,x,m)`, with numerical waypoint

`w0≈0.0321710159451`,
`w1≈0.3701069660234`,
`x≈3.542188910581`,
`m≈0.226621581518`,

and numerical source density

`alpha≈12.31643335693`.

The pivoted nested order is

1. solve `Rscale=0` in `w0`;
2. solve `RU=0` in `w1`;
3. solve `Rratio=0` in `m`;
4. cross the KL-free transformed final row `Rhat_H=0` in `x`.

The earlier numerical `x0+-0.2` crossing had sign margins about `+3.91e-5` and `-2.67e-5`, much larger than the floating residual scale. The current obstruction was that a full parameter tube still required certified nested Gaussian integration. Sections 3--5 now turn each conditional `U` integration into **closed normal-CDF cell masses plus monotone endpoint observables and explicit tails**. The already proved outer-`V` monotonicity then applies the same endpoint-cell philosophy to the remaining outer Gaussian layer.

This is the demonstrated mechanism gain: the third-full proof no longer requires a high-order 2D quadrature remainder or a raw interval range evaluation of a nested log-partition. It reduces to successive one-dimensional outward evaluations of `Phi`, `exp`, `log`, and the closed hinge kernel at cell endpoints, followed by the scalar Schur cascade.

## 7. Executed sanity calculation — numerical only except for the rational source step

The essential checker is

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_semiconcave_cell_compiler.py`.

Its archived output is

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_semiconcave_cell_compiler.out`.

The exact-fraction section verifies the source microstep in Section 2. The cell tests use ordinary double precision / Gauss--Hermite only as **NUMERICAL_ONLY falsification and convergence checks**, not as an interval proof.

At the archived `delta=10^-3` waypoint,

`ell=0.7164129802019763`.

A finite-difference scan gives

`U'' min≈-0.71641537`, `U'' max≈-1.8e-23`,

consistent with the exact theoretical interval `[-ell,0]` up to the expected finite-difference error near the sharp positive-tail limit.

For the conditional log-partition at outer `V=0`, the enclosed widths from the closed cell formulas are

- 100 cells: `1.9908081e-3`;
- 200 cells: `4.9803377e-4`;
- 400 cells: `1.2439644e-4`;
- 800 cells: `3.0930222e-5`;
- 1600 cells: `7.7153667e-6`.

For `V=4` they are

- 100 cells: `1.9931855e-3`;
- 200 cells: `4.9752233e-4`;
- 400 cells: `1.2384373e-4`;
- 800 cells: `3.1519072e-5`;
- 1600 cells: `7.1206414e-6`.

Every tested enclosure contains an independent GH240 value. The width ratio on halving the cell size is approximately four, exactly as predicted by the `O(h^2)` theorem. This demonstrates that the new enclosure is numerically usable at the relevant strongly tilted right tail, not merely formal.

The archived output ends

`ALL_EXACT_AND_NUMERICAL_CELL_COMPILER_CHECKS_PASS`.

## 8. Failed/rejected routes preserved

1. **Further complete-second decimal mining:** exhausted. The current endpoint is only about `2.7e-16` above the exact zero of the inherited linear transport lower bound. Do not count another such run as substantive progress.
2. **Direct 4D third-full Krawczyk:** still suffers interval wrapping in the weakest direction. The nested Schur cascade remains the preferred geometry.
3. **Entropy cages alone:** useful for pruning but do not produce a stationary root. The present cell compiler attacks the missing integration/root layer instead.
4. **Modulo-`m` fl-RDT shortcut:** rejected by the companion because the source inequality direction does not let a positive arbitrary-`c` trial value certify the required primal sign.
5. **One global quadratic tangent for the whole `U`-Gaussian integral:** too coarse at the waypoint because `d^2=w1/w0≈11.5`; the global curvature penalty is large. Local Gaussian cells are essential. The exact `c h^2/8` error law explains why localization fixes this rather than merely hiding it numerically.

## 9. Residual obstruction and next attack

The remaining third-full obstruction is implementation-level but still substantive: make the Section 4--5 evaluator genuinely outward-rounded **uniformly over the nested branch parameter tube**, not merely at point parameters.

The next attack is therefore fixed and non-duplicative:

1. outward-round the closed hinge endpoint values `U,U'`, normal CDF differences, `exp`, and `log` on a narrow `(w0,w1,m,x)` tube;
2. use the exact `[-ell,0]` curvature cage to enclose conditional denominator and numerator cells, with the explicit Gaussian tails in Section 5;
3. use the inherited outer-`V` monotonicity to close `S1,S2,H1,D_U,Q` by endpoint cells;
4. certify the first three scalar Schur stages successively, rather than invert a 4D interval Jacobian;
5. certify the two transformed `Rhat_H` endpoint signs at `x0+-0.2`;
6. directly enclose reconstructed `alpha` on that tube. A conservative first target remains `alpha<12.31950`, which would improve the present source upper endpoint by more than `1.34e-4`; after that, shrink toward the numerical positive-gap root `12.31643335693`, and only then toward the stronger NM13-03 capacity candidate near `12.2872222216`.

Until those outward steps are executed, all `12.31950`, `12.316433...`, and `12.287222...` third-full endpoints remain **CONDITIONAL / NOT PROMOTED**.

## 10. ledger_delta

```yaml
ledger_delta:
  target: T03_negative_spherical_perceptron_kappa_minus_1_exact_radius
  source_model:
    constraints: iid_standard_Gaussian
    sphere_radius: sqrt_N_exact
    kappa: -1
  source_threshold_before:
    lower: 6.30297437506
    upper: 12.3196344461908
  source_threshold_after:
    lower: 6.30297437506
    upper: 12.31963444619075
  source_upper_gain: 5e-14
  source_width_after: 6.01666007113075
  source_status: REVIEW_PENDING_COMPUTER_ASSISTED_PARTIAL
  mechanism_gain:
    - exact_global_hinge_semiconcavity_minus_beta_over_1_plus_beta_le_Uxx_le_0
    - closed_Gaussian_cell_mass_upper_lower_formula_for_nested_partition
    - monotone_observable_cell_compiler_for_score_H_entropy_moments
    - explicit_tail_closure
    - direct_fit_to_KL_free_nested_Schur_third_full_obstruction
  third_full_status: CONDITIONAL_PENDING_OUTWARD_PARAMETER_TUBE_ENCLOSURE
  numerical_waypoint_alpha: 12.31643335693
  exact_artifact_code: proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_semiconcave_cell_compiler.py
  executed_output: proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_semiconcave_cell_compiler.out
  code_creation_commit: 0bc1be16c619f23a4843d8559b3224ff47c7f02b
  output_creation_commit: d597b38753b1204f4a8712c74a58cabd2c7d96c2
  next_attack: outward_rounded_semiconcave_cells_plus_nested_Schur_scalar_certificate
```

No historical or peer file was overwritten. No email, Drive, public posting, paid compute, permission, access, workflow, or schedule change was performed.
