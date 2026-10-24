Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated as the applied reasoning setting.**

# NM13-03 / T03 — exact variance-deficit entropy cage and supported alpha=12.2872222217 third-full candidate

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-03`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-07`  
Status: **PARTIAL / NEW EXACT GAUSSIAN COMPARISON-FEASIBILITY LEMMA / STRICT SUPPORTED-CONDITIONAL SOURCE-BOUND IMPROVEMENT / NOT DIRECTED-INTERVAL CERTIFIED**

## 0. Compact handoff and exact source freeze

The source problem is unchanged. Let `M=floor(alpha N)`, let `g_1,...,g_M` be iid `N(0,I_N)`, and ask whether there exists `sigma` with

`||sigma||_2 = sqrt(N)` exactly,

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`,

as `N->infinity`, `M/N->alpha`.

No ball relaxation, changed radius, radial normalization, Ising restriction, or replica-only prediction is used as a source implication.

Preserved current frontier:

1. `NM13-07` has now pushed the review-pending directed complete-second endpoint to `alpha_U=12.31963454` by an exact local multi-affine branch-slope certificate. That route is numerically saturated near its own comparison zero and should not be used for further substantive digit shaving.
2. `NM13-03` has a stronger complete-third route. The entering supported CONDITIONAL candidate is `12.28722223`; no outward four-overlap inclusion has yet promoted it to the directed/review-pending tier.
3. The latest `PROB10-03` work proved a sharp generic curvature-deficit KL lower bound using only mean, score variance and a uniform curvature cap. It also proved that this cap-based theorem is sharp for quadratic tilts, so a universal strengthening must exploit perceptron-specific nonconstant curvature.
4. The named `NM13-07` obstruction is therefore the expensive nested `D_U,D_H` control in a four-overlap Krawczyk/subdivision certificate. The previous cap-based feasibility filter is useful but leaves large slack at the third-full point.

This run attacks that precise obstruction. It removes the uniform-curvature cap from the entropy lower bound by recovering the **exact Gaussian variance deficit** from the score and local curvature. The resulting complete-third c-sector cage uses only `u_x,u_xx` under the same outer tilt already required by the score/overlap compiler. It strictly contains the previous cap-based cage and is numerically much tighter at the supported branch.

## 1. Primary-source status, refreshed 20 September 2026

- **El Alaoui--Sellke, arXiv:2010.15811.** The model is exactly the iid-Gaussian spherical perceptron on radius `sqrt(N)`, with constraints `<g_a,sigma> >= kappa sqrt(N)`. For `kappa<0`, their algorithmic pure-state construction outputs on radius `sqrt(qbar N)` with `qbar in (0,1)`, not the exact full-radius threshold demanded here.
- **Stojnic, arXiv:2312.16531.** This places the negative spherical perceptron in stationarized fully lifted RDT and gives the full-lifting capacity characterization, while explicitly noting that substantial numerical work is required to make the machinery practically operational. The repository therefore distinguishes a finite-lift floating-point stationary value from a directed numerical proof layer.
- **Montanari--Zhong--Zhou, arXiv:2110.15824.** This supplies rigorous upper/lower information and the LP threshold, but not the exact `kappa=-1` satisfiability threshold. The retained lower endpoint is `6.30297437506` in the repository normalization.
- **Annesi--Malatesta--Zamponi, arXiv:2410.06717.** This computes the SAT/UNSAT transition under a full-RSB ansatz and is structural guidance, not a directed exact-radius proof certificate.
- **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** This exactly characterizes a dimension-free-Lipschitz algorithmic projection-pursuit class and explicitly separates the unrestricted feasible-projection problem as still outstanding.

A bounded fresh search on 20 September 2026 did not surface a later theorem plainly replacing the exact-radius `kappa=-1` task. This is dated negative evidence, not a worldwide novelty or priority certificate. `POSTED.md` exclusions for the owner's zero-margin/Ising perceptron work remain distinct from this continuous negative-margin exact-sphere target.

## 2. Generic Gaussian variance-deficit information lemma

Let `gamma=N(0,1)` and let

`d nu / d gamma = exp(phi)/Z`,

where `phi` is `C^2`, concave, and integrable enough for the following Gaussian integration by parts. Define

`r = phi'`, `tau = -phi'' >= 0`,

`mu = E_nu X`, `v = Var_nu(X)`, `R = Var_nu(r)`.

Set

`delta = E_nu tau - R`.

### Lemma NM03-T03-VARIANCE-DEFICIT

Under these hypotheses,

`boxed: delta = 1-v in [0,1)`                                             (2.1)

and, with

`psi(t)=-t-log(1-t)` for `0<=t<1`,

`boxed: D_KL(nu||gamma) >= mu^2/2 + psi(delta)/2`.                         (2.2)

Equality in (2.2) holds exactly when `nu` is Gaussian (equivalently, up to null sets, `phi` is quadratic).

### Proof

For smooth test `h`, Gaussian integration by parts against `e^{phi} d gamma` gives

`E_nu[X h(X)] = E_nu[h'(X)+r(X)h(X)]`.                                    (2.3)

With `h=1`,

`mu=E_nu r`.                                                              (2.4)

With `h=X`,

`E X^2 = 1 + E[Xr]`.                                                      (2.5)

With `h=r`,

`E[Xr] = E[r'] + E[r^2] = -E tau + E[r^2]`.                              (2.6)

Subtracting `mu^2=(E r)^2` from (2.5) and using (2.6),

`v = 1-E tau+Var(r)`,

so

`delta=1-v=E tau-R`.                                                       (2.7)

Because `phi` is concave, the potential `x^2/2-phi(x)` has second derivative at least one. Brascamp--Lieb therefore gives `v<=1`; nondegeneracy gives `v>0`. Hence `delta in [0,1)`.

Now among probability laws with fixed mean `mu` and variance `v`, the Gaussian `N(mu,v)` maximizes differential entropy. Equivalently,

`D_KL(nu||gamma) >= D_KL(N(mu,v)||N(0,1))`

` = (mu^2+v-1-log v)/2`

` = mu^2/2 + [-delta-log(1-delta)]/2`,

which is (2.2). Equality in the entropy maximization occurs exactly for a Gaussian law. QED.

This lemma is elementary as a Gaussian information statement; the new point here is its exact complete-third compilation below, which replaces a uniform curvature cap by the actual variance deficit of the tilted perceptron kernel.

## 3. Exact complete-third compilation

Keep the strict complete-third notation from the preceding runs:

`0<p3<p2<1`, `0<q3<q2<1`, `c2>c3>0`,

`m=c3/c2`, `d^2=p2-p3`, `s^2=1-p2`, `B=c2/(4 gamma_sq)`.

For independent standard Gaussians `U,V,H`, set

`X=dU+sqrt(p3)V-1`,

`f(x)=E_H exp[-B(x+sH)_+^2]`, `u=log f`.

For fixed `V=v`, let

`d nu_v/d gamma_U proportional exp[m u(dU+sqrt(p3)v-1)]`,

and define

`g_v=u_x(X)`,

`t_v=Var_{nu_v}(g_v)`,

`c_v=E_{nu_v}[-u_xx(X)]`.

The existing score moments are

`M1=E_V <u_x>_v^2`, `M2=E_V <u_x^2>_v`, `MB=-E_V<u_B>_v`,

and write

`C=4B^2 MB=c2^2/alpha`.

The already proved complete-third stationarity identities are

`q3=M1/C`, `q2=M2/C`,

`A_c3 = alpha D_U/c3^2`, `A_c2=alpha D_H/(c2 c3)`,                  (3.1)

where `D_U` is the outer KL contribution and `D_H` the inner KL contribution.

### Theorem NM03-T03-VARIANCE-DEFICIT-CAGE

At every strict complete-third stationary point, define

`delta_v = m d^2 c_v - m^2 d^2 t_v`.                                  (3.2)

Then `0<=delta_v<1`, and

`boxed: A_c3 >= d^2 q3/2 + E_V psi(delta_V)/(2 m^2 C)`.                (3.3)

For the inner Gaussian tilt

`d rho_x/d gamma_H proportional exp[-B(x+sH)_+^2]`,

one has the exact variance deficit

`boxed: 1-Var_{rho_x}(H) = -s^2 u_xx(x)`.                              (3.4)

Consequently `0<=-s^2u_xx(x)<1` and

`boxed: A_c2 >= s^2 q2/2 + E_{V,nu_V} psi(-s^2 u_xx(X))/(2 C)`.       (3.5)

These inequalities involve only `u_x,u_xx` under the same tilted `U,V` law already required for the overlap score equations. They contain no subtraction of nested KL terms.

### Proof of (3.3)

For fixed `v`, apply Lemma (2.2) to

`phi_v(U)=m u(dU+sqrt(p3)v-1)`.

Its score and negative curvature are

`r_v = m d u_x(X)`,

`tau_v = -m d^2 u_xx(X)`.

Therefore

`mu_v = m d <u_x>_v`,

`Var(r_v)=m^2 d^2 t_v`,

`E tau_v=m d^2 c_v`,

and (2.1) gives exactly (3.2). Hence

`D_KL(nu_v||gamma_U)`

` >= (m^2 d^2/2)<u_x>_v^2 + psi(delta_v)/2`.

Average in `V`:

`D_U >= m^2 d^2 M1/2 + E_V psi(delta_V)/2`.                            (3.6)

Multiply by `alpha/c3^2`. Because `m=c3/c2` and `C=c2^2/alpha`,

`alpha m^2 M1/c3^2 = M1/C=q3`,

and

`alpha/c3^2 = 1/(m^2 C)`.

This gives (3.3).

### Proof of (3.4)--(3.5)

For fixed `x`, the inner tilt has

`phi_x(H)=-B(x+sH)_+^2`.

Its score is

`r_x(H)=-2Bs(x+sH)_+`.

Since `(y_+)^2` is `C^1` with a.e. second derivative `2 1_{y>0}`,

`tau_x(H)=-phi_x''(H)=2Bs^2 1_{x+sH>0}` a.e.                           (3.7)

A smooth approximation justifies applying Lemma (2.1), then taking the limit.

On the other hand, differentiation of `u=log f` gives

`u_x = E_{rho_x}[-2B(x+sH)_+]`,                                        (3.8)

`u_xx = -2B P_{rho_x}(x+sH>0)`

`       + Var_{rho_x}(-2B(x+sH)_+)`.                                   (3.9)

Thus

`E tau_x = 2Bs^2 P_{rho_x}(x+sH>0)`,

`Var(r_x)=s^2 Var(-2B(x+sH)_+)`.

Subtracting with (3.9),

`E tau_x-Var(r_x) = -s^2 u_xx(x)`,

which is (3.4). The inner mean is `E r_x=s u_x(x)`, so Lemma (2.2) gives

`D_KL(rho_x||gamma_H)`

` >= s^2 u_x(x)^2/2 + psi(-s^2 u_xx(x))/2`.                            (3.10)

Multiply by `m`, average under `V,nu_V`, then multiply by `alpha/(c2 c3)`. Using `m=c3/c2`, `C=c2^2/alpha`, and `M2=Cq2`, the first term becomes `s^2q2/2` and the second becomes exactly (3.5). QED.

## 4. Why this strictly improves the previous cap-based obstruction filter

The newest `PROB10-03` generic filter uses a curvature cap `K` and the implication

`delta >= Var(r)/K`.

For the outer tilt, `-u_xx<=L` with

`L=2B/(1+2Bs^2)`,

so that old argument only retains

`delta_v >= m t_v/L`.

Since `psi` is increasing and convex on `[0,1)`, (3.3) implies both

`E psi(delta_V) >= psi(E delta_V)`

and the preceding cap-based correction after replacing `delta_v` by `m t_v/L` and averaging. Thus (3.3) dominates that filter pointwise before Jensen. It is strict unless the tilt has the quadratic/constant-curvature equality structure.

The same logic applies to (3.5): the exact inner deficit `-s^2u_xx` dominates the cap-only score-variance surrogate used previously. This is precisely the perceptron-specific variable-curvature information that the sharpness obstruction in the preceding generic report said was necessary.

At the GH240 third-full point used below, the c-sector lower bounds are:

outer / `c3` sector:

`old cap-based lower = 0.043405598878892816`,

`exact-deficit Jensen lower = 0.048932769929008114`,

`exact-deficit pointwise lower = 0.06111032415767984`,

`actual stationary A_c3 = 0.0672315172352671`;

inner / `c2` sector:

`old cap-based lower = 0.00992370790352111`,

`exact-deficit pointwise lower = 0.011316786751223076`,

`actual stationary A_c2 = 0.011510668080663304`.

Thus the new inner cage captures about 98% of the actual c-sector value at the supported point, while the outer pointwise cage removes most of the previous slack. This is a substantially stronger subdivision rejection test for `NM13-07` before any direct nested KL interval evaluation.

## 5. Strict supported source-bound improvement

In the same run I solved the fixed-density complete-third stationary equations at

`boxed: alpha = 12.2872222217`.

The comparison and independently reconstructed scale-gap remain positive at every tested Gauss--Hermite order:

- GH120: `Psi3=6.3993255139394023e-12`, scale gap `6.3980210018854677e-12`, full-gradient infinity norm `9.878e-15`;
- GH160: `Psi3=3.6342595599592187e-12`, scale gap `3.6362857169791596e-12`, full-gradient infinity norm `2.006e-14`;
- GH200: `Psi3=3.6704528305619988e-12`, scale gap `3.6698977190496862e-12`, full-gradient infinity norm `4.128e-15`;
- GH240: `Psi3=3.6691760740836799e-12`, scale gap `3.6678438064541297e-12`, full-gradient infinity norm `6.665e-15`.

The GH240 stationary parameters are

`p3=0.5991666155385682`,

`p2=0.96911591246064266`,

`q3=0.22869805152433842`,

`q2=0.63843683126844042`,

`c3=2.8674017462395627`,

`c2=13.103474332358253`,

`gamma_sq=0.076564602130952758`,

`gamma_p=3.2652164714236886`.

The numerical variance-deficit identity `delta_V=1-Var_{nu_V}(U)` is satisfied by the GH240 discretization to `1.084e-10` infinity norm over its outer nodes; this is a floating-point tail diagnostic, not part of the exact theorem proof.

These checks are **numerical support only**, not outward interval arithmetic. Therefore the new endpoint remains **SUPPORTED CONDITIONAL**.

## 6. Original-problem before/after, separately from mechanism progress

### Review-pending directed source bracket

Entering from the latest `NM13-07` report:

`[6.30297437506, 12.31963454]`, width `6.01666016494`.

After this run:

`[6.30297437506, 12.31963454]`, width `6.01666016494`.

**No movement at the directed/review-pending tier.**

### Supported CONDITIONAL complete-third source bracket

Before:

`[6.30297437506, 12.28722223]`, width `5.98424785494`.

After:

`boxed: [6.30297437506, 12.2872222217]`,

`boxed: width = 5.98424784664`.

Source-level upper-endpoint / width gain:

`boxed: 8.2999989e-9`.

This is small because the complete-third numerical comparison zero is already localized at the `12.287222221...` scale. The mathematical advance of this run is not the extra digits: it is the exact variable-curvature entropy cage (3.3)--(3.5), which materially reduces the remaining certification slack.

## 7. Essential executed artifacts

Saved create-only under this run namespace:

- code: `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_variance_deficit_alpha122872222217.py`
- actual stdout: `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_variance_deficit_alpha122872222217.out`

Code commit: `57c845aa4056993873ab81bc252a1274e4edb517`.

Output commit: `06af47d538e9ff2e6c861d3524f50820a5791735`.

The output ends `ALL_NUMERICAL_CHECKS_PASS`. These are self-checks, not independent audits.

## 8. Preserved failures and next nonduplicating attack

Preserved failed/exhausted routes:

1. complete-second digit shaving is saturated near its own comparison zero;
2. whole-box objective positivity fails near that zero;
3. the first algebraic transport/LSI c-sector cage is automatic in the strict projective cone;
4. the generic curvature-cap KL theorem is sharp for quadratic tilts and cannot be universally strengthened using only `(mean, score variance, uniform curvature cap)`;
5. floating-point complete-third convergence alone is not a directed source certificate.

The remaining named obstruction is a genuine outward complete-third root inclusion. The best complementary compiler is now:

1. algebraic q-sector and prescribed-positive-gap reconstruction from `NM13-07`;
2. curvature-overlap rejection using the earlier NM13-03 `q2-q3` sandwich;
3. **new exact variance-deficit c-sector rejection (3.3)--(3.5)** using `u_x,u_xx`, avoiding direct nested KL subtraction on most boxes;
4. entropy-dissipation / direct nested interval quadrature only on boxes surviving those cheap filters;
5. a weighted four-overlap Krawczyk or contraction inclusion.

That is the next route capable of moving the directed endpoint toward the complete-third value; another floating-point refinement alone would not be substantive.

## ledger_delta

```yaml
worker: NM13-03
parent: T03
status: PARTIAL
source_model:
  kappa: -1
  disorder: iid_standard_gaussian_rows
  radius: exact_sqrt_N
review_pending_directed_bracket:
  before: [6.30297437506, 12.31963454]
  after:  [6.30297437506, 12.31963454]
  movement: 0
supported_conditional_bracket:
  before: [6.30297437506, 12.28722223]
  after:  [6.30297437506, 12.2872222217]
  upper_endpoint_gain: 8.2999989e-9
  width_after: 5.98424784664
mechanism_gain:
  theorem: NM03-T03-VARIANCE-DEFICIT-CAGE
  outer: A_c3 >= d^2*q3/2 + E psi(delta_V)/(2*m^2*C)
  delta_V: m*d^2*c_V - m^2*d^2*t_V
  inner: A_c2 >= s^2*q2/2 + E psi(-s^2*u_xx)/(2*C)
  application: tighter noncancellation c-sector filter for NM13-07 four-overlap inclusion
certification:
  theorem_proof: complete_on_page
  numerical_endpoint: CONDITIONAL
  directed_interval_third_full: false
artifacts:
  code_commit: 57c845aa4056993873ab81bc252a1274e4edb517
  output_commit: 06af47d538e9ff2e6c861d3524f50820a5791735
next_step: combine variance-deficit c-sector cage with curvature-overlap q-gap cage in outward four-overlap Krawczyk subdivision
```
