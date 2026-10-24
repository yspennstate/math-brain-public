Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-07 / T03 — double semiconcavity and scalar-free-energy compiler; endpoint 12.3196344461907498

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03`  
Status: **PARTIAL / STRICT REVIEW-PENDING DIRECTED SOURCE-BRACKET IMPROVEMENT / NEW COMPLETE-THIRD SCALAR-Q COMPILER / THIRD-FULL ROOT STILL CONDITIONAL PENDING OUTWARD TUBE EXECUTION**

## 0. Short handoff and exact source freeze

The source model remains exactly

- `M=floor(alpha N)`;
- rows `g_a iid N(0,I_N)`;
- `||sigma||_2=sqrt(N)` exactly;
- `<g_a,sigma> >= -sqrt(N)` for all `a<=M` (`kappa=-1`);
- fixed `alpha`, `N->infinity`.

No ball relaxation, changed sphere radius, radial renormalization, Ising restriction, algorithmic-class threshold, or replica/full-RSB-only value is used as a source implication.

The latest own report proved the sharp inner hinge semiconcavity

`-beta/(1+beta) <= U'' <= 0`

for the dimensionless hinge log-kernel and used it to make each *middle* Gaussian conditional partition integral an explicit tangent/quadratic Gaussian-cell enclosure. The latest relevant companion report removed `D_H` from the final positive-gap Schur row through the exact KL-free identity

`Rhat_H = RH + RU/(x-1) + (m w1/lambda) Rscale`.

The remaining obstruction was still substantial: the complete-third residuals used four different outer moments `S1,S2,H1,D_U`, each requiring its own directed propagation across the parameter tube. This run changes the attack. It proves that **all four moments are directional derivatives of one scalar nested free energy `Q`, with a usable convexity/concavity sign in every required auxiliary direction**. Combined with a new outer semiconcavity theorem, the entire four-overlap residual map can therefore be enclosed using only scalar partition values and algebraic operations.

The complete-second transport route is already saturated. A final exact bookkeeping sliver is recorded in Section 2 only because the owner requires a strict source before/after when one is available; the substantive work is Sections 3--6.

## 1. Primary-source hypotheses and current proof status, refreshed 20 September 2026

### 1.1 El Alaoui--Sellke, arXiv:2010.15811

Their ambient problem exactly matches the required Gaussian spherical geometry: independent standard Gaussian constraints and `sigma` on the sphere of radius `sqrt(N)`, with `<g_a,sigma> >= kappa sqrt(N)`. For `kappa<0`, however, their algorithm outputs a feasible vector on radius `sqrt(qbar N)` with `qbar in (0,1)` and expects `qbar->1` only near capacity. This does not establish the exact full-radius threshold required by T03.

### 1.2 Stojnic, arXiv:2312.16531

The paper fits the negative spherical perceptron into fully lifted RDT and states a capacity characterization through stationarized full lifting. It explicitly notes that making fl-RDT fully operational requires substantial numerical work and reports rapid convergence by the third stationarized level. The source implication used in this repository therefore remains separated from a floating stationary solve: the non-fixed lifting parameters must satisfy the stationarity system (or an exactly equivalent certified reduction) before the positive comparison value is promoted.

### 1.3 Rigorous and later work

- Montanari--Zhong--Zhou, arXiv:2110.15824, prove rigorous upper/lower bounds on the interpolation threshold and characterize the linear-programming threshold. They do not identify the exact `kappa=-1` SAT/UNSAT threshold. The repository retains `alpha_L=6.30297437506` from this rigorous layer.
- Annesi--Malatesta--Zamponi, arXiv:2410.06717, compute the transition under a full-RSB ansatz. This is structural guidance, not the missing source-valid directed certificate.
- Winer--Herderschee, arXiv:2503.11761, use a jammed Parisi ansatz to compute `P(SAT)`/threshold behavior; again this is not substituted for a rigorous exact-radius proof.
- Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026, exactly characterize a dimension-free-Lipschitz algorithmic projection-pursuit class and explicitly state that characterizing all feasible projections in the non-algorithmic problem remains a major outstanding challenge.

A bounded fresh source search on 20 September 2026 did not surface a later rigorous theorem plainly closing unrestricted exact-radius `kappa=-1`. This is dated negative evidence, not a novelty or priority claim. `POSTED.md` excludes the owner's zero-margin/Ising perceptron work from duplicate research; that restricted result is a different source problem and does not close T03.

## 2. Source-threshold before/after — final exact complete-second sliver

Entering review-pending directed endpoint from the preceding NM13-07 report:

`alpha_U(before)=12.31963444619075`.

Take

`alpha_U(after)=12.3196344461907498`.

The exact gain is

`1/5000000000000000 = 2e-16`.

The inherited directed recentered complete-second chart is uniform for density decrements from the anchor `alpha_0=12.319635` in

`[4.46e-7,5.54e-7]`.

The new decrement is exactly

`2769046251/5000000000000000 = 5.538092502e-7`,

so the already certified stationary branch exists at the new endpoint. Reusing the inherited exact stationary-objective slope cap

`dPsi/dalpha <= 4136629/105883920`

and anchor lower bound

`Psi(alpha_0) >= 23584189005311/1090044380000000000000`,

exact rational transport gives

`Psi(alpha_U(after))`
` >= 27370402538833/9618180994030800000000000000000`
` = 2.8456942696149635e-18 > 0`.

Hence, under the same source-matched stationarized complete-sfl implication used by the archived directed certificates, exact-sphere asymptotic UNSAT holds at `alpha_U(after)`. Constraint monotonicity gives the review-pending bracket

`boxed: 6.30297437506 <= alpha_c(-1) <= 12.3196344461907498`,

with width

`boxed: 6.0166600711307498`.

This is a genuine but microscopic source movement. The inherited linear transport zero lies only about `7.3e-17` below this endpoint. The complete-second route is therefore **retired as a substantive attack**; no further same-chart decimal shaving should count as progress.

## 3. New theorem I — semiconcavity survives the middle Gaussian log-partition

Fix `ell>0` and let `U:R->R` satisfy

`-ell <= U'' <= 0`.

For `m>0`, `d>0`, define

`q(a)=log E_G exp[m U(a+dG)]`.

Let `nu_a` be the tilted law on `T` with density proportional to

`exp[mU(T)] exp[-(T-a)^2/(2d^2)] dT`.

### Theorem NM07-T03-OUTER-SEMICONCAVITY

For every `a`,

`boxed: -m ell/(1+m ell d^2) <= q''(a) <= 0`.               (3.1)

#### Proof

The exponential-family identities are

`q'(a)=(E_nu T-a)/d^2`,

`q''(a)=Var_nu(T)/d^4-1/d^2`.                               (3.2)

The tilted potential is

`V_a(t)=(t-a)^2/(2d^2)-mU(t)`,

so

`1/d^2 <= V_a''(t) <= 1/d^2+m ell`.                         (3.3)

The lower curvature in (3.3) and one-dimensional Brascamp--Lieb give

`Var_nu(T) <= d^2`,

which yields the upper bound `q''<=0`.

For the complementary variance lower bound, integration by parts gives

`E[(T-ET)V_a'(T)]=1`.                                       (3.4)

The map `V_a'` is globally `L`-Lipschitz with

`L=1/d^2+m ell`.

For any scalar random variable and any `L`-Lipschitz function, the iid-copy identity gives

`Var(V_a'(T)) <= L^2 Var(T)`.

Cauchy--Schwarz in (3.4) therefore implies

`1 <= sqrt(Var(T)Var(V_a'(T))) <= L Var(T)`,

hence

`Var(T) >= 1/L = d^2/(1+m ell d^2)`.                        (3.5)

Substitution in (3.2) proves (3.1). QED.

For the perceptron hinge kernel, the preceding report proved

`ell=beta/(1+beta)`

with `beta=xi-1`, so this theorem is global and parameter-explicit.

### Corollary — derivative-free outer Gaussian cells

If the outer mean is affine,

`a(v)=b v-c`,

then

`-C <= d^2q/dv^2 <= 0`,

where

`boxed: C=b^2 m ell/(1+m ell d^2)`.                          (3.6)

On a cell `[r,s]`, let `L_rs(v)` be the chord through `(r,q(r))` and `(s,q(s))`. Concavity and (3.6) imply

`boxed: L_rs(v) <= q(v) <= L_rs(v)+(C/2)(v-r)(s-v)`.        (3.7)

Indeed `q-L_rs` is concave with zero endpoint values, hence nonnegative. The function

`(C/2)(v-r)(s-v)-(q-L_rs)`

also has zero endpoint values and second derivative `-C-q''<=0`, so it too is nonnegative.

Both Gaussian cell integrals in (3.7) are closed. Put

`P=Phi(s)-Phi(r)`,
`I1=phi(r)-phi(s)`,
`I2=r phi(r)-s phi(s)+P`,
`sec=(q(s)-q(r))/(s-r)`.

Then

`int_r^s L_rs(v)phi(v)dv`
` = q(r)P + sec [I1-rP]`,                                  (3.8)

and

`int_r^s (v-r)(s-v)phi(v)dv`
` = -I2+(r+s)I1-rsP`.                                      (3.9)

In particular a cell of width `h` contributes uncertainty at most

`C h^2 P/8`,

so a uniform interior mesh has a deterministic `O(h^2)` enclosure width. The already proved explicit Gaussian right-tail envelope for `-q` closes the truncation tails. Endpoint values `q(r),q(s)` themselves are enclosed by the preceding **inner** semiconcave Gaussian-cell theorem. Thus the two nested Gaussian levels are now both controlled by second-order, derivative-free scalar cell bounds.

### A useful third-derivative fallback

The same tilted law is `1/d^2`-strongly log-concave. Poincare applied to `(T-ET)^2` gives

`E(T-ET)^4 <= 5d^4`.

Since

`q'''(a)=kappa_3(T)/d^6`,

Cauchy yields

`boxed: |q'''(a)| <= sqrt(5)/d^3`.                           (3.10)

After `a=bv-c`, a centered secant therefore approximates `q_v` with a rigorous error at most

`sqrt(5)(b/d)^3 h^2/6`.

Section 4 makes this fallback unnecessary for the four principal moments, but it is useful for parameter-tube Jacobian bounds.

## 4. New theorem II — every complete-third moment is a derivative of one scalar `Q`

The key simplification is to expose the Gaussian layers as heat semigroups. Let

`h_beta(x)=exp[-beta x_+^2/2]`,

`u(r,x)=log P_r h_beta(x)`,

where `P_r` is the one-dimensional Gaussian heat semigroup of variance `r`. Let

`q(s,r,a;m)=log P_s exp[m u(r,.)](a)`,

and finally

`Q(t,s,r,a0;m,beta)=P_t q(s,r,. ;m)(a0)`.

At the physical positive-gap point,

`r=1`, `s=d^2=w1/w0`, `t=b^2=w2/w0`,

`a0=-1/sqrt(w0)`.

The auxiliary variance changes below are **proof devices inside this exact representation**, not changes of the perceptron sphere or source disorder.

### 4.1 Exponent direction: `D_U`

At fixed `(t,s,r,a0,beta)`,

`Q_m=P_t <u>`

and

`Q_mm=P_t Var(u) >=0`.

Therefore

`boxed: D_U = m Q_m-Q`,                                    (4.1)

and `Q` is convex in the auxiliary exponent `m`. One-sided `m` secants rigorously enclose `Q_m`, hence `D_U`.

### 4.2 Penalty direction: `H1`

For the inner hinge tilt,

`u_beta=-1/2 E_rho X_+^2`,

`u_betabeta=1/4 Var_rho(X_+^2) >=0`.

Consequently

`Q_betabeta`
`=P_t[ m< u_betabeta > + m^2 Var(u_beta) ] >=0`,

and

`boxed: Q_beta=-(m/2) H1`.                                  (4.2)

Thus convex one-sided `beta` secants enclose `H1` without directly integrating the positive-tail moment observable.

### 4.3 Variance transfer `H -> U`: `S2`, with a new concavity theorem

Let

`D_tau := partial_s-partial_r`,

corresponding to the auxiliary path `s->s+tau`, `r->r-tau`, with total inner-plus-middle Gaussian variance fixed. The heat equations

`u_r=(u_xx+u_x^2)/2`

and the middle log-heat equation give the exact score identity

`D_tau q = [m(m-1)/2] <u_x^2>`.                             (4.3)

After applying the outer heat semigroup,

`boxed: Q_tau=[m(m-1)/2] S2`.                               (4.4)

The missing fact was the curvature sign of this direction.

### Theorem NM07-T03-TAU-CONCAVITY

For `0<m<1`,

`boxed: Q_tautau <=0`.                                      (4.5)

#### Proof

For a middle tilted expectation `<.>`, direct differentiation gives, for any smooth `f`,

`D_tau <f>`
`= 1/2 < f_xx+2m u_x f_x > - <f_r>`
`  + [m(m-1)/2] Cov(f,u_x^2)`.                              (4.6)

Set `f=u_x^2`. Using

`(u_x)_r=(u_xxx+2u_xu_xx)/2`,

(4.6) reduces exactly to

`D_tau <u_x^2>`
`= < u_xx^2+2(m-1)u_x^2u_xx >`
`  + [m(m-1)/2] Var(u_x^2)`.                               (4.7)

Write

`A=-u_xx >=0`, `Z=u_x^2 >=0`.

The middle tilted potential has curvature

`1/s-mu_xx=1/s+mA`.

Brascamp--Lieb applied to `Z` yields

`Var(Z) <= < 4ZA^2/(1/s+mA) >`.                             (4.8)

The negative variance contribution in (4.7) is therefore at most

`2m(1-m)< ZA^2/(1/s+mA) >`
` <=2(1-m)<ZA>`,                                            (4.9)

because `mA/(1/s+mA)<=1`. The positive non-variance part of (4.7) is exactly

`<A^2+2(1-m)ZA>`.

Combining (4.7)--(4.9) gives the stronger estimate

`D_tau <u_x^2> >= <A^2> >=0`.                               (4.10)

Multiplying by `m(m-1)/2<0` in (4.3), then applying the positive outer heat semigroup, proves (4.5). QED.

Thus `S2` is also enclosed by one-sided secants of the scalar `Q`; no separate `U_x^2` moment evaluator remains.

### 4.4 Variance transfer `U -> V`: `S1`, also concave

Let

`D_rho := partial_t-partial_s`,

corresponding to `t->t+rho`, `s->s-rho`. Since the middle partition satisfies

`q_s=(q_aa+q_a^2)/2`,

one obtains

`D_rho Q = -1/2 P_t(q_a^2)`.

But `q_a=m<u_x>`, so

`boxed: Q_rho=-(m^2/2) S1`.                                 (4.11)

Moreover `q_aa<=0` by Section 3. If `F=P_t(q_a^2)`, then

`D_rho F`
`=P_t[ q_aa^2-2q_a^2 q_aa ] >=0`.                          (4.12)

Hence

`boxed: Q_rhorho<=0`.                                       (4.13)

Again one-sided scalar secants enclose the required derivative.

## 5. Consequence — the four-overlap residual map is scalar-Q only

At prescribed positive comparison gap `delta>0`, the already proved dimensionless compiler uses the four moments

`S1, S2, H1, D_U`

(after the companion's exact KL-free row removes `D_H`). Sections 4.1--4.4 give

`S1 = -2 Q_rho/m^2`,

`S2 =  2 Q_tau/[m(m-1)]`,

`H1 = -2 Q_beta/m`,

`D_U = mQ_m-Q`.                                             (5.1)

The curvature signs are, respectively,

- `Q` concave in `rho`;
- `Q` concave in `tau` for `0<m<1`;
- `Q` convex in `beta`;
- `Q` convex in the auxiliary exponent `m`.

Therefore **all four moment intervals can be obtained from values of one scalar function `Q` at the base point and at two nearby auxiliary points in each direction**. For a convex direction, the left and right secants bracket the derivative in the usual order; for a concave direction the order is reversed. Multiplication by the known signs in (5.1) then gives outward moment intervals.

This is the main mechanism gain of the run. It removes the need for four different monotone-observable outer integrators and their separate parameter derivatives. The remaining numerical kernel is only the nested scalar partition `Q`; Section 3 and the preceding inner-cell theorem already reduce that quantity to closed `Phi`, `phi`, `exp`, and `log` endpoint arithmetic plus explicit Gaussian tails.

In particular, the pivoted complete-third cascade

`(Rscale,RU,Rratio,Rhat_H)` versus `(w0,w1,m,x)`

can now be evaluated outward without ever integrating `U_x`, `U_x^2`, the positive-tail second moment, `D_U`, or an inner KL observable directly. This directly complements NM13-03's comparison theory: its KL-free final row and the present scalar-Q compiler collapse the non-algebraic burden to one scalar partition function.

## 6. Executed sanity checks and demonstrated numerical gain

The analytic theorems above do not rely on floating quadrature. Two executable falsification checkers were nevertheless run and archived.

### 6.1 Double-semiconcavity/cell checker

At the robust prescribed-gap waypoint `delta=10^-3`, approximately

`w0=0.0321710159451`,
`w1=0.3701069660234`,
`x=3.54218891058`,
`m=0.226621581518`,
`xi=3.52625448341119`,

it gives

`ell=0.7164129802019763`,
`d^2=11.504360529204533`,
`b^2=18.5795194982734`,

and the new outer curvature cap

`C=1.0518465771092356`.

Finite differences of `q_vv` at `v=-5,-3,-1,0,1,3,5` all lie in `[-C,0]`; at `v=5` the value is about `-1.04680`, showing the lower curvature bound is numerically close to active in the right tail.

For the truncated outer scalar integral on `[-6,6]`, an independent high-accuracy numerical reference is

`Q_trunc=-0.09729503964145682`.

The proved secant/parabola cell formula contains that reference at every tested mesh size. Its interval width is

- `5.04886e-3` at 50 cells;
- `1.26222e-3` at 100;
- `3.15554e-4` at 200;
- `7.88885e-5` at 400;
- `1.97221e-5` at 800;
- `4.93053e-6` at 1600.

The width contracts by essentially a factor of four whenever the mesh is doubled, matching the proved `O(h^2)` law. These numbers are **NUMERICAL_ONLY demonstrations** of usefulness, not interval-certified source endpoints.

### 6.2 Directional compiler checker

At the same waypoint, GH140 gives the numerical-only values

`Q=-0.09729505259521637`,
`S1=0.0942586821609841`,
`S2=0.261829946438269`,
`H1=0.06423814503571629`,
`D_U=0.044205704383740704`.

The derivative identities predict

`Q_tau=-0.022944713326197855`,
`Q_rho=-0.0024204376508503407`,
`Q_beta=-0.007278875010873697`,
`Q_m=-0.2342643090563982`.

Centered finite differences at steps `10^-3,5e-4,2e-4,10^-4` converge to these values. The corresponding second differences retain exactly the proved signs:

- `Q_tautau ~= -0.01719030 <0`;
- `Q_rhorho ~= -0.00032916 <0`;
- `Q_betabeta ~= +0.00408746 >0`;
- `Q_mm ~= +0.806235 >0`.

The checker also symbolically verifies the decisive Brascamp--Lieb domination remainder

`2(1-m)ZA - 2m(1-m)ZA^2/(1/s+mA)`
`= 2(1-m)ZA/(1+mAs) >=0`.

Again, the floating lines are falsification checks only; the sign theorems are analytic.

## 7. Residual obstruction, failed route, and next attack

### Residual obstruction

The prospective third-full endpoint near

`alpha ~= 12.31643335693`

at exact prescribed objective gap `Psi_3=10^-3` remains **CONDITIONAL / NUMERICAL_ONLY**. It is not entered into the source bracket. The missing task is now narrower than in the previous run: implement one outward scalar `Q` evaluator over the small projective branch tube and combine scalar secant evaluations in the four auxiliary directions with the already pivoted nested-Schur continuation.

### Failed/superseded route preserved

The previous route attempted to outward-integrate `S1,S2,H1,D_U` as four distinct monotone observables. It was not mathematically wrong, but it multiplied the dependency/tube burden and left a difficult moment-Jacobian layer. This run supersedes that route rather than continuing to tune its meshes. During the present derivation the `tau`-direction curvature initially appeared sign-indefinite because differentiating `<u_x^2>` produces a negative variance term. A crude constant-Poincare bound is too weak. The variable-curvature Brascamp--Lieb estimate (4.8) exactly absorbs that variance term and proves concavity; this is the decisive recovery.

### Next attack

1. Implement outward elementary bounds for the scalar nested `Q` only: inner hinge endpoint `Phi/phi/exp/log` arithmetic, inner semiconcave cells, then the new outer secant/parabola cells and explicit tails.
2. Evaluate `Q` at auxiliary `rho,tau,beta,m` secant points to obtain rigorous intervals for `S1,S2,H1,D_U` via (5.1).
3. Feed those intervals into the pivoted scalar cascade `(Rscale,RU,Rratio,Rhat_H)` and certify the successive `w0,w1,m` branches plus the final two `x` endpoint signs.
4. First target the robust `delta=10^-3` waypoint. A successful inclusion there would move the source upper endpoint non-microscopically from `12.3196344461907498` to approximately `12.31643335693`; only after that should continuation pursue the stronger NM13-03 conditional capacity branch near `12.2872222216`.

## 8. Essential executed artifacts and readback target

Executed scalar-Q cell checker:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_double_semiconcave_qcompiler.py`

creation commit `1378cb2f36e2ee534d96b26d9232654b506744cd`.

Archived stdout:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_double_semiconcave_qcompiler.out`

creation commit `b09b996e964c771573ebc2b0a9104a0be8b0d6de`; its final line is

`ALL_EXACT_AND_NUMERICAL_DOUBLE_SEMICONCAVITY_CHECKS_PASS`.

Executed variance-transfer checker:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_variance_transfer_concavity.py`

creation commit `08c1f2615002c8a4282a4dc77b30cf88ed78d257`.

Archived stdout:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_variance_transfer_concavity.out`

creation commit `c07eed09fb71ab2d1276441a4d5a3ad87d40f963`; its final line is

`ALL_EXACT_AND_NUMERICAL_DIRECTIONAL_COMPILER_CHECKS_PASS`.

## 9. ledger_delta

- parent: `T03 negative spherical perceptron`, exact radius `sqrt(N)`, `kappa=-1`;
- status: **OPEN / PARTIAL**;
- source bracket before: `[6.30297437506, 12.31963444619075]`;
- source bracket after: `[6.30297437506, 12.3196344461907498]`;
- source gain: `2e-16` at the upper endpoint; width after `6.0166600711307498`;
- source mechanism for that microstep: inherited directed complete-second branch plus exact rational objective transport; no new source model;
- substantive new theorem 1: middle Gaussian log-partition preserves explicit two-sided curvature, `-m ell/(1+m ell d^2)<=q''<=0`;
- substantive new theorem 2: derivative-free outer chord/parabola Gaussian-cell enclosure with deterministic `O(h^2)` width;
- substantive new theorem 3: `Q` is concave under both variance transfers `H->U` and `U->V`, while convex in auxiliary `beta` and exponent `m`;
- substantive compiler: `S1,S2,H1,D_U` all become one-sided secant derivatives of a single scalar `Q`;
- demonstrated numerical gain: outer `Q` cell width contracts by factor approximately 4 under mesh doubling; all four directional curvature signs independently match finite differences;
- stronger endpoint `~12.31643335693`: **CONDITIONAL / NOT PROMOTED** pending outward scalar-Q tube/cascade certificate;
- complete-second route: **SATURATED / retire from substantive use**;
- next attack: outward scalar-Q-only pivoted complete-third certificate at `delta=10^-3`;
- runtime model/effort: **GPT-5.6 Sol / UNVERIFIED reasoning level**.
