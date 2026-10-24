Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated as the applied reasoning setting.**

# NM13-07 / T03 — matched-Gaussian entropy cage, recentered contraction, and exact-sphere upper endpoint 12.31963446

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03`  
Status: **PARTIAL / STRICT COMPUTER-ASSISTED SOURCE-BRACKET IMPROVEMENT / NEW THIRD-FULL VARIATIONAL CAGE / PENDING LATER INDEPENDENT REVIEW**

## 0. Short handoff and frozen source problem

The source problem is unchanged. Let `M=floor(alpha N)`, let `g_1,...,g_M` be iid `N(0,I_N)`, and ask whether there exists `sigma` with

`||sigma||_2 = sqrt(N)` exactly,

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`,

as `N->infinity` with `M/N->alpha`.

No radius change, ball relaxation, radial rescaling, Ising replacement, or replica-only threshold is used as a source implication.

The entering repository-supported review-pending bracket is

`alpha_L = 6.30297437506`,

`alpha_U = 12.31963454`,

width `6.01666016494`.

The previous NM13-07 run proved a local multi-affine tangent estimate `0<dPsi/dalpha<1/25` on the complete-second directed rectangle and nearly exhausted its original center-based contraction geometry. It explicitly said that another unchanged center microextension should not count as substantive progress. The latest companion NM13-03 run instead strengthened the complete-third route: its variance-deficit theorem gives a sharp **lower** entropy cage and supports a third-full stationary candidate at `alpha=12.2872222217`, but no outward four-overlap inclusion yet exists.

This run therefore does two things, with the effort concentrated on the new third-full mechanism.

1. It proves a complementary **matched-Gaussian entropy upper cage**. Together with NM13-03's exact variance-deficit lower cage, both difficult complete-third c-sector entropies are sandwiched by score/curvature moments already present in the overlap compiler, without evaluating a subtractive nested log-partition/KL expression.
2. It then closes one small source-level gap rigorously by a genuinely new **predictor/recentered contraction chart** inside the already directed complete-second rectangle. The new chart has a fresh midpoint inverse and fresh exact vertex contraction constant; it is not the exhausted old center estimate. This gives the strict source upper endpoint `12.31963446`.

## 1. Primary-source hypotheses and current proof status, refreshed 20 September 2026

1. **El Alaoui--Sellke, arXiv:2010.15811.** The ambient model is exactly the iid-Gaussian spherical perceptron on the radius-`sqrt(N)` sphere with constraints `<g_a,sigma> >= kappa sqrt(N)`. For `kappa<0`, the algorithm described in the abstract outputs a feasible vector on radius `sqrt(qbar N)` with `qbar in (0,1)`, given oracle access to the Parisi solution. The authors expect `qbar->1` near capacity, but that expectation is not an exact-radius threshold theorem. Therefore this result does not close T03.
2. **Stojnic, arXiv:2312.16531.** This fits the negative spherical perceptron into fully lifted random duality theory. Theorem 2 requires the non-fixed lifting parameters to solve the full stationarity system in `p,q,c,gamma_sq,gamma_p` before the complete-sfl identity is invoked. The abstract also says substantial numerical work is needed to make the characterization operational. The present project therefore keeps a source-matched stationary identity separate from a floating finite-lift table and supplies directed numerical proof layers when claiming endpoints.
3. **Montanari--Zhong--Zhou, arXiv:2110.15824.** This rigorously proves upper and lower bounds on the negative-perceptron interpolation threshold and characterizes the LP threshold. It does not identify the exact `kappa=-1` threshold. The retained lower endpoint `6.30297437506` is the repository-normalized rigorous LP-success-side value.
4. **Annesi--Malatesta--Zamponi, arXiv:2410.06717.** Their transition is computed under a full-RSB ansatz. It is useful structural guidance but is not substituted for a rigorous exact-radius certificate.
5. **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** This gives exact thresholds for a dimension-free Lipschitz algorithmic projection-pursuit class. Its abstract explicitly says that the non-algorithmic problem of characterizing all feasible projections remains a major outstanding challenge.

A bounded fresh search on 20 September 2026 did not surface a later theorem plainly closing the unrestricted exact-radius `kappa=-1` target. This is dated negative evidence, not a novelty or priority certificate. The repository's POSTED zero-margin/Ising perceptron results remain distinct from this continuous negative-margin exact-sphere target.

## 2. New generic theorem — matched-Gaussian entropy/Fisher cage

Let `gamma=N(0,1)`, and let

`d nu / d gamma = exp(phi)/Z`

with sufficient smoothness and integrability for the integrations by parts below. Write

`mu = E_nu X`, `v = Var_nu(X)>0`,

`r=phi'`, `R=Var_nu(r)`, `delta=1-v`.

In the complete-third applications `phi` is concave, so `0<v<=1` and `0<=delta<1` by Brascamp--Lieb. Define

`psi(delta) = -delta-log(1-delta)`.

### Theorem NM07-T03-MATCHED-GAUSSIAN-CAGE

Let `G=N(mu,v)` be the Gaussian having the same mean and variance as `nu`. Then

`D(nu||gamma) = [mu^2+psi(delta)]/2 + D(nu||G)`,                 (2.1)

and

`0 <= D(nu||G) <= (1/2) log(1+v R-delta^2)`.                   (2.2)

Consequently

`boxed:`

`[mu^2+psi(delta)]/2`

` <= D(nu||gamma)`

` <= [mu^2+psi(delta)+log(1+(1-delta)R-delta^2)]/2`.           (2.3)

Moreover

`vR-delta^2 = v I(nu||G) >= 0`,                               (2.4)

where `I(nu||G)` is the relative Fisher information. Equality in the correction occurs when `nu` itself is Gaussian.

### Proof

Because `G` matches the first two moments of `nu`, `log(dG/dgamma)` is a quadratic whose expectation is the same under `nu` and `G`. Therefore

`D(nu||gamma)=D(nu||G)+D(G||gamma)`.

The Gaussian term is

`D(G||gamma)=(mu^2+v-1-log v)/2`

`              =[mu^2-delta-log(1-delta)]/2`,

which proves (2.1).

For the Fisher term, Gaussian integration by parts under the tilt gives

`E_nu r = mu`,

and, using `E[X h(X)]=E[h'(X)+r(X)h(X)]` with `h=X`,

`Cov_nu(X,r)=v-1=-delta`.                                     (2.5)

The score of `nu` relative to the matching Gaussian is

`d/dx log(dnu/dG)`

` = (r-mu)+(1/v-1)(X-mu)`.

Squaring and using (2.5), with `1/v-1=delta/v`, gives

`I(nu||G)=R-delta^2/v`,

hence (2.4).

It remains to prove the entropy/Fisher upper bound. For completeness, it follows from the one-dimensional Gaussian log-Sobolev inequality by optimizing over dilations. Let a centered law `X` have variance `v` and ordinary Fisher information `J`. Applying standard Gaussian LSI to `aX` gives

`D(aX||gamma) <= I(aX||gamma)/2`.

Expanding both sides cancels the common `a^2 v/2` term and yields

`h(X) >= (1/2)log(2 pi) + log a + 1 - J/(2a^2)`.

Optimizing at `a^2=J` gives Stam's entropy--Fisher inequality

`h(X) >= (1/2)log(2 pi e/J)`.

After translation this implies

`D(nu||G) <= (1/2)log(vJ)`.

The ordinary and relative Fisher informations satisfy `vJ=1+v I(nu||G)`, so by (2.4)

`D(nu||G) <= (1/2)log(1+vR-delta^2)`.

This proves (2.2)--(2.3). QED.

### Structural meaning

NM13-03's variance-deficit theorem identified the first term in (2.1) as a robust lower cage. The new theorem identifies exactly what is missing: the non-Gaussian entropy defect `D(nu||G)`, and upper-bounds it by a single nonnegative score-curvature statistic `vR-delta^2`. No partition function appears in the correction. This is adapted to interval arithmetic because all ingredients are local expectations under the same tilted laws already used in the overlap equations.

## 3. Complete-third compilation

Use the strict complete-third notation already source-matched in NM13-03/NM13-07:

`0<p3<p2<1`, `0<q3<q2<1`, `c2>c3>0`,

`m=c3/c2`, `d^2=p2-p3`, `s^2=1-p2`, `B=c2/(4 gamma_sq)`.

For independent standard Gaussians `U,V,H`, put

`X=dU+sqrt(p3)V-1`,

`f(x)=E_H exp[-B(x+sH)_+^2]`, `u(x)=log f(x)`.

For fixed `V=v`, let `nu_v` be the tilted `U`-law proportional to `exp[m u(X)]`, and write

`g_v=<u_x>_v`,

`t_v=Var_v(u_x)`,

`c_v=< -u_xx >_v`,

`delta_v=m d^2 c_v-m^2 d^2 t_v`.

The outer c-sector entropy is

`D_U=E_V KL(nu_V||gamma_U)`.

Applying Theorem (2.3) pointwise in `V` gives the two-sided, cancellation-free cage

`L_U <= D_U <= U_U`,                                             (3.1)

where

`L_U = (1/2) E_V[(m d g_V)^2 + psi(delta_V)]`,

`U_U = L_U`

`      +(1/2)E_V log(1+(1-delta_V)m^2 d^2 t_V-delta_V^2)`.       (3.2)

The correction inside the logarithm is automatically nonnegative by (2.4).

For the inner tilted `H`-law

`d rho_x/d gamma_H proportional exp[-B(x+sH)_+^2]`,

NM13-03 already proved the exact variance deficit

`delta_H(x) = 1-Var_rho(H) = -s^2 u_xx(x)`.                     (3.3)

Its tilt score is

`r_H=-2Bs(x+sH)_+`,

so

`R_H(x)=Var_rho(r_H)`

`      =2Bs^2 P_rho(x+sH>0)-delta_H(x)`.                        (3.4)

The first equality follows from the definition, while the second is the exact deficit identity `delta=E tau-Var(r)` with `tau=2Bs^2 1_{x+sH>0}`. Therefore

`L_H(x) <= KL(rho_x||gamma_H) <= U_H(x)`,                       (3.5)

with

`L_H(x)=[s^2u_x(x)^2+psi(delta_H(x))]/2`,

`U_H(x)=L_H(x)`

` +(1/2)log(1+(1-delta_H(x))R_H(x)-delta_H(x)^2)`.              (3.6)

After multiplying by `m` and averaging under the outer tilted law, (3.5) gives the complete inner c-sector entropy cage. Finally, the source c-stationarity normalization is unchanged:

`A_c3 = alpha D_U/c3^2`,

`A_c2 = alpha D_H/(c2 c3)`.

Thus both c-sector residuals now have **lower and upper** enclosures using only `u_x,u_xx`, a positive-tail probability, and score variances. Direct nested KL/log-partition evaluation can be reserved for a final tiny subbox, or potentially avoided altogether.

This directly complements NM13-03's comparison theory rather than duplicating it: that worker supplied the exact variance-deficit lower term; the present theorem supplies the matched-Gaussian Fisher upper correction.

## 4. Numerical-only falsification at the strongest companion third-full point

I executed an independent GH200 implementation at the companion's supported, still CONDITIONAL density

`alpha=12.2872222217`.

The full five-equation stationary solve gives

`p3 = 0.59916661553777206`,

`p2 = 0.96911591246056061`,

`q3 = 0.22869805152395933`,

`q2 = 0.63843683126824713`,

`c3 = 2.867401746232769`,

`c2 = 13.103474332343133`,

`gamma_sq = 0.076564602131018136`,

`gamma_p = 3.2652164714210445`,

with full-gradient infinity norm about `2.35e-14`.

The new outer entropy cage evaluates to

`D_U lower = 0.04089196358580124`,

`D_U actual = 0.04498795894957890`,

`D_U matched-Gaussian upper = 0.05515653284106402`.

The inner cage is much tighter:

`D_H lower = 0.03460544411393312`,

`D_H actual = 0.03519831112275527`,

`D_H matched-Gaussian upper = 0.03665835191555745`.

After source c-sector scaling,

`A_c3: 0.06111032415779018 <= 0.06723151723535059 <= 0.08242777567442602`,

`A_c2: 0.011316786751250453 <= 0.01151066808069106 <= 0.011988135448133869`.

For comparison, NM13-03's earlier generic transport-LSI upper cages at the nearby branch point were about `0.1180946` for `A_c3` and `0.0154420` for `A_c2`. The new matched-Gaussian correction therefore removes a substantial part of the remaining c-sector interval slack, especially in the inner sector.

These values are **NUMERICAL_ONLY** sanity checks. They do not promote `12.2872222217`; the source endpoint still needs an outward four-overlap root inclusion.

The executed numerical checker ends

`ALL_NUMERICAL_MATCHED_GAUSSIAN_CAGE_CHECKS_PASS`.

## 5. New exact predictor/recentered complete-second contraction chart

The complete-second route is numerically saturated, but the preceding source endpoint stopped because the old contraction was centered at the original `alpha0=12.319635` scout and had localization factor near one. A new center can exploit the same already certified derivative rectangle without recomputing any Gaussian intervals.

### Consumed directed rectangle

At the original center `(p_c,B_c)` the directed certificate supplies radii

`r_p^old=1e-7`, `r_B^old=4e-6`,

and the rational-widened derivative box

`H_p in [-3371/100000,-2828/100000]`,

`H_B in [3284/10^7,5044/10^7]`,

`alpha_p in [24671/1000,25288/1000]`,

`alpha_B in [-60244/100000,-6008/10000]`.

The center residual ceilings are

`|H_c|<4.7e-12`,

`|alpha_c-alpha0|<3.7e-11`.

The same rectangle also carries the objective-derivative intervals used for the exact tangent bound `0<dPsi/dalpha<1/25`.

### Predictor center

Take the midpoint density shift

`delta_m=5e-7`.

Let `J_m` be the midpoint of the `(H,alpha)` derivative box and let `A_m=J_m^{-1}`. Use the linear predictor

`(Delta p,Delta B) = -A_m (0,delta_m)`.

Exact rational arithmetic gives

`Delta p = 347/13742913500`

`        = 2.524937670603835e-8`,

`Delta B = 6199/3298299240`

`        = 1.879453484638950e-6`.

Around this shifted center choose

`r_B = 2.1e-6`,

`r_p = r_B/(85/2) = 4.941176470588236e-8`.

The whole new box lies strictly inside the old directed rectangle because

`|Delta p|+r_p = 7.46611414119207e-8 < 1e-7`,

`|Delta B|+r_B = 3.97945348463895e-6 < 4e-6`.                  (5.1)

Therefore every inherited directed derivative enclosure is valid on the new box.

### Fresh contraction constant

Using `A_m`, I enumerated all sixteen vertices of the independent interval Jacobian for `(H,alpha)`. In the weighted norm with ratio `r_B/r_p=85/2`, the exact result is

`q_new = 229179741/467259059`

`      = 0.4904768277590526`.                                  (5.2)

This is a newly computed contraction constant, not the previous chart's inherited `q`.

### Shifted-center residual without new quadrature

The segment from the old center to the predictor center lies inside the old rectangle. The fundamental theorem of calculus plus the directed derivative box therefore gives

`|H(new center)|`

` <= 196779801607/824574810000000000000`

` = 2.3864396440512174e-10`,                                  (5.3)

and, relative to the midpoint target `alpha0-5e-7`,

`|alpha(new center)-(alpha0-5e-7)|`

` <= 772427426797/82457481000000000000`

` = 9.36758457121677e-9`.                                     (5.4)

Now vary the target uniformly over

`I=[12.31963446,12.31963454]`.

Its distance from the midpoint target is at most `4e-8`, so the second residual is uniformly at most

`4.936758457121677e-8`.                                       (5.5)

Applying the exact rational preconditioner to (5.3)--(5.5) yields normalized center displacement

`eta = 17649093670330819/40795417037192166`

`    = 0.4326244208814088`.

Since

`1-q_new = 0.5095231722409473`,

we have `eta<1-q_new`. The a-posteriori localization factor is

`rho = eta/(1-q_new)`

`    = 300034592395623923/353365575128603244`

`    = 0.8490770281922054 < 1`.                               (5.6)

Hence for every target density in `I` the preconditioned map is a self-map contraction and has a unique stationary zero in the new box.

### Connecting to the previously certified branch

A separate uniqueness argument is needed so that the new chart's root at the overlap density `12.31963454` is the same root transported from the certified `alpha0` anchor.

On the entire old rectangle the directed intervals give

`H_p<0`, `H_B>0`,

and the exact 16-vertex determinant bound

`Delta=H_p alpha_B-H_B alpha_p`

`>=1323549/312500000 = 0.0042353568>0`.                        (5.7)

For each fixed `p`, `H` is strictly increasing in `B`, so there is at most one `B` with `H=0`. If two zeroes have `p_1<p_2`, then monotonicity forces `B_1<B_2`, and the intermediate-value theorem fills a unique zero graph between them. Along that graph,

`d alpha/dp = -Delta/H_B <0`.                                  (5.8)

Thus two points of `H=0` in the old rectangle cannot have the same `alpha`. The stationary zero for a fixed target is globally unique inside the old rectangle. Consequently the new-chart zero and the preceding certified branch coincide at `alpha=12.31963454`, giving one connected `C^1` branch all the way from `alpha0` to the new target.

### Objective transport and new endpoint

The exact 64-vertex multi-affine calculation from the predecessor is rechecked by the new exact checker:

`0 < dPsi/dalpha < 1/25`                                      (5.9)

throughout the old rectangle. The true stationary root at `alpha0` has the already directed lower bound

`Psi(alpha0) >= 23584189005311/1090044380000000000000`

`            = 2.163598972485047e-8`.

The new endpoint is

`alpha1 = 12.31963446 = alpha0-5.4e-7`.

By (5.9),

`Psi(alpha1)`

` >= Psi(alpha0)-(5.4e-7)/25`

` >= 39230397311/1090044380000000000000`

` = 3.598972485046893e-11 > 0`.                               (5.10)

Consuming the same source-matched stationarized complete-sfl comparison implication as the previous directed certificates, (5.10) gives asymptotic UNSAT at `alpha1` for the exact radius-`sqrt(N)` model. Constraint monotonicity therefore yields

`boxed: alpha_c(-1) <= 12.31963446`.                           (5.11)

The exact checker ends

`ALL_EXACT_PREDICTOR_RECENTER_CHECKS_PASS`.

## 6. Source threshold before/after, separately from mechanism gains

### Source-level review-pending computer-assisted bracket

Before:

`[6.30297437506, 12.31963454]`,

width `6.01666016494`.

After:

`boxed: [6.30297437506, 12.31963446]`,

width

`boxed: 6.01666008494`.

Strict upper-endpoint and bracket-width gain:

`boxed: 8e-8`.

This remains **PARTIAL** and pending later independent review. It is an improved upper bound, not a determination of the exact threshold.

### Demonstrated mechanism gains

1. **Third-full:** the new matched-Gaussian theorem turns NM13-03's one-sided variance-deficit lower cage into a two-sided entropy cage. Its upper correction depends only on `vR-delta^2=v I(nu||G)`, so both nested c-sector entropies can be enclosed by the same score/curvature moment engine used for overlaps. At the supported third-full point the inner scaled c-sector interval shrinks numerically from roughly `[0.0113168,0.0154420]` under the previous generic upper cage to `[0.0113168,0.0119882]` before any direct KL evaluation.
2. **Complete-second:** the predictor/recenter construction proves that an exhausted center-based contraction does not imply the whole directed rectangle is exhausted. A fresh local chart with `q_new≈0.49048` certifies another source interval and gives the strict endpoint (5.11). This is useful as an a-posteriori continuation device, but the complete-second comparison zero is still only about `1e-7` farther down, so it is not the main future route.

## 7. Essential executed artifacts

Exact rational predictor/recenter checker:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_predictor_recenter_alpha1231963446.py`

creation commit: `329ee5cd2ef40b0965cba235a92d1228428cf230`.

Actual archived stdout:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_predictor_recenter_alpha1231963446.out`

creation commit: `2c0f74453ed2350248e86a9d6d7603f6f1f17aeb`.

Numerical-only matched-Gaussian falsification checker:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_matched_gaussian_entropy_cage.py`

creation commit: `aa5a95a6f970c251742464ff06209ec1afd357a2`.

Actual archived stdout:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_matched_gaussian_entropy_cage.out`

creation commit: `63b00c7bf7689c9b029ea6e00578037be31698b9`.

The exact source-level certificate uses only rational arithmetic after consuming the previously archived directed intervals. The third-full checker is explicitly numerical support, not an interval certificate.

## 8. Residual obstruction, preserved failures, and next attack

### Residual obstruction

The materially stronger third-full candidate remains **CONDITIONAL**. No outward four-overlap Krawczyk/root inclusion has yet been completed. The new upper cage greatly reduces the c-sector uncertainty but does not by itself prove that the four residuals have a common zero.

### Preserved failures / limitations

1. Floating-point Gauss--Hermite convergence, even with `1e-14` residuals, is not promoted to a source endpoint.
2. The prior generic LSI upper cage is rigorous but too loose for a small four-dimensional inclusion; the matched-Gaussian correction is designed to replace it.
3. Direct interval evaluation of nested log partitions suffers dependency/wrapping. The present theorem reduces the necessary interval primitives to score/curvature moments, but those moments still need outward enclosures on a parameter box.
4. The complete-second route is nearly at its own comparison zero. The present recentering is a strict source advance, but another run devoted only to shaving complete-second decimals should not count as substantial progress.
5. Changed radius, ball relaxation, pure-state rescaling, replica/full-RSB numerics, and algorithmic thresholds remain non-closures for T03.

### Next attack

Use the projective complete-third coordinates `(w0,w2,x,y)` and the prescribed-positive-gap compiler, initially at the robust `delta=10^-3` waypoint near `alpha≈12.31643335693` rather than the tiny-gap capacity point. On a small projective box:

1. reconstruct `c2,c3,gamma_p,gamma_sq,B` algebraically, so all q-sector/log-domain inequalities are structural;
2. outward-enclose only `u_x,u_xx`, the positive-tail probability, and the score moments needed by the overlap equations;
3. apply NM13-03's variance-deficit lower cage together with the new matched-Gaussian upper cage as two-sided c-sector residual filters;
4. use the curvature-overlap sandwich as an independent q-gap filter;
5. run a weighted four-dimensional Krawczyk inclusion only on surviving subboxes.

At prescribed positive gap, a successful stationary inclusion already has `Psi_3=delta>0` algebraically, so no separate nested objective enclosure is needed. Certifying the `delta=10^-3` waypoint would move the source upper endpoint non-microscopically by about `0.0032`; after one certified third-full anchor, stationary branch continuation can target the much stronger `12.287222...` regime.

## 9. ledger_delta

```yaml
ledger_delta:
  parent: T03
  owner: NM13-07
  date: 2026-09-20
  source_model:
    kappa: -1
    constraints: iid Gaussian
    radius: sqrt(N) exactly
  status: PARTIAL
  source_threshold_before:
    lower: 6.30297437506
    upper: 12.31963454
    width: 6.01666016494
  source_threshold_after:
    lower: 6.30297437506
    upper: 12.31963446
    width: 6.01666008494
  strict_source_gain: 8.0e-8
  source_gain_mechanism: predictor/recentered directed contraction plus stationary objective transport
  new_theorem:
    name: NM07-T03-MATCHED-GAUSSIAN-CAGE
    statement: two-sided KL cage around the moment-matched Gaussian using variance deficit and relative Fisher correction
    applied_to: complete-third outer and inner c-sector entropy residuals
  strongest_thirdfull_candidate:
    alpha: 12.2872222217
    status: CONDITIONAL_NUMERICAL_ONLY
  residual_obstruction: outward four-overlap Krawczyk inclusion for complete-third stationarity
  next_attack: projective positive-gap four-dimensional interval inclusion using two-sided entropy cage
  exact_artifact: t03_predictor_recenter_alpha1231963446.py
  numerical_artifact: t03_matched_gaussian_entropy_cage.py
  independent_review: pending
```

No historical file, peer file, shared root ledger, POSTED result, schedule, permission, workflow, email, Drive object, paid resource, or public resource was modified.
