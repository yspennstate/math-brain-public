Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated as the applied reasoning setting.**

# NM13-07 / T03 — monotone third-full c-sector compiler and sharp complete-second tangent endpoint 12.3196344462

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03`  
Status: **PARTIAL / STRICT COMPUTER-ASSISTED SOURCE-BRACKET IMPROVEMENT / NEW THIRD-FULL MONOTONE-KL COMPILER / PENDING LATER INDEPENDENT REVIEW**

## 0. Short handoff and frozen source problem

The exact source problem is unchanged:

- `M=floor(alpha N)`;
- `g_1,...,g_M iid N(0,I_N)`;
- `||sigma||_2=sqrt(N)` exactly;
- `<g_a,sigma> >= -sqrt(N)` for every `a<=M`;
- fixed `alpha`, `N->infinity`.

No changed radius, ball relaxation, Ising restriction, radial rescaling, replica-only value, or algorithmic threshold is used as a source implication.

The entering repository-supported, review-pending directed bracket is

`alpha_L = 6.30297437506`,

`alpha_U = 12.31963446`,

width `6.01666008494`.

The latest NM13-03 companion report `2026-09-20__t03-stein-hsi-alpha1228722222161.md` supports a stronger complete-third **CONDITIONAL / numerical** point at `alpha=12.28722222161`, but still lacks the outward four-overlap root inclusion needed for a source endpoint. The preceding NM13-07 run already showed that complete-second digit shaving was essentially saturated and redirected substantive effort to the complete-third certification obstruction.

This run therefore uses the complete-second branch only to obtain a small but strict source movement, while the main mathematical advance is a new exact monotonicity/stochastic-order compiler for both complete-third c-sector KL terms. It removes the outer-`V` derivative burden from their compact quadrature and sharply improves the previous `D_H` tail envelope.

## 1. Primary-source hypotheses and current proof status, refreshed 20 September 2026

1. **El Alaoui--Sellke, arXiv:2010.15811.** Their model is exactly the iid-Gaussian spherical perceptron on radius `sqrt(N)`, with `<g_a,sigma> >= kappa sqrt(N)`. For `kappa<0`, the algorithm in the abstract outputs on radius `sqrt(qbar N)` with `qbar in (0,1)` and relies on the Parisi/FRSB description; the authors expect `qbar->1` near capacity. This is not an exact-radius threshold theorem and cannot close T03.
2. **Stojnic, arXiv:2312.16531.** Theorem 2 assumes the complete stationarized fully lifted RDT setup and requires the non-fixed lifting parameters to solve the stationarity system before the complete-sfl identity is applied. Section 4.2 then says the theorem becomes operational once the underlying numerical evaluations are carried out. The present project therefore keeps the source comparison theorem separate from floating finite-lift stationary points and supplies directed inclusion layers before promoting source endpoints.
3. **Montanari--Zhong--Zhou, arXiv:2110.15824.** They rigorously prove upper and lower information-theoretic bounds on the negative-perceptron interpolation threshold and characterize the linear-programming threshold, but do not identify the exact `kappa=-1` satisfiability threshold. The repository-retained rigorous SAT-side lower endpoint remains `6.30297437506`.
4. **Annesi--Malatesta--Zamponi, arXiv:2410.06717.** Their transition value is computed under a full-RSB ansatz. It remains structural guidance, not a replacement rigorous exact-sphere certificate.
5. **Winer--Herderschee, arXiv:2503.11761.** The paper proposes a jammed Parisi ansatz and reports spherical-perceptron SAT probabilities/threshold agreement. It is again ansatz-level guidance rather than the missing directed exact-radius proof.
6. **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** They exactly characterize a dimension-free Lipschitz algorithmic projection-pursuit class and explicitly distinguish the unrestricted non-algorithmic feasible-projection problem as still open/challenging.

A bounded fresh search on 20 September 2026 did not surface a later rigorous theorem plainly closing the unrestricted exact-radius `kappa=-1` target. This is dated negative evidence, not a novelty/priority certificate.

## 2. Source-threshold before/after — exact sharp tangent transport

The previous complete-second directed rectangle supplies the rational derivative boxes

`H_p in [-3371/100000,-2828/100000]`,

`H_B in [3284/10^7,5044/10^7]`,

`alpha_p in [24671/1000,25288/1000]`,

`alpha_B in [-60244/10^5,-6008/10^4]`,

`Psi_p in [8701/10^4,8955/10^4]`,

`Psi_B in [-2137/10^5,-2115/10^5]`.

For a stationary branch `F=(H,alpha-a)=0`, put

`Delta = H_p alpha_B-H_B alpha_p`,

`N = -Psi_p H_B+Psi_B H_p`.

Then implicit differentiation gives

`dPsi/da = N/Delta`.

The preceding run used the convenient cap `1/25`. Here I compute the **best cap obtainable from the same independent derivative box by the multi-affine vertex argument**.

Exact enumeration of the 64 vertices gives

`Delta >= 1323549/312500000 = 0.0042353568 > 0`,

`N >= 732159/5000000000 = 0.0001464318 > 0`,

and the largest vertex ratio is exactly

`S_* = 4136629/105883920`

`    = 0.03906758457752603...`.

For fixed `S_*`, the function `N-S_* Delta` is multi-affine in the six interval variables. It is `<=0` at every vertex (with equality at one vertex), hence on the whole hyperrectangle. Since `Delta>0`,

`boxed: 0 < dPsi/da <= 4136629/105883920 < 1/25`.              (2.1)

This is an exact theorem on the already directed box, not interval division.

### Recentered existence chart

Reuse the previous midpoint-inverse predictor centered at density decrement `5e-7`. The new weighted box has

`r_B=2.1e-6`, `r_B/r_p=42.5`,

is contained in the old directed rectangle, and has exact contraction constant

`q = 229179741/467259059 = 0.4904768277590526`.

Enlarging the density half-band to `5.4e-8` around the predictor center covers both the old endpoint and the new target below. Exact fundamental-theorem-of-calculus residual propagation gives

`eta = 18671401519768819/40795417037192166`

`    = 0.4576838006765948`,

while

`1-q = 238079318/467259059 = 0.5095231722409473`.

Therefore

`rho = eta/(1-q)`

`    = 317413825836069923/353365575128603244`

`    = 0.8982590500519212 < 1`.

Banach contraction supplies a genuine stationary zero for every density in the covered band, in particular at

`alpha_1 = 12.3196344462`

with decrement from the certified anchor `alpha_0=12.319635`

`delta = 2769/5000000000 = 5.538e-7`.

The previously certified anchor objective obeys

`Psi(alpha_0) >= 23584189005311/1090044380000000000000`.

Using (2.1),

`Psi(alpha_1)`

` >= Psi(alpha_0)-S_* delta`

` >= 173793709614263/480909049701540000000000000`

` = 3.613858165533009e-13 > 0`.                              (2.2)

The old rectangle also has `H_p<0`, `H_B>0`, `Delta>0`, so the stationary zero is on the same unique branch already connected to the anchor. Under the previously source-matched stationarized complete-sfl comparison implication, (2.2) gives exact-sphere asymptotic UNSAT at `alpha_1`; constraint monotonicity gives the new source upper endpoint.

Hence the review-pending source bracket moves strictly from

`[6.30297437506, 12.31963446]`

to

`boxed: [6.30297437506, 12.3196344462]`.

The width moves from

`6.01666008494`

to

`6.01666007114`,

a strict source gain of

`69/5000000000 = 1.38e-8`.

This exhausts the present complete-second transport information almost completely: the limiting endpoint obtainable from the same anchor lower bound and the exact box cap `S_*` is approximately `12.319634446190749`; the new endpoint is only about `9.25e-12` above it. Further same-box decimal shaving is not a substantive next attack.

## 3. New third-full theorem — monotone c-sector KL compiler

Use the strict complete-third notation

`0<p3<p2<1`, `0<q3<q2<1`, `c2>c3>0`,

`m=c3/c2`, `d^2=p2-p3`, `s^2=1-p2`, `B=c2/(4 gamma_sq)`.

For independent standard Gaussians `U,V,H`, define

`a(v)=sqrt(p3) v-1`,

`X=a(v)+d U`,

`f(x)=E_H exp[-B(x+sH)_+^2]`, `u(x)=log f(x)`.

Let `rho_x` be the inner tilted `H` law

`d rho_x/d gamma_H = exp[-B(x+sH)_+^2]/f(x)`

and write

`K(x)=KL(rho_x || gamma_H)`.

For fixed `v`, let `nu_v` be the outer tilted `U` law

`d nu_v/d gamma_U = exp[m u(a(v)+dU)]/Z_v`.

Define the two conditional c-sector entropy integrands

`D_U(v)=KL(nu_v || gamma_U)`,

`D_H(v)=m E_{nu_v} K(a(v)+dU)`.

The full c-sector entropies are the standard-Gaussian `V` averages of these functions.

### Theorem NM07-T03-MONOTONE-CSECTOR

For every strict-domain parameter tuple above:

1. `D_U(v)` and `D_H(v)` are nonnegative and nondecreasing functions of `v`.
2. Put `sigma^2=1-p3=d^2+s^2` and

   `T_sigma(a)=E(a+sigma G)_+^2`

   `=[a^2+sigma^2] Phi(a/sigma)+a sigma phi(a/sigma)`.

   Then both conditional entropies obey the same pointwise envelope

   `boxed: 0 <= D_U(v), D_H(v) <= m B T_sigma(a(v)).`          (3.1)
3. Consequently, for any mesh `L=v_0<...<v_n=R`, with

   `omega_i=Phi(v_{i+1})-Phi(v_i)`,

   each `D` equal to either `D_U` or `D_H` satisfies the derivative-free compact enclosure

   `sum_i omega_i D(v_i)`

   ` <= int_L^R D(v) phi(v) dv`

   ` <= sum_i omega_i D(v_{i+1})`.                            (3.2)

   The left tail is bounded by `Phi(L)D(L)`. The right tail has the explicit polynomial envelope

   `int_R^infinity D(v)phi(v)dv`

   ` <= mB {p3 R phi(R)-2 sqrt(p3) phi(R)+2 Q(R)}`.           (3.3)

Thus the outer `V` integration of **both** cancellation-sensitive c-sector KL terms can be certified by one-dimensional endpoint evaluations and exact Gaussian cell masses; no `V`-derivative or high-order two-dimensional quadrature remainder is needed.

### Proof

The kernel `y -> exp[-B y_+^2]` is nonincreasing and log-concave. Gaussian convolution preserves log-concavity, so `u` is nonincreasing and concave:

`u_x<=0`, `u_xx<=0`.

For the inner entropy, put `W=(x+sH)_+`. Since

`K(x)=-B E_{rho_x} W^2-u(x)`,

differentiating the exponential family gives

`K'(x)=B^2 Cov_{rho_x}(W^2,2W)`.

The functions `W^2` and `W` are comonotone, hence their covariance is nonnegative. Therefore

`K'(x)>=0`.                                                        (3.4)

For the outer entropy, viewing `a` as the parameter and writing `nu_a` for `nu_v`,

`D_U(a)=m E_{nu_a}u(a+dU)-log Z_a`.

Differentiation gives the exact cancellation

`dD_U/da=m^2 Cov_{nu_a}(u,u_x)`.                                (3.5)

Because both `u` and `u_x` are nonincreasing functions of their scalar argument, their covariance is nonnegative. Hence `D_U` is nondecreasing in `a`, and therefore in `v`.

For `D_H`, write the law of `X` under `nu_a` as

`d mu_a(x) proportional exp[m u(x)] exp[-(x-a)^2/(2d^2)] dx`.

If `a_2>a_1`, then

`d mu_{a_2}/d mu_{a_1}(x)=C exp[(a_2-a_1)x/d^2]`,

which is increasing in `x`. Thus the family is increasing in monotone-likelihood-ratio order, hence in first-order stochastic order. Since `K` is nondecreasing by (3.4), `E_{mu_a}K` is nondecreasing. This proves part 1.

For the common envelope, Jensen first gives

`u(x)=log E_H exp[-B W^2] >= -B E_H W^2`.                       (3.6)

Also

`K(x)=-B E_{rho_x}W^2-u(x) <= -u(x)`.                           (3.7)

For `D_U`, since `u<=0`,

`D_U=m E_{nu_a}u-log Z_a <= -log Z_a`

` <= -m E_{U}u(a+dU)` by Jensen,

which by (3.6) is at most

`mB E_{U,H}(a+dU+sH)_+^2=mB T_sigma(a)`.                        (3.8)

For `D_H`, the likelihood ratio of `mu_a` with respect to `N(a,d^2)` is proportional to `exp[m u(x)]`, which is nonincreasing. Hence `mu_a` is stochastically dominated by `N(a,d^2)`. The function

`F_s(x)=E_H(x+sH)_+^2`

is nondecreasing. Combining (3.6)--(3.7) with this stochastic domination gives

`D_H/m <= B E_{mu_a}F_s(X)`

` <= B E_{X~N(a,d^2)}F_s(X)`

` = B T_sigma(a)`.                                              (3.9)

This proves (3.1). Formula (3.2) is immediate from monotonicity on each Gaussian cell. For (3.3), use `T_sigma(a)<=a^2+sigma^2` and the standard identities

`int_R^infinity phi=Q(R)`,

`int_R^infinity v phi(v)dv=phi(R)`,

`int_R^infinity v^2 phi(v)dv=Q(R)+R phi(R)`.

Substituting `a(v)=sqrt(p3)v-1` and `sigma^2=1-p3` simplifies the coefficient of `Q(R)` to exactly `2`. QED.

## 4. Demonstrated mechanism gain

The theorem materially strengthens the preceding R14/NM13-07 tail machinery. The earlier generic inner c-sector envelope was

`D_H(v) <= mB E2(v)`,

where `E2` contains an additional score-drift square. The new bound (3.1) replaces it by the same sharp truncated-normal envelope already natural for the outer entropy.

At the archived prescribed-positive-gap waypoint `delta=10^-3`, near the conditional density `alpha≈12.31643335693`, the executed GH160 scout has

`B≈39.262895641136346`, `m≈0.22662158151593148`.

At `v=0`, the new common envelope is

`0.0670335676960`,

versus the older `D_H` envelope

`12.8551518646`,

a factor about `191.77` reduction. At `v=6`, the new envelope is

`121.390927721`,

versus `1354.97965739`,

a factor about `11.16` reduction.

The same numerical scout checks the predicted monotonicity on a 601-point grid in `[-6,6]`; the minimum `D_H` increment is positive, while the minimum `D_U` increment is `-3.7e-16`, consistent with roundoff at a tail value numerically indistinguishable from zero.

More importantly, using only monotone endpoint sums on `[-6,6]` plus the explicit tail bound, the numerical-only enclosure widths fall as follows:

- 256 cells: `D_U` width `0.00354039`, `D_H` width `0.00242724`;
- 1024 cells: `0.000884935`, `0.000606791`;
- 4096 cells: `0.000221326`, `0.000151792`.

These are **NUMERICAL_ONLY** practicality checks, not directed certificates. Their role is to demonstrate that the exact monotone-cell theorem converts the remaining outer c-sector integration into a systematically refinable endpoint problem. Each endpoint itself is only a one-dimensional `U` integral because the inner `H` partition function is analytically closed.

## 5. Residual obstruction and failed routes preserved

The source-level complete-second branch is now saturated to within about `9.25e-12` of what the current anchor objective and exact derivative box can transport. Repeating the same route is no longer a meaningful attack.

The stronger complete-third candidate near `12.28722222161` remains **CONDITIONAL** because a genuine four-overlap zero has not yet been enclosed outward. The new monotone theorem removes the outer-`V` derivative/remainder burden for both c-sector entropies and sharply reduces the inner-entropy tail slack, but it does **not** itself certify the four-dimensional stationary root.

Previously preserved failures remain active:

- changed-radius El Alaoui--Sellke constructions do not imply the exact sphere target;
- direct whole-box product interval arithmetic loses the cancellations in the lifted stationarity system;
- generic weighted second-moment/overlap approaches have the known positive-overlap curvature obstruction;
- sphere nets pay excessive entropy;
- plain Gaussian-polytope facet first moment is too weak;
- finite-lift floating values and replica/full-RSB ansatz values are not promoted without a source-valid directed proof layer.

## 6. Next attack

Do **not** spend another substantive run on complete-second decimals.

Insert Theorem NM07-T03-MONOTONE-CSECTOR into the projective prescribed-gap four-overlap compiler. Use projective coordinates `(w0,w2,x,y)` so the q-sector cone, positive Gaussian denominators, and c-sector algebraic signs are automatic. On each outer `V` cell:

1. outward-enclose the two endpoint conditional entropies by one-dimensional `U` integration;
2. use (3.2) for the compact `V` integral with no derivative remainder;
3. use the common envelope (3.1)--(3.3) for the tails;
4. intersect with NM13-03's variance-deficit / matched-Gaussian / Stein-HSI cages before Krawczyk evaluation.

The first directed target should remain the robust prescribed-gap `delta=10^-3` waypoint near `alpha≈12.31643335693`, because there `Psi_3=10^-3` is algebraic once the four-overlap root is certified. A successful Krawczyk inclusion there would produce a non-microscopic source improvement of about `0.00320`; only afterward should continuation target the stronger capacity-zero branch near `12.28722222161`.

## 7. Essential executed artifacts

Created, executed, and archived in this run:

- `artifacts/t03_monotone_csector_sharp_tangent_alpha123196344462.py`
  - creation commit `5c20b86d55c9a30e2385540e74332d86d82f9bf1`;
- `artifacts/t03_monotone_csector_sharp_tangent_alpha123196344462.out`
  - creation commit `d6557df1e438a3012c1d55ee503420574ca1630c`.

The output ends

`ALL_EXACT_SHARP_TANGENT_CHECKS_PASS`

and

`ALL_NUMERICAL_MONOTONE_CSECTOR_CHECKS_PASS`.

Only the exact rational section is used for the new source endpoint; the GH section is explicitly numerical-only.

## 8. ledger_delta

```yaml
ledger_delta:
  target: T03_negative_spherical_perceptron_kappa_minus_1_exact_radius_sqrtN
  source_metric:
    alpha_L: 6.30297437506
    alpha_U_before: 12.31963446
    alpha_U_after: 12.3196344462
    width_before: 6.01666008494
    width_after: 6.01666007114
    strict_upper_gain: 1.38e-8
    status: review_pending_computer_assisted_rigorous_candidate
  mechanism_gain:
    theorem: NM07-T03-MONOTONE-CSECTOR
    exact_results:
      - D_U(v) monotone_nondecreasing
      - D_H(v) monotone_nondecreasing
      - common_truncated_normal_envelope_mB_Tsigma
      - derivative_free_Gaussian_cell_enclosure
      - explicit_common_right_tail_formula
    demonstrated:
      old_over_new_DH_envelope_ratio_v0: 191.77
      old_over_new_DH_envelope_ratio_v6: 11.16
      monotone_4096_cell_DU_width: 2.21326e-4
      monotone_4096_cell_DH_width: 1.51792e-4
      status: theorem_exact_numerical_practicality_check_only
  conditional_frontier:
    NM13_03_complete_third_alpha: 12.28722222161
    status: CONDITIONAL_NUMERICAL_NOT_OUTWARD_ROOT_CERTIFIED
  residual_obstruction: four_dimensional_outward_Krawczyk_in_projective_overlap_coordinates
  next_attack: outward_endpoint_U_integrals_plus_monotone_V_cells_then_weighted_Krawczyk_at_delta_1e-3
  exact_threshold_status: OPEN_PARTIAL
```

No historical report, peer file, POSTED item, canonical claim, email, Drive object, permission, workflow, scheduler, cadence, or task state was changed.
