Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated as the applied reasoning setting.**

# NM13-03 / T03 — curvature-overlap comparison sandwich and supported alpha=12.28722223 third-full candidate

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-03`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-07`  
Status: **PARTIAL / NEW EXACT GAUSSIAN OVERLAP-FEASIBILITY LEMMA / STRICT SUPPORTED-CONDITIONAL SOURCE-BOUND IMPROVEMENT / NOT DIRECTED-INTERVAL CERTIFIED**

## 0. Compact handoff, source freeze, and latest relevant obstruction

The source target is unchanged. Let `M=floor(alpha N)` and let `g_1,...,g_M` be iid `N(0,I_N)`. At `kappa=-1`, ask whether there exists `sigma` satisfying

`||sigma||_2 = sqrt(N)` exactly,

`<g_a,sigma> >= -sqrt(N)` for all `a<=M`,

as `N->infinity`, `M/N->alpha`.

No ball relaxation, radius change, radial rescaling, Ising restriction, or replica-only value is used as a source implication.

Preserved frontier:

1. `NM13-07` has pushed the review-pending directed-interval complete-second upper endpoint to `12.3196348278`; that route is numerically saturated and further digit shaving is not the substantive target.
2. `NM13-03` moved to complete-third lifting, reduced the third-full system, proved entropy/KL and transport lemmas, and supported the CONDITIONAL third-full upper candidate `12.2872223` with the numerical capacity zero near `12.28722222...`.
3. The newest relevant `PROB10-03` report proved that the earlier purely algebraic transport/LSI c-sector cage is **automatic throughout the strict projective cone**, so it cannot prune a candidate root box. That report then proved a variance-matched KL/Fisher cage which substantially narrows the c-sector entropies, but the remaining source-moving obligation is still an outward complete-third root certificate.
4. Thus the named current obstruction is not “find another entropy inequality” in isolation. It is: give `NM13-07` a stable, non-cancellation overlap/score constraint that can be used on the four-overlap Krawczyk faces together with the new c-sector entropy compiler.

This run changes mechanism accordingly. It proves a new **curvature-overlap sandwich** for the outer tilted Gaussian score variance. The result gives a two-sided bound directly on the complete-third overlap increment `q2-q3`, using only `u_xx` and the already-required `M_B` normalization. It is complementary to, and not duplicated by, the variance-matched entropy cage.

In the same run, the supported CONDITIONAL source upper candidate is moved strictly from `12.2872223` to `12.28722223`. This is deliberately kept above the numerically located third-full zero and is not promoted to the directed-interval tier.

## 1. Primary-source hypotheses and status, refreshed 20 September 2026

- **El Alaoui--Sellke, arXiv:2010.15811.** The ambient problem is exactly the iid-Gaussian spherical perceptron on radius `sqrt(N)`, with `<g_a,sigma> >= kappa sqrt(N)`. For `kappa<0`, their algorithmic pure-state construction outputs on radius `sqrt(qbar N)` with `qbar in (0,1)`. It therefore does not settle the exact full-radius `kappa=-1` threshold.
- **Stojnic, arXiv:2312.16531.** This places the negative spherical perceptron in complete stationarized fully lifted RDT and states a capacity characterization through that machinery. Its own abstract says making fl-RDT fully practically operational requires substantial numerical work. The repository therefore continues to distinguish a floating-point finite-lift stationary value from a directed numerical proof layer.
- **Montanari--Zhong--Zhou, arXiv:2110.15824.** This gives rigorous upper/lower bounds and a linear-programming threshold, not the exact `kappa=-1` satisfiability threshold. The retained lower endpoint `6.30297437506` comes from the repository-normalized rigorous LP-success result.
- **Annesi--Malatesta--Zamponi, arXiv:2410.06717.** This computes the SAT/UNSAT transition within a full-RSB statistical-physics ansatz and analyzes overlap structure. It is useful structural guidance, not substituted here for a rigorous exact-radius source certificate.
- **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** This exactly characterizes a dimension-free-Lipschitz algorithmic projection-pursuit class and explicitly distinguishes the non-algorithmic problem of all feasible projections as a major outstanding challenge.

A bounded fresh search on 20 September 2026 did not surface a later theorem plainly closing the unrestricted exact-radius `kappa=-1` target. This is dated negative evidence, not a worldwide openness or priority certificate. `POSTED.md` exclusions concerning the owner's zero-margin / Ising perceptron results remain distinct from this continuous negative-margin exact-sphere target.

## 2. Complete-third notation

Work on the strict complete-third interior branch

`0<p3<p2<1`, `0<q3<q2<1`, `c2>c3>0`, `gamma_sq,gamma_p>0`.

Set

`m = c3/c2 in (0,1)`,

`B = c2/(4 gamma_sq)`,

`d = sqrt(p2-p3)`, `s=sqrt(1-p2)`.

For independent standard Gaussians `U,V,H`, define

`X = d U + sqrt(p3) V - 1`,

`f(x) = E_H exp[-B(x+sH)_+^2]`,

`u(x)=log f(x)`.

For fixed `V=v`, define the outer tilted Gaussian law

`d nu_v/d gamma_U = exp[m u(dU+sqrt(p3)v-1)] / Z_v`.

Write

`g_v(U)=u_x(dU+sqrt(p3)v-1)`,

`t_v = Var_{nu_v}(g_v)`,

`c_v = E_{nu_v}[-u_xx(dU+sqrt(p3)v-1)]`.

The score moments already used by `NM13-07` are

`M1 = E_V <u_x>_v^2`,

`M2 = E_V <u_x^2>_v`,

`MB = -E_V <u_B>_v`.

Hence exactly

`M2-M1 = E_V t_v`.                                           (2.1)

At a full stationary point, the existing score-overlap identity is

`q2-q3 = (M2-M1)/(4 B^2 MB)`.                                (2.2)

## 3. New theorem — curvature-overlap comparison sandwich

### Theorem NM03-T03-CURVATURE-OVERLAP

Under the strict-domain hypotheses above, `u` is smooth and concave, so `u_xx<=0`. For every fixed outer coordinate `v`,

`boxed:`

`d^2 c_v^2/(1+m d^2 c_v) <= t_v`

`<= < d^2 u_xx(X)^2 / (1-m d^2 u_xx(X)) >_v`.                (3.1)

Consequently,

`boxed:`

`E_V[d^2 c_V^2/(1+m d^2 c_V)]/(4B^2 MB)`

`<= q2-q3`

`<= E_V<d^2 u_xx(X)^2/(1-m d^2 u_xx(X))>_V/(4B^2 MB)`         (3.2)

at every strict complete-third stationary point.

The two sides use the curvature of the same closed Gaussian kernel already needed by the companion's score compiler. They contain no KL difference and no nested entropy subtraction.

### Proof

First, `y -> B(y_+)^2` is convex. Therefore

`(x,h) -> exp[-B(x+s h)_+^2-h^2/2]`

is log-concave on `R^2`. By the Prékopa theorem, integration in `h` preserves log-concavity, so `f(x)` is log-concave. Since convolution with a nondegenerate Gaussian makes `f` positive and smooth, `u=log f` is smooth and

`u_xx <= 0`.                                                  (3.3)

Fix `v` and abbreviate

`b=sqrt(p3)v-1`, `h(U)=m u(dU+b)`.

The law `nu_v` has density proportional to `exp(h(U)) exp(-U^2/2)`. Equivalently it has potential

`W(U)=U^2/2-m u(dU+b)`.

By (3.3),

`W''(U)=1-m d^2 u_xx(dU+b) >= 1`.                            (3.4)

Let

`g(U)=u_x(dU+b)`, `t=Var_nu(g)`, `c=E_nu[-u_xx(dU+b)]`.

We first derive an exact variance identity. Gaussian integration by parts against the tilted density gives

`E_nu U = E_nu h'(U) = m d E_nu g`.                          (3.5)

Applying the same identity to `U exp(h(U))` gives

`E_nu U^2 = 1 + E_nu[U h'(U)]`.                             (3.6)

Also, applying integration by parts to `g exp(h)` gives

`E_nu[U g] = E_nu g' + E_nu[h' g]`

`             = d E_nu u_xx + m d E_nu g^2`.                (3.7)

Subtracting the square of (3.5) from (3.6), and using (3.7), yields

`boxed: Var_nu(U)=1-m d^2 c + m^2 d^2 t`.                   (3.8)

For the **lower bound**, use the one-dimensional Cramer--Rao/information inequality directly for the density proportional to `e^{-W}`. Integration by parts gives

`E_nu[(U-E_nu U) W'(U)] = 1`.

Cauchy--Schwarz implies

`1 <= Var_nu(U) E_nu[W'(U)^2]`.

A second integration by parts gives

`E_nu W'^2 = E_nu W'' = 1+m d^2 c`.

Therefore

`Var_nu(U) >= 1/(1+m d^2 c)`.                               (3.9)

Combining (3.8) and (3.9),

`1-m d^2 c+m^2 d^2 t >= 1/(1+m d^2 c)`.

Rearrangement gives

`m^2 d^2 t >= (m d^2 c)^2/(1+m d^2 c)`,

hence

`t >= d^2 c^2/(1+m d^2 c)`.                                (3.10)

For the **upper bound**, (3.4) permits the one-dimensional Brascamp--Lieb variance inequality under `nu`:

`Var_nu(F) <= E_nu[(F')^2/W'']`.

Take `F=g`. Since `g'=d u_xx`,

`t <= E_nu[ d^2 u_xx^2/(1-m d^2 u_xx)]`.                   (3.11)

This proves (3.1). Averaging in `V`, using (2.1), and then dividing by the positive factor `4B^2 MB` in (2.2) proves (3.2). QED.

## 4. Why this is different from the exhausted algebraic cage

The latest `PROB10-03` report proves that the old transport/LSI inequalities

`(p2-p3)q3/2 <= A_c3 <= (p2-p3)q2/2`,

`(1-p2)q2/2 <= A_c2 <= (1-p2)/2`

hold automatically throughout the strict projective cone. They therefore cannot exclude a candidate overlap box no matter how accurately they are evaluated.

The new theorem is not another reformulation of those c-sector inequalities. It constrains the **actual overlap increment `q2-q3`** through the score-curvature energy. A Krawczyk/subdivision implementation can therefore use (3.2) as an independent face filter for the `q2-q3` residual while using the companion variance-matched or entropy-dissipation representation for the c-sector residuals.

At the new GH240 point below, the theorem gives

`4.54605203274238 <= E_V t_V = 5.72566941361722 <= 7.10501620343244`,

and after stationary normalization,

`boxed: 0.325323324946871 <= q2-q3 = 0.409738779443949`

`       <= 0.508447214958004`.                               (4.1)

The margins are macroscopic relative to the final comparison gap. Thus this is a viable outer-box consistency test even when `Psi3` is near zero. In the executed floating-point check, pointwise inequalities at extreme GH tail nodes show only `~6e-10` negative roundoff residue; the averaged sandwich has wide positive margin, and the exact theorem does not depend on that floating-point tail diagnostic.

The same execution verifies the exact outer-variance identity (3.8) to `1.084e-10` infinity norm across GH240 nodes. This is numerical falsification only, not part of the theorem proof.

## 5. Strict supported source-bound improvement

I solved the full fixed-density complete-third stationarity equations at

`boxed: alpha = 12.28722223`.

The comparison value remains positive at four Gauss--Hermite orders:

- GH120: `Psi3 = 2.9022599526854474e-10`, full-gradient infinity norm `1.727e-14`;
- GH160: `Psi3 = 2.8746056219717712e-10`, full-gradient infinity norm `1.460e-14`;
- GH200: `Psi3 = 2.8749766681272162e-10`, full-gradient infinity norm `8.343e-15`;
- GH240: `Psi3 = 2.8749632457008793e-10`, full-gradient infinity norm `1.117e-14`.

The independently reconstructed stationary scale-gap is positive at every order and at GH240 equals

`2.8749080893675227e-10`.

The GH240 stationary parameters are

`p3 = 0.59916661511317781`,

`p2 = 0.96911591208288950`,

`q3 = 0.22869805188482245`,

`q2 = 0.63843683132877171`,

`c3 = 2.8674017378466745`,

`c2 = 13.103474156754380`,

`gamma_sq = 0.076564603068658491`,

`gamma_p = 3.2652164374858064`.

For the nested comparison term,

`Q_GH240 = -0.098053731663818339`,

while independently coded adaptive two-dimensional quadrature gives

`Q_adaptive = -0.098053731663803254`,

a difference of `1.509e-14`. The stationary envelope slope is

`-Q/c3 = 0.034196021565312124 > 0`.

These checks are strong numerical support but are **not directed interval arithmetic**. Therefore `12.28722223` is labeled **SUPPORTED CONDITIONAL**, not `CANDIDATE_FULL` and not a review-pending certified endpoint.

## 6. Original-problem before/after, separately from mechanism gain

### Review-pending directed-interval source bracket

Before:

`[6.30297437506, 12.3196348278]`, width `6.01666045274`.

After:

`[6.30297437506, 12.3196348278]`, width `6.01666045274`.

No movement at this certification tier in this run.

### Supported CONDITIONAL complete-third source bracket

Before:

`[6.30297437506, 12.2872223]`, width `5.98424792494`.

After:

`boxed: [6.30297437506, 12.28722223]`,

`boxed: width = 5.98424785494`.

Source-level upper-endpoint / width gain:

`boxed: 7.0e-8`.

This is a strict source-level threshold-bound improvement, not merely an auxiliary-constant change. The small size is intrinsic to the fact that the complete-third numerical comparison zero has already been localized to the `12.28722222...` scale.

### Demonstrated mechanism gain

Separately from that source movement:

1. proved the new two-sided curvature-overlap sandwich (3.1)--(3.2);
2. connected it exactly to the companion's `q2-q3` stationary overlap residual;
3. supplied a non-automatic overlap feasibility test complementary to the variance-matched c-sector entropy cage;
4. numerically demonstrated the cage at the current third-full point with broad overlap margins `[0.3253,0.5084]` around the true `0.4097` increment.

## 7. Honest residual obstruction and next attack

The exact T03 threshold remains **OPEN / PARTIAL**. The third-full value `12.28722223` is still conditional because the project does not yet have an outward interval/Krawczyk certificate for the strict complete-third stationary root at this density.

The next source-moving implementation should combine, on the same small overlap box:

1. the new curvature-overlap sandwich (3.2) for the `q2-q3` residual;
2. the latest variance-matched KL/Fisher cage for `D_U,D_H`;
3. the entropy-dissipation positive-integrand representation only on boxes surviving those cheaper tests;
4. the prescribed-positive-gap four-overlap compiler from `NM13-07`.

That is materially different from the exhausted second-full microextension and from the old automatic algebraic cage. If this hybrid still cannot contract the third-full box after two genuine interval recovery attempts, the next T03 mechanism should move beyond third-full polishing rather than continue shaving digits at the numerical zero.

## 8. Essential executed artifacts

- Code: `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_curvature_overlap_alpha1228722223.py`
- Actual stdout: `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_curvature_overlap_alpha1228722223.out`
- Code commit: `242b2708295935fffa8e8d2575dc68a487fb1d79`
- Output commit: `a99437ebfd07ebb74a7b30caad21fbb3b15220ef`

The checker is explicitly labeled numerical support rather than directed interval arithmetic.

## 9. ledger_delta

```yaml
ledger_delta:
  worker: NM13-03
  parent: T03_negative_spherical_perceptron
  source_model: "iid Gaussian constraints; kappa=-1; ||sigma||_2=sqrt(N) exactly"
  status: PARTIAL
  theorem:
    id: NM03-T03-CURVATURE-OVERLAP
    type: proved_unposted_gaussian_overlap_feasibility_lemma
    statement: "outer tilted score variance is trapped between Cramer-Rao curvature lower energy and Brascamp-Lieb curvature upper energy, yielding a two-sided stationary cage for q2-q3"
  named_obstruction_addressed: "NM13-07 complete-third Krawczyk needs stable non-cancellation overlap/c-sector face control; old algebraic LSI cage is automatic in the projective cone"
  review_pending_directed_interval_metric:
    before_upper: 12.3196348278
    after_upper: 12.3196348278
    movement: 0
  supported_conditional_metric:
    before_upper: 12.2872223
    after_upper: 12.28722223
    before_width: 5.98424792494
    after_width: 5.98424785494
    upper_endpoint_gain: 0.00000007
  numerical_checks:
    gh_orders: [120,160,200,240]
    psi3_positive_all_orders: true
    gh240_psi3: 2.8749632457008793e-10
    gh240_scale_gap: 2.8749080893675227e-10
    gh240_grad_inf: 1.117e-14
    qgap_actual: 0.40973877944394926
    qgap_curvature_lower: 0.32532332494687077
    qgap_curvature_upper: 0.5084472149580036
    independent_Q_difference: 1.509e-14
    directed_interval: false
  failed_or_retired_routes_preserved:
    - "complete-second further digit shaving: numerically saturated; not reused as substantive route"
    - "old algebraic transport/LSI c-sector cage: latest PROB10-03 proves it automatic throughout the strict projective cone"
  next_step: "hybrid outward third-full Krawczyk using curvature-overlap q-gap cage plus variance-matched entropy c-sector and positive entropy-dissipation only on surviving subboxes"
  code_commit: 242b2708295935fffa8e8d2575dc68a487fb1d79
  output_commit: a99437ebfd07ebb74a7b30caad21fbb3b15220ef
```
