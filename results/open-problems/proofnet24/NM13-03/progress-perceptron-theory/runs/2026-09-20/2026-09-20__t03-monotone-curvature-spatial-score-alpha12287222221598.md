Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-03 / T03 — monotone-curvature hinge semigroup, spatial score compiler, and supported alpha=12.287222221598

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-03`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-07`  
Status: **PARTIAL / NEW EXACT GAUSSIAN COMPARISON-FEASIBILITY LEMMAS / STRICT SUPPORTED-CONDITIONAL SOURCE-BOUND IMPROVEMENT / THIRD-FULL DIRECTED CERTIFICATE STILL OPEN**

## 0. Compact handoff and source freeze

The source problem remains exactly

- `M=floor(alpha N)`;
- `g_1,...,g_M iid N(0,I_N)`;
- exact sphere `||sigma||_2=sqrt(N)`;
- constraints `<g_a,sigma> >= -sqrt(N)` for all `a<=M` (`kappa=-1`);
- fixed `alpha`, `N->infinity`.

No ball relaxation, changed radius, radial renormalization, Ising restriction, algorithmic-class threshold, or replica/full-RSB-only value is used as a source implication.

The latest companion report on `master`,

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-double-semiconcavity-scalarQ-alpha123196344461907498.md`,

proves a scalar-`Q` compiler for the complete-third positive-gap branch. In its current form the four non-algebraic moments are recovered as auxiliary directional derivatives of the nested scalar free energy `Q`; in particular

`S1 = -2 Q_rho/m^2`

uses an auxiliary variance-transfer direction `rho`. The same report identifies the remaining obstruction as an **outward scalar-`Q` tube/cascade certificate** at `delta=10^-3`, with the final KL-free Schur row still depending on `S1` and `Q`.

This run removes the `rho` direction from the `S1` compiler. It proves that the actual conditional scalar partition already has a stronger one-dimensional shape: its curvature is monotone, not merely bounded. Consequently `S1` admits a two-sided spatial-secant enclosure using only the same conditional `q` values already needed by the outer `Q` cells. A second local curvature-energy inequality materially tightens the one-sided score cage.

A repository search found the preceding global bound `|q'''|<=sqrt(5)/d^3`, but no project proof of the sign `q'''<=0`, no invariant monotone-curvature cone for this hinge semigroup, and no spatial-secants-only `S1` compiler. The results below are therefore **unposted in this repository**. Publication novelty is not claimed.

## 1. Primary-source status, refreshed 20 September 2026

1. **El Alaoui--Sellke, arXiv:2010.15811.** The ambient model is exactly the iid-Gaussian spherical perceptron on radius `sqrt(N)`, with `<g_a,sigma> >= kappa sqrt(N)`. For `kappa<0`, however, their algorithm outputs a feasible vector on radius `sqrt(qbar N)` with `qbar in (0,1)` and only expects `qbar->1` near capacity. This does not establish the exact full-radius threshold required here.
2. **Stojnic, arXiv:2312.16531.** The paper fits the negative spherical perceptron into stationarized fully lifted RDT and states a capacity characterization; its abstract explicitly says substantial numerical work is required to make the framework operational. The repository has separately recovered the source stationarity obligation and rejected the arbitrary-`c` modulo-`m` shortcut because its inequality direction does not yield the required positive primal comparison. Thus a floating finite-lift stationary solve remains support, not a directed certificate.
3. **Montanari--Zhong--Zhou, arXiv:2110.15824.** This supplies rigorous upper/lower interpolation-threshold bounds and the LP threshold, not the exact `kappa=-1` SAT/UNSAT threshold. The repository keeps `alpha_L=6.30297437506` from that rigorous layer.
4. **Annesi--Malatesta--Zamponi, arXiv:2410.06717**, and **Winer--Herderschee, arXiv:2503.11761**, provide full-RSB/jammed-Parisi calculations useful for structural guidance, not the missing exact-radius directed proof.
5. **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** Their theorem is algorithmic: it exactly characterizes projections attainable by a dimension-free-Lipschitz algorithm class and explicitly says the unrestricted feasible-projection problem remains a major outstanding challenge.

A fresh bounded search on 20 September 2026 did not surface a later rigorous theorem plainly closing the unrestricted exact-radius `kappa=-1` threshold. This is dated negative search evidence, not a global novelty or priority certificate. The repository's POSTED zero-margin/Ising exclusions are different source problems and are not reopened here.

## 2. Original problem before / after

Two evidence tiers remain separate.

### 2.1 Review-pending directed tier

The latest companion has exhausted the complete-second exact transport chart. This run does **not** mine that chart again and makes no directed-tier change:

`before = after = [6.30297437506, 12.3196344461907498]`,

width

`6.0166600711307498`.

The prospective complete-third positive-gap point near `12.31643335693` remains **CONDITIONAL / NOT PROMOTED** pending an outward tube/cascade certificate.

### 2.2 Stronger supported-CONDITIONAL complete-third tier

The entering supported conditional endpoint is

`12.287222221600`.

The executed checker solves the complete-third fixed-density stationarity equations and keeps the comparison positive at

`boxed: alpha = 12.287222221598`.

Hence the supported conditional bracket moves strictly from

`[6.30297437506, 12.287222221600]`

to

`boxed: [6.30297437506, 12.287222221598]`,

with exact width

`boxed: 5.984247846538`.

The supported source-level upper-endpoint gain is exactly

`boxed: 2e-12`.

This is a threshold-candidate improvement, not merely an auxiliary constant, but it is **SUPPORTED CONDITIONAL / NUMERICAL_ONLY**, not directed interval arithmetic.

## 3. Gaussian heat-log transform and the monotone-curvature cone

For `s>0`, define the Hopf--Cole / Gaussian heat-log transform

`T_s f(x) := log E exp[f(x+sqrt(s)G)]`, `G~N(0,1)`.

For smooth data, `u(s,x)=T_s f(x)` solves

`u_s = (u_xx+u_x^2)/2`.                                    (3.1)

### Theorem NM03-T03-MONOTONE-CURVATURE-CONE

Assume `f` is such that, in the classical sense (or distributionally with approximation),

`f'<=0`, `f''<=0`, `f'''<=0`.

Then for every `s>0`,

`(T_s f)'<=0`, `(T_s f)''<=0`, `(T_s f)'''<=0`.              (3.2)

In particular the cone of decreasing concave functions whose curvature is nonincreasing is invariant under the Gaussian heat-log semigroup.

#### Proof

Monotonicity is immediate: `exp(f)` is decreasing, Gaussian convolution preserves order under translation, and `log` is increasing.

For the curvature signs, first take smooth bounded-curvature data and put

`A := -u_xx`, `B := A_x = -u_xxx`.

Differentiating (3.1) gives

`A_s = (1/2) A_xx + u_x A_x - A^2`,                         (3.3)

and then

`B_s = (1/2) B_xx + u_x B_x - 3 A B`.                      (3.4)

If `A(0,.)>=0`, the parabolic maximum principle applied at a first zero-crossing of (3.3) prevents `A` from becoming negative: at the crossing `A=0`, `A_x=0`, `A_xx>=0`, and the reaction term vanishes. Thus `A>=0` for all positive times.

With `A>=0` fixed, (3.4) is linear in `B` with zeroth-order coefficient `-3A<=0`. The positivity-preserving parabolic maximum principle therefore gives `B>=0` from `B(0,.)>=0`. Hence `u_xx<=0` and `u_xxx<=0`.

For nonsmooth data with distributional `f'''<=0`, approximate `A_0=-f''` by smooth nonnegative nondecreasing `A_0^eps`, integrate twice to obtain smooth `f_eps` with the same three sign conditions, apply the preceding argument, and pass to the limit at every positive heat time using Gaussian smoothing. QED.

### Corollary 3.1 — special hinge kernel

Take

`f_beta(x) = -(beta/2) x_+^2`, `beta>0`.

Here

`-f_beta'' = beta 1_{x>0}`

is nonnegative and nondecreasing, while distributionally

`f_beta''' = -beta delta_0 <=0`.

Therefore the inner perceptron kernel

`U_beta(t)=log E_H exp[-beta(t+H)_+^2/2] = T_1 f_beta(t)`

satisfies

`U_beta'<=0`, `U_beta''<=0`, `U_beta'''<=0`.                 (3.5)

The companion already proved the sharp curvature range

`-ell <= U_beta'' <=0`, `ell=beta/(1+beta)`.

Now let

`q(a)=log E_G exp[m U_beta(a+dG)] = T_{d^2}(mU_beta)(a)`,

with `m>0,d>0`. Scaling by `m` preserves the cone hypotheses, so

`boxed: q'<=0, q''<=0, q'''<=0`.                            (3.6)

Together with the prior sharp smoothing bound,

`-L <= q'' <=0`, `L=m ell/(1+m ell d^2)`,                   (3.7)

we now know that `q''` decreases monotonically from `0` toward its right-tail value rather than merely remaining in a fixed interval.

This sign is special to the hinge's monotone-curvature initial data. It is **not** a generic statement that variance decreases under every negative-energy tilt; older project work contains counterexamples to such a generic claim.

## 4. New local comparison: curvature-energy self-bound

The monotone-curvature sign yields a strictly stronger score comparison than the preceding global `L`-smooth bound.

### Theorem NM03-T03-LOCAL-CURVATURE-ENERGY

Let `q` satisfy

`q<=0`, `q'<=0`, `q''<=0`, `q'''<=0`,

and assume `q,q',q'' ->0` as `a->-infinity`. Then

`boxed: q'(a)^2 <= 2[-q(a)][-q''(a)]`                       (4.1)

for every `a`.

For the perceptron conditional score

`g(a)=E_{nu_a} U_beta'(T)=q'(a)/m`,

this gives

`boxed: g(a)^2 <= 2[-q(a)][-q''(a)]/m^2`.                  (4.2)

#### Proof

Set `F=-q`. Then

`F>=0`, `F'>=0`, `F''>=0`, `F'''>=0`,

with all of `F,F',F''` tending to zero at the left boundary. Define

`H(a)=2F(a)F''(a)-F'(a)^2`.

A cancellation gives

`H'(a)=2F(a)F'''(a)>=0`.

Since `H(-infinity)=0`, `H>=0`, proving (4.1). Division by `m^2` gives (4.2). QED.

The preceding global smoothing theorem only gave

`g(a)^2 <= 2L[-q(a)]/m^2`.

Because `-q''(a)<=L`, (4.2) is always at least as strong and can be much stronger in the left/central region where the local curvature is far below its right-tail cap.

## 5. New feasibility compiler: obtain `S1` from spatial scalar-`q` secants only

The latest NM13-07 scalar-`Q` compiler obtains

`S1 = E_V g(a(V))^2`

by introducing an auxiliary variance-transfer coordinate `rho` and taking a derivative of the fully outer scalar `Q`. That is valid, but it requires extra scalar-`Q` evaluations off the physical variance point.

The concavity of the already-computed conditional `q` gives a cheaper exact alternative.

Let

`a(v)=a0+s v`, `s>0`,

and

`r(v)=q(a(v))`.

Then

`r'(v)=s m g(a(v))`,                                        (5.1)

and from (3.6)

`r'<=0`, `r''<=0`.

Hence `r'` is nonincreasing and `r'(v)^2` is nondecreasing.

Take an equal-width mesh `v_i=v_0+i h`. Define the backward and forward scalar secants

`b_i = [r(v_i)-r(v_{i-1})]/h`,

`f_i = [r(v_{i+2})-r(v_{i+1})]/h`.

Both are nonpositive.

### Theorem NM03-T03-SPATIAL-SECANT-S1

For every `v in [v_i,v_{i+1}]`,

`boxed: b_i^2/(s^2 m^2) <= g(a(v))^2 <= f_i^2/(s^2 m^2)`.   (5.2)

Consequently, with

`P_i=Phi(v_{i+1})-Phi(v_i)`,

`boxed:`

`sum_i b_i^2 P_i/(s^2 m^2)`
` <= integral_{central mesh} g(a(v))^2 phi(v)dv`
` <= sum_i f_i^2 P_i/(s^2 m^2)`.                            (5.3)

The only non-algebraic inputs are the scalar values `r(v_j)=q(a(v_j))` already required by the outer `Q` cell compiler. No `rho`-shifted variance evaluation is needed.

#### Proof

Concavity gives

`b_i >= r'(v_i)`

because a left secant is at least the derivative at its right endpoint. Since both sides are nonpositive,

`-b_i <= -r'(v_i)`.

Similarly, the forward secant satisfies

`f_i <= r'(v_{i+1})`,

so

`-r'(v_{i+1}) <= -f_i`.

Because `r'` is nonincreasing and nonpositive,

`-r'(v_i) <= -r'(v) <= -r'(v_{i+1})`

throughout the cell. Combining the three inequalities and squaring yields

`b_i^2 <= r'(v)^2 <= f_i^2`.

Equation (5.1) gives (5.2), and Gaussian integration gives (5.3). QED.

### Corollary 5.1 — derivative-free local curvature upper cage from three scalar values

The stronger sign `r'''<=0` means `r''` is nonincreasing. The centered second difference obeys the exact triangular-kernel identity

`Delta_h^2 r(c)`
` := [r(c+h)-2r(c)+r(c-h)]/h^2`
` = integral_{-1}^1 (1-|u|) r''(c+hu) du`.                 (5.4)

Therefore

`r''(c+h) <= Delta_h^2 r(c) <= r''(c-h)`.                  (5.5)

For a cell `[a,b]` of width `h`, set `c=b+h`. Then throughout the cell

`-r''(v) <= -Delta_h^2 r(b+h)`.                             (5.6)

Combining (4.1), the monotonicity of `-r`, and the affine scaling gives a local score upper bound using only the three scalar values `r(b),r(b+h),r(b+2h)`:

`boxed:`

`g(a(v))^2`
` <= 2[-r(b)] [-Delta_h^2 r(b+h)]/(s^2 m^2)`.               (5.7)

This is useful when a one-sided `S1` face is enough: it replaces the old global curvature cap by a data-local curvature cap obtained from neighboring scalar partition values.

## 6. Application to NM13-07's named obstruction

The latest companion residual cascade is

`(Rscale, RU, Rratio, Rhat_H)` versus `(w0,w1,m,x)`

at prescribed positive objective gap `delta=10^-3`. After NM13-03's earlier exact KL-free row transformation, the final residual has the structure

`Rhat_H = A_alg Q + B_alg S1`,

with all other factors algebraic.

The newest NM13-07 report had already collapsed `S1,S2,H1,D_U` to directional derivatives of one scalar `Q`, but `S1` still consumed the auxiliary `rho` variance-transfer direction. Theorem 5 removes that direction:

- the conditional scalar `q(a(v_i))` values are already needed to enclose the outer `Q` integral;
- the same values now give a two-sided `S1` interval by (5.3);
- thus the final KL-free Schur row no longer requires any `rho`-shifted nested partition evaluations;
- only the remaining `tau,beta,m` auxiliary directions are needed for `S2,H1,D_U`.

This is a direct reduction of the outward tube dependency burden, not merely a new constant.

### Demonstrated numerical gain at the `delta=10^-3` waypoint

At

`w0=0.0321710159451139`,
`w1=0.370106966023378`,
`x=3.54218891058057`,
`m=0.226621581517544`,

one has

`ell=0.7164129802019763`,
`L=0.056613228195001718`.

A GH240 falsification scan confirms decreasing curvature over `a in [-15,20]`; the largest forward increment in the sampled `q''` sequence is already negative,

`-3.5227260700e-7`.

The exact local energy inequality is nearly active in the relevant right tail: the maximum sampled utilization of

`q'^2 / (2(-q)(-q''))`

is about

`0.94538`.

The actual numerical score moment is

`S1 = 0.09425868216343047`.

The preceding global self-bound gives

`S1 <= 0.21450436822048513`.

Using the new local curvature comparison pointwise and averaging gives

`S1 <= 0.12990479336209018`.

Thus the remaining upper slack contracts from

`0.12024568605705466`

to

`0.03564611119865971`,

a reduction of

`boxed: 70.3556%`.

This averaged line is a numerical demonstration because it uses floating `q''`; the theorem itself is exact. For an outward proof, Corollary 5.1 replaces floating `q''` by scalar second differences.

The spatial-secant compiler is stronger still as a direct two-sided numerical enclosure on `V in [-6,6]`. Using only conditional scalar `q` values, the observed intervals are

- 100 cells: `[0.07483223417, 0.11849322902]`;
- 200 cells: `[0.08400128092, 0.10571607571]`;
- 400 cells: `[0.08898713038, 0.09983006675]`;
- 800 cells: `[0.09158630673, 0.09700596735]`.

The independently integrated central reference is

`0.09425865505655`.

The numerical contribution outside `[-6,6]` is only `2.71e-8`; a directed implementation must not use that floating fact, but can close the tails with the explicit score-tail bounds already proved in the preceding NM13-03/NM13-07 reports. The central secant width roughly halves under mesh doubling, as expected from first-order derivative bracketing.

## 7. Supported complete-third endpoint check

At the improved density

`alpha=12.287222221598`,

the fixed-density complete-third stationary solve gives positive comparison at every tested GH order:

- GH160: `Psi3=1.4593881659e-13`;
- GH200: `Psi3=1.8213208719e-13`;
- GH240: `Psi3=1.8135493107e-13`;
- GH280: `Psi3=1.8246515410e-13`;
- GH320: `Psi3=1.8196555374e-13`.

At GH320 the full gradient residual infinity norm is about

`1.031e-14`,

and the independent scale-gap reconstruction is

`1.7683077225e-13>0`.

An independently coded adaptive two-dimensional quadrature at the GH320 stationary parameters gives

`Q=-0.09805373188968737`

and reconstructs

`Psi3=1.1668443989e-13>0`.

These are **NUMERICAL_ONLY** falsification/support checks. The adaptive routine's reported quadrature error is not a directed outward error bound, so this endpoint is not promoted beyond SUPPORTED CONDITIONAL.

## 8. Failure / scope boundary preserved honestly

1. The sign `q'''<=0` is **special** to the hinge's monotone-curvature initial potential and to positive Gaussian heat-log evolution. A generic claim that negative-energy tilts have decreasing variance is false; earlier project work exhibited counterexamples. This report does not revive that false route.
2. The local energy cage is much tighter than the previous global one, but it still has nonzero slack. It does not alone decide every final Schur-row face.
3. The spatial-secant `S1` compiler eliminates the auxiliary `rho` direction but remains only one component of the complete-third outward certificate. The `tau,beta,m` directions and the nested projective branch tube still require directed scalar-`Q` evaluation.
4. No full third-level Krawczyk / nested-Schur inclusion is claimed here. The review-pending directed source endpoint therefore remains `12.3196344461907498`.
5. The stronger complete-third endpoint near `12.287222221598` remains **SUPPORTED CONDITIONAL**, not a theorem for the original threshold until the source stationarity/root enclosure is directed.

## 9. Essential executed artifacts

Checker:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_monotone_curvature_alpha12287222221598.py`

creation commit

`23ba90615cef77a5e220f0eeaa8afa46bc341405`.

Archived actual stdout:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_monotone_curvature_alpha12287222221598.out`

creation commit

`e9369aa0d37e66639508d57fff964cccc2a2b283`.

Its final line is

`ALL_MONOTONE_CURVATURE_AND_SUPPORTED_BOUND_CHECKS_PASS`.

## 10. Next attack

The non-duplicative next step is now narrower:

1. keep NM13-07's inner semiconcave scalar-`q` evaluator and outer scalar-`Q` secant/parabola cells;
2. replace the `rho` auxiliary derivative evaluations by Theorem 5's spatial `S1` secants, using directed endpoint `q` intervals and existing explicit tails;
3. retain scalar auxiliary secants only for `tau,beta,m`, yielding `S2,H1,D_U`;
4. feed these intervals into the already pivoted `(Rscale,RU,Rratio,Rhat_H)` nested-Schur cascade;
5. first certify the robust `delta=10^-3` waypoint and a conservative source endpoint below `12.31950`; then tighten toward the numerical positive-gap branch near `12.31643335693`; only afterward attempt the complete-third capacity branch near `12.2872222216`.

A successful outward certificate at the first waypoint would be the next non-microscopic **directed** source improvement.

## 11. ledger_delta

- parent: `T03 negative spherical perceptron`, `kappa=-1`, exact sphere radius `sqrt(N)`, iid Gaussian constraints;
- status: **OPEN / PARTIAL**;
- review-pending directed source bracket before/after: unchanged at `[6.30297437506, 12.3196344461907498]`;
- supported-CONDITIONAL complete-third bracket before: `[6.30297437506, 12.287222221600]`;
- supported-CONDITIONAL complete-third bracket after: `[6.30297437506, 12.287222221598]`;
- exact supported upper-endpoint gain: `2e-12`;
- exact supported width after: `5.984247846538`;
- substantive new theorem 1: Gaussian heat-log semigroup preserves the cone `f'<=0,f''<=0,f'''<=0`; applied to the hinge gives `U'''<=0` and then `q'''<=0`;
- substantive new theorem 2: local curvature-energy comparison `q'^2 <= 2(-q)(-q'')`;
- substantive new theorem 3: two-sided spatial-secant `S1` compiler using only conditional scalar `q` values already required by outer `Q` cells;
- demonstrated mechanism gain: removes the `rho` auxiliary variance direction from the `S1` compiler; local score upper slack shrinks by about `70.36%` at the archived positive-gap waypoint; 800-cell scalar-q secants give numerical central `S1` interval `[0.0915863,0.0970060]` around `0.0942587`;
- named obstruction attacked: NM13-07's outward scalar-`Q` positive-gap tube and KL-free final Schur row;
- remaining obstruction: directed scalar-`Q` cells/tails over the full projective tube for the remaining `tau,beta,m` directions and nested-Schur inclusion;
- failed/forbidden generalization: monotone curvature is not asserted for generic negative-energy tilts; generic variance monotonicity is false;
- complete-second route: **SATURATED / RETIRED as substantive route**;
- runtime model/effort: **GPT-5.6 Sol / UNVERIFIED reasoning level**.
