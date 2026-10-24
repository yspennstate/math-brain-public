Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-07 / T03 — third-full score-overlap identities and a five-scalar derivative-free capacity compiler

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03`  
Status: **PARTIAL / NEW EXACT THIRD-FULL REDUCTION / SOURCE BRACKET UNCHANGED / 12.288 REMAINS CONDITIONAL**

## 1. Short handoff and exact source target

The exact source model remains frozen:

- `M=floor(alpha N)`;
- `g_a iid N(0,I_N)`;
- `||sigma||_2=sqrt(N)` exactly;
- `<g_a,sigma> >= -sqrt(N)` for every `a<=M`;
- fixed `alpha`, `N->infinity`.

No changed radius, ball relaxation, Ising replacement, replica-only prediction, or algorithmic-only threshold is used as a source implication.

The preceding NM13-07 report certified the review-pending complete-second upper endpoint

`alpha_U = 12.31963485`,

with retained rigorous lower endpoint

`alpha_L = 6.30297437506`.

Its explicit conclusion was that complete-second is numerically saturated and that the next material attack must change mechanism. The newest companion report did so: NM13-03 derived the complete third-full (`r=3`) source objective, eliminated the `q3,q2,gamma_p` sector, and found a high-accuracy **CONDITIONAL** exact-sphere stationary point at

`alpha = 12.288`

with

`Psi3 = 2.65977391709358e-5 > 0`,

while the numerical capacity zero converged near

`12.28722222159`.

NM13-03 correctly did **not** promote `12.288` to a rigorous endpoint because the five-dimensional stationary root and the two-dimensional Gaussian expectation were not outward-enclosed.

This invocation consumes that state and changes the third-full certification problem itself. The new result is an exact Gaussian-semigroup / overlap reduction that removes all numerical differentiation from the `p3,p2,gamma_sq` sector, turns the two overlap variables into normalized score energies, and lowers the third-full capacity system from six scalars to five.

## 2. Primary-source hypotheses and current proof status

A bounded fresh source check on 20 September 2026 remains consistent with the repository state.

1. **El Alaoui--Sellke, arXiv:2010.15811.** Their model is exactly the iid-Gaussian spherical perceptron on radius `sqrt(N)`. For negative `kappa`, their algorithm uses the Parisi/FRSB structure and outputs a feasible vector on radius `sqrt(qbar N)` with `qbar<1`. That is not the exact-radius threshold theorem required here.
2. **Stojnic, arXiv:2312.16531.** This treats the negative spherical perceptron by stationarized fully lifted RDT. Theorem 2 requires the non-fixed lifting parameters to solve the stationarity system; Section 4.2.3 gives the full third-level objective and derivative system; the paper explicitly says practical operation requires substantial numerical work. Its displayed `kappa=-1` third-full value `12.29` is therefore not imported as an already certified endpoint.
3. **Montanari--Zhong--Zhou, arXiv:2110.15824.** Rigorous interpolation bounds and the LP threshold; not the exact `kappa=-1` satisfiability threshold. The retained `6.30297437506` lower endpoint comes from the repository's exact normalization of that LP-success theorem.
4. **Annesi--Malatesta--Zamponi, arXiv:2410.06717.** Full-RSB SAT/UNSAT calculations are useful structural guidance, not a rigorous exact-radius replacement for the comparison certificate here.
5. **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** Exact thresholds are proved for a dimension-free Lipschitz algorithm class; the paper explicitly distinguishes the unrestricted feasible-projection problem as still open.

A bounded search for later 2025--2026 rigorous exact-full-radius `kappa=-1` threshold results did not surface a theorem superseding this status. This is dated negative evidence, not a worldwide novelty certificate. `POSTED.md` continues to separate the owner's zero-margin / Ising perceptron results from this continuous negative-margin exact-sphere target.

## 3. Third-full source objective and notation

Use the companion's source-matched interior third-full branch

`0<p3<p2<1`, `0<q3<q2<1`, `c2>c3>0`, `gamma_sq,gamma_p>0`.

Set

`Aq = 2 gamma_p - c2(1-q2)`,

`Dq = Aq - c3(q2-q3)`,

`B = c2/(4 gamma_sq)`, `m=c3/c2`.

For independent standard Gaussians `U,V,H`, define

`X = sqrt(p2-p3) U + sqrt(p3) V - 1`,

`s=sqrt(1-p2)`,

`f(x)=E_H exp[-B(x+sH)_+^2]`, `u(x)=log f(x)`.

The companion already checked the exact closed kernel

`f(x)=Phi(-x/s) + (1+2Bs^2)^(-1/2)`
`      * exp[-B x^2/(1+2Bs^2)]`
`      * Phi(x/(s sqrt(1+2Bs^2)))`.

Define the nested perceptron term

`Q = E_V log E_U exp[m u(X)]`.

For fixed outer `V=v`, define the tilted inner expectation

`<h>_v = E_U[h(X) exp(m u(X))] / E_U[exp(m u(X))]`.

Finally define four scalar moments

`M1 = E_V <u_x>_V^2`,

`M2 = E_V <u_x^2>_V`,

`MB = - E_V <u_B>_V`,

`QM = E_V <u>_V`.

Here `MB>0` on the interior branch because increasing `B` strictly decreases `f` on a positive-measure set.

The source third-full objective after the exact closed `q`-Gaussian block is

`Psi3 = A + gamma_sq - (alpha/c3) Q`,

where, for later convenience, put the `gamma_sq` term into

`A0 = 1/2(1-p2 q2)c2 + 1/2(p2 q2-p3 q3)c3 - gamma_p`
`     + (1/(2c2)) log(Aq/(2 gamma_p))`
`     + (1/(2c3)) log(Dq/Aq) - q3/(2Dq)`

and write

`A = A0 + c2/(4B)`.

## 4. New theorem: exact Gaussian-semigroup score identities

### Theorem NM07-T03-THIRDFULL-SCORE

On the strict interior domain above,

`Q_p3 = -(m^2/2) M1`,                                      (4.1)

`Q_p2 =  (m(m-1)/2) M2`,                                  (4.2)

`Q_B  = -m MB`,                                             (4.3)

and

`Q_m = QM`.                                                 (4.4)

Consequently, at every genuine interior third-full stationary point,

`q3 = (alpha/c2^2) M1`,                                    (4.5)

`q2 = (alpha/c2^2) M2`,                                    (4.6)

`alpha = c2^2/(4 B^2 MB)`.                                 (4.7)

Eliminating `alpha` gives the particularly simple score-overlap formulas

`boxed: q3 = M1/(4 B^2 MB)`,                               (4.8)

`boxed: q2 = M2/(4 B^2 MB)`.                               (4.9)

Hence

`boxed: q2-q3 = E_V Var_<.>_V(u_x) / (4 B^2 MB) >= 0`.     (4.10)

The inequality is strict on the nondegenerate third-full branch. Thus the hierarchical overlap split has an exact interpretation as **conditional score variance**.

### Proof of (4.1)--(4.4)

Let `P_t` denote the Gaussian heat semigroup of variance `t`:

`P_t h(x)=E h(x+sqrt(t)Z)`.

Because `1-p2>0`, the base Gaussian convolution makes `f` and `u=log f` smooth, strictly positive, and differentiable under the Gaussian integrals used below.

Write

`u_{p2}(x)=log P_{1-p2}[exp(-B(y_+)^2)](x)`.

Then

`Q = P_{p3} [ log P_{p2-p3} exp(m u_{p2}) ](-1)`.

For `p3`, keep `p2` fixed. If

`F=log P_t exp(m u)` with `t=p2-p3`,

then the standard logarithmic heat identity is

`partial_t F = 1/2(F_xx+F_x^2)`.

Increasing `p3` increases the outer heat time and decreases the inner heat time by the same amount. Therefore

`Q_p3 = 1/2 E(F_xx) - 1/2 E(F_xx+F_x^2)`
`      = -1/2 E(F_x^2)`.

But differentiating the tilted log-partition function in `x` gives

`F_x = m <u_x>_V`.

Thus (4.1) follows.

For `p2`, keep `p3` fixed. The inner heat time `t=p2-p3` increases, while the base heat time `1-p2` decreases. The base logarithmic heat equation gives

`partial_p2 u = -1/2(u_xx+u_x^2)`.

Meanwhile

`F_xx+F_x^2 = <m u_xx + m^2 u_x^2>_V`.

Combining the derivative coming from the increasing inner heat time with the derivative of the base potential gives exact cancellation of the `u_xx` terms:

`Q_p2`
` = 1/2 E <m u_xx + m^2 u_x^2>`
`   - m/2 E <u_xx+u_x^2>`
` = m(m-1)/2 E <u_x^2>`
` = m(m-1)M2/2`.

This is (4.2).

At fixed `p2,p3,m`, ordinary differentiation of the tilted partition function gives

`Q_B = m E <u_B> = -m MB`,

which is (4.3). Similarly

`Q_m = E <u> = QM`,

which is (4.4). QED.

### Proof of stationary consequences

The source `p3` and `p2` stationarity equations are, directly from the displayed objective,

`0 = -(1/2) q3 c3 - (alpha/c3) Q_p3`,

`0 = -(1/2) q2(c2-c3) - (alpha/c3) Q_p2`.

Substituting (4.1), `m=c3/c2`, and canceling gives (4.5). Substituting (4.2) and using

`m(1-m)/c3 = (c2-c3)/c2^2`

gives (4.6).

For `gamma_sq`, equivalently differentiate after the change of variable `B=c2/(4 gamma_sq)`. The source equation becomes

`0 = -c2/(4B^2) - (alpha/c3) Q_B`.

Using `Q_B=-m MB=-c3 MB/c2` gives (4.7). Combining (4.5)--(4.7) gives (4.8)--(4.9). Finally

`M2-M1 = E[<u_x^2>-<u_x>^2]`
`      = E Var_<.>_V(u_x)`,

which proves (4.10). QED.

## 5. New theorem: derivative-free five-scalar capacity compiler

The companion and the R14 reduction already show that the source `q3,q2,gamma_p` equations can be solved algebraically. Given `(p2,p3,q2,q3)` in the strict domain, set

`c3 = sqrt(p3/q3)/(p2-p3) - sqrt(q3/p3)/(q2-q3)`,

`gamma_p = 1/2 * (1-q2)/(1-p2) * (p2-p3)/(q2-q3) * sqrt(q3/p3)`,

`c2 = [(p2-p3)/(q2-q3) sqrt(q3/p3)]/(1-p2)`
`     - [(q2-q3)/(p2-p3) sqrt(p3/q3)]/(1-q2)`.

Assume the resulting `c2>c3>0`, and choose `B>0`; then `gamma_sq=c2/(4B)`.

The remaining `c`-derivatives can also be written without numerical differentiation. At fixed source variables define

`A_c3 = 1/2(p2 q2-p3 q3)`
`       - log(Dq/Aq)/(2 c3^2)`
`       - (q2-q3)/(2 c3 Dq)`
`       - q3(q2-q3)/(2 Dq^2)`,                             (5.1)

`A_c2 = 1/2(1-p2 q2)`
`       - log(Aq/(2 gamma_p))/(2 c2^2)`
`       - (1-q2)/(2 c2 Aq)`
`       + (1-q2)/(2 c3)(1/Aq-1/Dq)`
`       - q3(1-q2)/(2 Dq^2)`.                              (5.2)

From (4.3)--(4.4) and `m=c3/c2`, `B=c2/(4 gamma_sq)`,

`Q_c3 = QM/c2`,                                            (5.3)

`Q_c2 = (B Q_B - m QM)/c2`.                               (5.4)

Therefore the two source `c` stationarity equations are exactly

`R_c3 := A_c3 + alpha Q/c3^2 - alpha QM/(c2 c3) = 0`,     (5.5)

`R_c2 := A_c2 - alpha(B Q_B-m QM)/(c2 c3) = 0`.           (5.6)

Now use (4.7) to reconstruct

`alpha = c2^2/(4B^2 MB)`                                  (5.7)

rather than treating `alpha` as an independent capacity unknown. The `p` and `gamma_sq` equations reduce to

`R_3 := q3 - M1/(4B^2 MB) = 0`,                           (5.8)

`R_2 := q2 - M2/(4B^2 MB) = 0`.                           (5.9)

At capacity `Psi3=0`. Since `Q_B=-c3 MB/c2`, substituting (5.7) into the objective gives the derivative-free capacity equation

`R_cap := A + c2 Q/(4B^2 Q_B) = 0`.                       (5.10)

### Equivalence statement

On the strict interior branch, a third-full capacity point is therefore equivalent to a zero of the **five-scalar system**

`(R_3,R_2,R_c3,R_c2,R_cap)=0`                              (5.11)

in only

`(p2,p3,q2,q3,B)`,

with `(c2,c3,gamma_p,gamma_sq,alpha)` reconstructed algebraically from the displayed formulas.

Conversely, any strict-domain zero of (5.11) reconstructs all eight source stationarity equations plus `Psi3=0`: the three `q/gamma_p` equations hold by the existing algebraic reconstruction; (5.8)--(5.9) are exactly the two `p` equations after (4.7); (5.7) is exactly the `gamma_sq` equation; (5.5)--(5.6) are the two `c` equations; and (5.10) is exactly the capacity objective.

This improves the companion's six-scalar capacity compiler by **one full dimension** and, more importantly for a computer-assisted proof, removes numerical differentiation of the two-dimensional Gaussian expectation from every residual evaluation. The only Gaussian objects needed are the scalar moment integrals `Q,M1,M2,MB,QM`.

At fixed target density `alpha0`, replace `R_cap` by

`R_alpha := c2^2/(4B^2 MB)-alpha0=0`.

Then the same five variables give a completely derivative-free fixed-density stationarity system; `Psi3` is evaluated only after the root is certified.

## 6. Decisive executed sanity check on the independent alpha=12.288 point

I implemented the closed kernel and score moments independently of NM13-03's automatic-differentiation solver. The script uses product Gauss--Hermite quadrature only as a **numerical self-check**, not as a rigorous interval certificate.

Artifact:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_thirdfull_score_overlap.py`

creation commit:

`b8da04839ca43336e505783c0fda5f872dfe3f93`.

Executed output:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_thirdfull_score_overlap.out`

creation commit:

`ca0f48a7c23f62095489a996866decfea7f00cbf`.

Using NM13-03's independently obtained `alpha=12.288` point,

`p3=0.599126773053267`,
`p2=0.969080522852930`,
`q3=0.228731793616387`,
`q2=0.638442418504189`,
`c3=2.86661591200020`,
`c2=13.0870435401505`,
`gamma_sq=0.0766524281089569`,
`gamma_p=3.26204123769656`,

the algebraic `q`-sector reconstruction returns

`c2=13.087043540150393`,
`c3=2.8666159120001957`,
`gamma_p=3.262041237696555`,

agreeing at about `1e-13` or better.

At Gauss--Hermite order 160 the independently evaluated moments are

`Q  = -0.098032841467929857`,
`M1 = 3.188074249372902`,
`M2 = 8.89863976499884`,
`MB = 0.0019126284944657442`,
`QM = -0.2422664130166665`,
`Q_B= -0.0004189465144789637`.

The new score reconstruction gives

`q3_pred = 0.22873179361219326`,
`q2_pred = 0.6384424185093357`,
`alpha_pred = 12.288000000000084`.

Thus the deviations from the independent input values are

`q3_pred-q3 = -4.19e-12`,
`q2_pred-q2 =  5.15e-12`,
`alpha_pred-alpha = 8.35e-14`.

Evaluating all five remaining source stationarity residuals with the derivative-free formulas gives maximum absolute residual

`2.63e-11`.

The quadrature convergence is also clean:

- order 60: `alpha_pred=12.288006168421047`;
- order 80: `12.287999746995673`;
- order 100: `12.288000006179276`;
- order 120: `12.288000000561501`;
- order 160: `12.288000000000084`.

As an independent formula check, central finite differences at order 120 agree with the exact semigroup derivatives:

`Q_p3`: theory `-0.07648113982724544`, finite difference `-0.07648114002227942`;

`Q_p2`: theory `-0.7611129480987973`, finite difference `-0.7611130679915923`;

`Q_B`: theory `-0.0004189465144598227`, finite difference `-0.0004189465154421275`.

The archived run ends

`ALL_NUMERICAL_SANITY_CHECKS_PASS`.

Again: these are numerical sanity checks of the exact algebra, **not** outward-rounded proof of the `12.288` stationary root.

## 7. Source threshold before/after versus mechanism gain

### Rigorous / review-pending source bracket

Entering this invocation:

`alpha_L = 6.30297437506`,

`alpha_U = 12.31963485`,

`W = 6.01666047494`.

After this invocation:

`alpha_L = 6.30297437506`,

`alpha_U = 12.31963485`,

`W = 6.01666047494`.

**Source-threshold movement: NONE.**

I do not fabricate a strict endpoint improvement from non-interval Gauss--Hermite convergence. The companion's third-full `12.288` point remains **CONDITIONAL**, so the stronger conditional bracket

`[6.30297437506,12.288]`, width `5.98502562494`,

is not promoted to the rigorous/review-pending bracket in this run.

If the new five-scalar interval system is certified at `12.288`, the upper endpoint would improve by

`12.31963485-12.288 = 0.03163485`,

which is a material rather than microscopic gain.

### Demonstrated mechanism gain

Before this run, third-full validation required a five-dimensional fixed-density root expressed through source partial derivatives, or a six-scalar capacity system, with numerical differentiation/automatic differentiation of a nested two-dimensional Gaussian expectation.

After this run:

1. the two overlap variables have exact score representations (4.8)--(4.9);
2. the overlap split `q2-q3` is exactly a normalized conditional score variance (4.10);
3. `alpha` is reconstructed algebraically from one positive moment `MB`;
4. the `c2,c3` source derivatives are explicit in `Q,QM,Q_B`;
5. fixed-density stationarity is a five-variable **derivative-free moment system**;
6. capacity is a five-variable system rather than the companion's six-variable system.

This directly attacks the named residual obstruction: the next interval validator no longer has to enclose numerical gradients of the nested Gaussian integral merely to evaluate its residual map.

## 8. Residual obstruction and next attack

The exact target is still open. The remaining obligation is now sharply delimited:

1. construct a small five-dimensional box around the `alpha=12.288` point in variables `(p2,p3,q2,q3,B)`;
2. outward-enclose the five scalar Gaussian moments `Q,M1,M2,MB,QM` on that box using the already closed one-dimensional base kernel and a two-stage interval/Taylor quadrature;
3. derive covariance-form analytic first derivatives of those five moments, so the Krawczyk Jacobian is also free of finite differences;
4. certify a zero of `(R_3,R_2,R_c3,R_c2,R_alpha)` by a weighted Krawczyk or contraction argument;
5. use an a-posteriori localization of `Psi3`, rather than demanding whole-box objective positivity, to retain the companion's `2.66e-5` positive margin.

The conditioning reported by NM13-03 (`sigma_min about 2.555e-4`, condition number about `1.65e5`) means naive whole-box interval arithmetic will likely wrap. The score formulas identify the correct fix: precondition the **new five-scalar moment residual**, not the original eight-variable derivative system.

No historical or peer file was overwritten. No shared root ledger, scheduler, permission, workflow, email, Drive item, or public post was changed.

## 9. ledger_delta

```yaml
ledger_delta:
  worker: NM13-07
  parent: T03
  source_model: "iid Gaussian constraints; kappa=-1; ||sigma||=sqrt(N) exactly"
  source_status: PARTIAL
  source_metric:
    name: rigorous_threshold_bracket
    before: "[6.30297437506, 12.31963485]"
    after: "[6.30297437506, 12.31963485]"
    width_before: 6.01666047494
    width_after: 6.01666047494
    movement: none
  conditional_candidate:
    upper: 12.288
    width_if_certified: 5.98502562494
    status: CONDITIONAL_NOT_INTERVAL_CERTIFIED
  mechanism_gain:
    - "Exact heat-semigroup identities Q_p3=-(m^2/2)M1, Q_p2=(m(m-1)/2)M2, Q_B=-m MB."
    - "Exact score-overlap identities q3=M1/(4B^2 MB), q2=M2/(4B^2 MB)."
    - "Exact overlap split q2-q3 = E Var_tilt(u_x)/(4B^2 MB)."
    - "Third-full capacity compiler reduced from six scalars to five."
    - "Fixed-density residual evaluation no longer needs numerical differentiation of nested Gaussian Q."
  consumed_companion:
    path: "proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-thirdfull-feasibility-alpha12288.md"
    candidate_alpha: 12.288
    candidate_status: CONDITIONAL
  artifact_source:
    path: "proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_thirdfull_score_overlap.py"
    commit: "b8da04839ca43336e505783c0fda5f872dfe3f93"
  artifact_output:
    path: "proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_thirdfull_score_overlap.out"
    commit: "ca0f48a7c23f62095489a996866decfea7f00cbf"
    terminator: ALL_NUMERICAL_SANITY_CHECKS_PASS
  residual_obstruction: "Outward-rounded five-dimensional root/Jacobian enclosure for the third-full moment residual at alpha=12.288."
  next_attack: "Derive covariance-form Jacobian identities for Q,M1,M2,MB,QM and interval-Krawczyk the new five-scalar residual; then certify Psi3>0 a posteriori."
```
