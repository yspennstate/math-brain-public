Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-07 / T03 — prescribed-positive-gap dimensionless four-overlap compiler, all-moment monotonicity, and endpoint 12.319634446195

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03`  
Status: **PARTIAL / STRICT COMPUTER-ASSISTED SOURCE-BRACKET IMPROVEMENT / NEW EXACT THIRD-FULL COMPILER / PENDING LATER INDEPENDENT REVIEW**

## 0. Short handoff and exact source freeze

The source problem is unchanged:

- `M=floor(alpha N)`;
- `g_1,...,g_M iid N(0,I_N)`;
- `||sigma||_2=sqrt(N)` exactly;
- `<g_a,sigma> >= -sqrt(N)` for every `a<=M`;
- fixed `alpha`, `N->infinity`.

No changed sphere radius, ball relaxation, Ising restriction, radial rescaling, algorithmic-class threshold, or replica/FRSB-only value is used as a source implication.

The entering repository-supported, review-pending directed bracket is

`alpha_L = 6.30297437506`,

`alpha_U = 12.3196344462`,

width `6.01666007114`.

The preceding NM13-07 run proved that the complete-second derivative rectangle is essentially exhausted: its sharp multi-affine objective-slope cap is

`S_* = 4136629/105883920 = 0.03906758457752603...`,

and the source endpoint `12.3196344462` lies only about `9.25e-12` above the limiting transport point from the same anchor/box. Consequently the substantive attack here is **not** another complete-second decimal search. It is a complete-third reduction aimed at the missing outward four-overlap inclusion. A `5e-12` strict complete-second microstep is recorded separately only because the owner requires source before/after to be kept honest.

The latest companion `NM13-03` result supports a stronger complete-third stationary candidate near `12.28722222161`, but explicitly labels it CONDITIONAL / numerical because the four-overlap root is not outward-enclosed. The robust prescribed-positive-gap waypoint with `Psi_3=10^{-3}` lies near `alpha=12.31643335693`; this run targets its certification geometry.

## 1. Primary-source hypotheses and proof status, refreshed 20 September 2026

1. **El Alaoui--Sellke, arXiv:2010.15811.** Their ambient problem is exactly the iid-Gaussian spherical perceptron on the radius-`sqrt(N)` sphere. For `kappa<0` the algorithm described in the abstract uses the conjectural FRSB/Parisi structure and returns a feasible vector on radius `sqrt(qbar N)` with `qbar in (0,1)`; the paper expects `qbar->1` near capacity. This is not the exact full-radius threshold theorem required by T03.
2. **Stojnic, arXiv:2312.16531.** The paper fits the negative spherical perceptron into fully lifted RDT and states a capacity characterization through the stationarized full-lifting machinery. It also states that substantial numerical work is required to make the construction practically operational. The project therefore keeps the source comparison theorem separate from a floating finite-level stationary computation and supplies a directed root-inclusion layer before promoting endpoints.
3. **Montanari--Zhong--Zhou, arXiv:2110.15824.** They rigorously prove upper and lower bounds on the interpolation threshold and characterize the linear-programming threshold; they do not identify the exact `kappa=-1` SAT/UNSAT threshold. The retained source lower endpoint is `6.30297437506` in the repository normalization.
4. **Annesi--Malatesta--Zamponi, arXiv:2410.06717.** The transition is computed using a full-RSB ansatz. It is useful structural guidance, not a replacement rigorous exact-sphere certificate.
5. **Winer--Herderschee, arXiv:2503.11761.** The jammed-Parisi calculation likewise remains ansatz-level guidance for the present proof obligation.
6. **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** They exactly characterize a dimension-free-Lipschitz algorithmic projection-pursuit class and explicitly distinguish the unrestricted non-algorithmic feasible-projection problem as still a major challenge.

A bounded fresh search on 20 September 2026 did not surface a later rigorous theorem plainly closing unrestricted exact-radius `kappa=-1`. This is dated negative evidence, not a novelty/priority certificate.

`POSTED.md` continues to exclude the owner's zero-margin/Ising perceptron work from duplicate research; that restricted posted result does not close this negative-margin continuous spherical target.

## 2. Source-threshold before/after — strict but intentionally microscopic

The preceding directed recentered complete-second chart is centered at density decrement `5e-7` from

`alpha_0=12.319635`

and is certified uniformly for decrements

`[4.46e-7,5.54e-7]`.

Its exact contraction data are

`q = 229179741/467259059 = 0.4904768277590526...`,

`eta = 18671401519768819/40795417037192166 = 0.4576838006765948...`,

with `eta < 1-q`. The anchor objective lower bound is

`Psi(alpha_0) >= 23584189005311/1090044380000000000000`,

and on the same directed derivative rectangle

`0 < dPsi/dalpha <= S_* = 4136629/105883920`.

Take

`alpha_1 = 12.319634446195`

`        = 2463926889239/200000000000`.

Its decrement from the anchor is

`delta_1 = 110761/200000000000 = 5.53805e-7`,

which lies strictly inside the already certified uniform density band. Therefore the inherited Banach map supplies a genuine stationary root at `alpha_1`. Transporting the objective gives the exact lower bound

`Psi(alpha_1)`

` >= 958247216972401/5770908596418480000000000000`

` = 1.6604789366567075e-13 > 0`.

The same source-matched stationarized complete-sfl implication used in the preceding directed certificates therefore gives exact-sphere asymptotic UNSAT at `alpha_1`, and constraint monotonicity gives the new upper endpoint.

Hence the review-pending source bracket moves from

`[6.30297437506, 12.3196344462]`

to

`boxed: [6.30297437506, 12.319634446195]`.

The width moves from `6.01666007114` to

`boxed: 6.016660071135`,

an exact source gain of

`1/200000000000 = 5e-12`.

This source movement is real but **not** the substantive mechanism gain of the run. The complete-second route is now saturated for practical purposes and should not be revisited merely to shave more decimals.

## 3. Exact third-full theorem I — dimensionless prescribed-positive-gap four-overlap compiler

### 3.1 Projective geometry and positive-gap scale

Use the strict complete-third projective chart

`w0=1-p2`, `w1=p2-p3`, `w2=p3`,

with `w_i>0`, `w0+w1+w2=1`, and

`r2=q3/p3`, `r1=(q2-q3)/(p2-p3)`, `r0=(1-q2)/(1-p2)`,

`x=r0 r2/r1^2 > 1`, `y=r1/r2 > 1`,

`Z=x y^2 w0+y w1+w2`.

The already proved q-sector elimination gives

`q3=w2/Z`,

`q2=(y w1+w2)/Z`,

`c2=(x-1)sqrt(Z)/(x y w0)`,

`c3=(y-1)sqrt(Z)/(y w1)`,

`gamma_p=xy/(2sqrt(Z))`.

Define

`S := r1/(r0 sqrt(r2)) = sqrt(Z)/(x y)`.

The scale-Euler identity on a full stationary point is

`Psi_3 = 2 gamma_sq-S`.

Fix a prescribed objective gap `delta>0` and set

`gamma_sq=(S+delta)/2`,

`lambda=S/(S+delta) in (0,1)`,

`xi=1+lambda(x-1)`.

Because `c2=(x-1)S/w0`, the hinge scale becomes

`B=c2/(4 gamma_sq)=lambda(x-1)/(2w0)`,

hence

`B w0=(xi-1)/2`.

This is the key scale removal away from capacity: the positive objective gap enters only through `xi`, not through an unbounded separate `B` coordinate.

The hierarchy can be built into the coordinates. Put `m=c3/c2`. Then

`m=x w0(y-1)/[(x-1)w1]`,

and conversely

`boxed: y=1+m(x-1)w1/(xw0)`.

Thus `(w0,w1,x,m)` with `w0,w1,w2=1-w0-w1>0`, `x>1`, `0<m<1` is a global strict-domain chart.

### 3.2 Dimensionless kernel and five positive moments

For independent standard Gaussians `U,V,H`, put

`T=sqrt(w1/w0) U+sqrt(w2/w0)V-1/sqrt(w0)`.

Define

`F_xi(t)=E_H exp[-(xi-1)(t+H)_+^2/2]`,

`U_xi(t)=log F_xi(t)`.

For fixed `V=v`, let `<.>_v` denote the `U`-tilt proportional to

`exp[m U_xi(T)] d gamma_U`.

Let `rho_t` denote the inner `H`-tilt proportional to

`exp[-(xi-1)(t+H)_+^2/2] d gamma_H`.

Define

`g(v)=<U_t>_v`,

`e2(v)=<U_t^2>_v`,

`h(v)=< E_{rho_T}(T+H)_+^2 >_v`,

`D_U(v)=KL(nu_v||gamma_U)=m<U>_v-log Z_v`,

`K(t)=KL(rho_t||gamma_H)=-(xi-1)E_{rho_t}(t+H)_+^2/2-U_xi(t)`,

`D_H(v)=m<K(T)>_v`.

Their outer averages are

`S1=E_V g(V)^2`, `S2=E_V e2(V)`, `H1=E_V h(V)`,

`D_U=E_V D_U(V)`, `D_H=E_V D_H(V)`.

### Theorem NM07-T03-POSGAP-DIMENSIONLESS-4D

For fixed `delta>0`, strict complete-third stationary points satisfying `Psi_3=delta` are equivalent to strict zeros in `(w0,w1,x,m)` of

`Rratio = S2/S1-(1+y w1/w2)`,

`Rscale = Z S1-w2 lambda^2 (x-1)^2 H1`,

`RU = x^2 w0 (y-1)^2 S1 [w2+w1 k(y)]`
`     -2 w1 w2 (x-1)^2 D_U`,

`RH = x (y-1) w0 S1 [Z-x y^2 w0 h(x)]`
`     -2 w1 w2 (x-1) D_H`,

where

`k(y)=y(y log y-y+1)/(y-1)^2`,

`h(x)=x(x-1-log x)/(x-1)^2`,

and `y,Z,S,lambda,xi` are reconstructed algebraically from `(w0,w1,x,m,delta)`.

At any such zero the source density is reconstructed by the **lambda-free** formula

`boxed: alpha=w2(x-1)^2/[x^2 y^2 w0 S1]`.

In particular, objective positivity is not a posteriori numerical evidence: any certified strict zero has `Psi_3=delta` **exactly**.

#### Proof

Let `z=sqrt(w0)t` in the original complete-third hinge kernel. Since

`B w0=lambda(x-1)/2=(xi-1)/2`,

the inner exponential becomes exactly

`exp[-(xi-1)(t+H)_+^2/2]`.

Spatial differentiation gives

`M1=S1/w0`, `M2=S2/w0`,

and differentiation in the original `B` gives

`MB=w0 H1`.

Also

`4B^2=lambda^2(x-1)^2/w0^2`.

The exact score/gamma stationarity identities therefore become

`q3=S1/[lambda^2(x-1)^2 H1]`,

`q2=S2/[lambda^2(x-1)^2 H1]`,

`alpha=Z/[lambda^2 x^2 y^2 w0 H1]`.

Substituting `q3=w2/Z` gives `Rscale=0`. Dividing the q2 and q3 equations gives `Rratio=0`. Eliminating `H1` with `Rscale` cancels `lambda` and yields

`alpha=w2(x-1)^2/[x^2y^2w0S1]`.

The exact entropy-stable c-sector identities are

`A_c3=alpha D_U/c3^2`,

`A_c2=alpha D_H/(c2c3)`.

The q-sector algebra gives, on the same strict projective branch,

`A_c3=w1[w2+w1k(y)]/(2Z)`,

`A_c2=w0[1-xy^2w0h(x)/Z]/2`.

Substituting the reconstructed `alpha,c2,c3` and multiplying only by positive strict-domain factors gives `RU=0` and `RH=0`. Conversely, reversing these algebraic steps reconstructs the two score equations, the gamma equation and both c-sector equations. The chosen `gamma_sq=(S+delta)/2` then gives `Psi_3=delta` by the scale-Euler identity. No root is added or lost in the strict domain. QED.

The executed checker verifies these cancellations symbolically with SymPy before any floating calculation.

## 4. Exact third-full theorem II — all-moment outer monotonicity and common tails

The previous NM13-07 theorem made only the two c-sector entropy integrands monotone in the outer Gaussian coordinate. The present compiler needs `S1,S2,H1` as well. All five non-algebraic quantities can in fact be handled by the same endpoint-cell method.

### Theorem NM07-T03-ALL-MOMENT-MONOTONE

Fix strict parameters in Section 3 and write, for outer mean `a`,

`d^2=w1/w0`,

`mu_a(dt) proportional exp[m U_xi(t)] exp[-(t-a)^2/(2d^2)] dt`.

Then as functions of `a` (hence of `v`), each of

`g(a)^2`, `E_{mu_a} U_t^2`, `E_{mu_a} H(T)`, `D_U(a)`, `D_H(a)`

is nonnegative and nondecreasing, where

`H(t)=E_{rho_t}(t+H)_+^2`.

Moreover, with

`a(v)=sqrt(w2/w0)v-1/sqrt(w0)`,

`sigma^2=1+d^2=(w0+w1)/w0`,

`T_sigma(a)=E(a+sigma G)_+^2`,

one has the common pointwise envelopes

`0 <= g(v)^2 <= e2(v) <= (xi-1)^2 T_sigma(a(v))`,

`0 <= h(v) <= T_sigma(a(v))`,

`0 <= D_U(v),D_H(v) <= m(xi-1) T_sigma(a(v))/2`.

Consequently every outer `V` integral in the four residuals admits derivative-free monotone Gaussian-cell lower/upper sums. For the right tail,

`int_R^infinity T_sigma(a(v)) phi(v) dv`

` <= [w2 R phi(R)-2 sqrt(w2) phi(R)+2Q(R)]/w0`.

Multiplying this one common tail by `(xi-1)^2`, `1`, or `m(xi-1)/2` gives tails for `S1/S2`, `H1`, or the two KL terms respectively.

#### Proof

The kernel `exp[-(xi-1)y_+^2/2]` is nonincreasing and log-concave. Gaussian convolution preserves log-concavity, so `U_xi` is nonincreasing and concave:

`U_t<=0`, `U_tt<=0`.

For `a2>a1`, the likelihood ratio of the tilted `T` laws is

`d mu_{a2}/d mu_{a1}(t)=C exp[(a2-a1)t/d^2]`,

which is increasing in `t`. Hence the family is increasing in monotone-likelihood-ratio order.

Because `U_t` is nonincreasing and nonpositive, `U_t^2` is nondecreasing. Thus `E U_t^2` is nondecreasing. Also `g(a)=E U_t` is nonincreasing and nonpositive, so `g(a)^2` is nondecreasing.

For the inner tilt, viewed as a law of `Y=t+H`, the ratio between parameters `t2>t1` is again `C exp[(t2-t1)y]`. Therefore `H(t)=E Y_+^2` is nondecreasing. Applying outer MLR order makes `E_{mu_a}H(T)` nondecreasing.

For the inner entropy `K(t)`, put `b=(xi-1)/2` and `W=Y_+`. The one-dimensional exponential-family calculation gives

`K'(t)=2b^2 Cov_{rho_t}(W^2,W)>=0`.

Thus `D_H(a)=m E_{mu_a}K(T)` is nondecreasing. Finally

`D_U(a)=m E_{mu_a}U(T)-log Z_a`

has the exact derivative

`D_U'(a)=m^2 Cov_{mu_a}(U,U_t)>=0`,

because both `U` and `U_t` are nonincreasing functions of the scalar `t`.

For the envelopes, inner stochastic domination holds because the tilt factor `exp[-b y_+^2]` is decreasing relative to `N(t,1)`. Hence

`H(t)<=T_1(t)`.

Also

`-U_t=(xi-1)E_{rho_t}Y_+`,

so Jensen and the preceding domination give

`U_t^2 <= (xi-1)^2 H(t) <= (xi-1)^2 T_1(t)`.

The outer tilt factor `exp[mU(t)]` is decreasing, so `mu_a` is stochastically dominated by `N(a,d^2)`. Since `T_1(t)` is increasing,

`E_{mu_a}T_1(T) <= E_{N(a,d^2)}T_1(T)=T_sigma(a)`.

This proves the score and `H1` envelopes. The KL envelope follows from the preceding Jensen/stochastic-order c-sector theorem after replacing the original hinge coefficient by `b=(xi-1)/2`.

Finally `T_sigma(a)<=a^2+sigma^2`; inserting `a(v)=sqrt(w2/w0)v-1/sqrt(w0)` and the Gaussian identities for `int phi`, `int v phi`, `int v^2 phi` gives the displayed common right-tail formula. QED.

### Demonstrated certification gain

The four-dimensional residual map has only five non-algebraic outer averages, and **all five now use the same certification architecture**: outward endpoint evaluation on a one-dimensional `U` integral, monotone Gaussian `V` cells, and an explicit common tail. No outer-`V` Taylor derivative or two-dimensional high-order remainder is needed.

A numerical falsification check on `[-6,6]` confirms the predicted monotonicity for all five integrands at the `delta=10^{-3}` waypoint; the only negative finite difference is `-3.67e-16` for `D_U`, at roundoff scale.

## 5. Exact third-full theorem III — covariance-form analytic Jacobian compiler

A Krawczyk proof needs a Jacobian. Finite differences are unacceptable for the directed certificate, but the derivative structure can be reduced to the same moment tower.

For a parameter `theta` among `(w0,w1,x,m)`, define the conditional tilted log-weight derivative

`L_theta = m_theta U + m(U_t T_theta+U_xi xi_theta)`.

For every conditional observable `A`,

`d_theta <A> = <A_theta> + Cov(A,L_theta)`.                  (5.1)

The five required derivatives are therefore

`g_theta=<U_tt T_theta+U_txi xi_theta>+Cov(U_t,L_theta)`,

`(e2)_theta=<2U_t(U_ttT_theta+U_txi xi_theta)>+Cov(U_t^2,L_theta)`,

`h_theta=<H_tT_theta+H_xi xi_theta>+Cov(H,L_theta)`,

`(D_U(v))_theta = m Cov(U,L_theta)`,

`(D_H(v))_theta = m_theta<K> + m[<K_tT_theta+K_xi xi_theta>+Cov(K,L_theta)]`.

The `D_U` line includes the exact partition-function cancellation and remains valid for `theta=m`.

All kernel derivatives use only positive-tail moments through order four. If

`mu_j=E_{rho_t}(t+H)_+^j`,

then

`U_t=-(xi-1)mu_1`, `U_xi=-mu_2/2`,

`U_tt=-(xi-1)[P_rho(Y>0)-(xi-1)(mu_2-mu_1^2)]`,

`H_t=2mu_1-(xi-1)(mu_3-mu_2mu_1)`,

`H_xi=-(mu_4-mu_2^2)/2`,

`U_txi=-H_t/2`,

`K_t=-(xi-1)H_t/2-U_t`,

`K_xi=-(xi-1)H_xi/2=(xi-1)(mu_4-mu_2^2)/4`.

The geometry derivatives are elementary. With

`y=1+m(x-1)w1/(xw0)`,

`S=sqrt(Z)/(xy)`, `lambda=S/(S+delta)`, `xi=1+lambda(x-1)`,

one has

`d log S = (1/2)d log Z-d log x-d log y`,

`d lambda=lambda(1-lambda)d log S`,

`d xi=lambda dx+(x-1)d lambda`,

and

`y_w0=-(y-1)/w0`, `y_w1=(y-1)/w1`,

`y_x=mw1/(w0x^2)`, `y_m=(y-1)/m`.

Writing

`T=aU+bV-c`, `a=sqrt(w1/w0)`, `b=sqrt(w2/w0)`, `c=w0^{-1/2}`,

also gives explicit `T_theta` without numerical differentiation.

The executed checker evaluates this analytic moment Jacobian at the waypoint and compares it only as a **falsification check** against centered finite differences: maximum absolute discrepancy `3.94e-9`, maximum relative discrepancy `1.69e-8`. The theorem itself is the exact covariance differentiation identity above; the finite-difference calculation is not part of the prospective certificate.

## 6. Executed numerical waypoint — CONDITIONAL only

The exact symbolic compiler was followed by Gauss--Hermite/scipy root solves solely to test the new coordinates and formulas. For prescribed gap

`delta=10^{-3}`,

the dimensionless root converges as quadrature order increases:

- GH60: `alpha=12.3164338713702`;
- GH80: `12.3164333240433`;
- GH100: `12.3164333588464`;
- GH120: `12.3164333568795`;
- GH160: `12.3164333569314`;
- GH200: `12.3164333569306`.

At GH200,

`w0=0.0321710159451139`,

`w1=0.370106966023378`,

`x=3.54218891058057`,

`m=0.226621581517544`,

`xi=3.52625448341119`,

with residual infinity norm about `4.44e-16`.

This value is **NUMERICAL_ONLY / CONDITIONAL**. It is not entered into the rigorous source bracket. If the four-dimensional outward inclusion succeeds, however, it would move the upper endpoint from `12.319634446195` to approximately

`12.31643335693`,

a non-microscopic gain of about `0.00320108926`, with `Psi_3=10^{-3}` certified algebraically by the theorem rather than by a tiny numerical objective subtraction.

## 7. Residual obstruction, preserved failures, and next attack

### Residual obstruction

The sole missing proof layer for the robust waypoint is now a directed inclusion of one zero of

`(Rratio,Rscale,RU,RH)`

in a small `(w0,w1,x,m)` box. The exact source comparison implication and the positive objective gap are already algebraically compiled once such a strict zero is certified.

### Preserved failed / superseded routes

1. **Complete-second same-box continuation:** essentially exhausted; the present `5e-12` microstep uses residual slack but further digit shaving is not substantive.
2. **Raw third-full coordinates `(p2,p3,q2,q3,B,...)`:** numerically workable but badly scaled and left hierarchy/domain constraints as separate face obligations.
3. **Earlier third-full outer quadrature:** required two-dimensional derivative/remainder control for the nested c-sector terms. The monotone endpoint-cell theorem first removed this for the two KL terms; the present theorem removes it for `S1,S2,H1` as well.
4. **Finite-difference Jacobian:** useful only for scouting and conditioning checks; it is not acceptable for certification. Section 5 replaces it by exact covariance/moment formulas.

### Next attack

Build one outward one-dimensional endpoint evaluator for the moment tower `mu_0,...,mu_4` and the associated `U,U_t,H,K` quantities. Use it at the endpoints of monotone Gaussian `V` cells, with the common tail theorem above, to enclose all five outer averages and their covariance-form derivatives on a small box around

`(w0,w1,x,m)=(0.0321710159451, 0.3701069660234, 3.542188910581, 0.2266215815175)`.

Then run a weighted Krawczyk / contraction inclusion for the four residuals. Start at `delta=10^{-3}`, where the objective margin is algebraically robust and the candidate source gain is about `0.0032`. Only after that inclusion succeeds should continuation target the stronger companion branch near `12.28722222161`.

## 8. Essential executed artifacts

Created and archived in this run:

- `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_posgap_dimensionless_allmoment.py`
  - creation commit `05569b3d3cdb31172806f7c6b777d8621dd8f31f`;
- `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_posgap_dimensionless_allmoment.out`
  - creation commit `b0567890613e35b0d431eab60c1d4691483945db`.

The output ends

`ALL_EXACT_AND_NUMERICAL_CHECKS_PASS`.

The exact-source and symbolic-algebra sections are separated in the checker from all Gauss--Hermite/scipy lines marked `NUMERICAL_ONLY`.

## 9. ledger_delta

```yaml
ledger_delta:
  parent: T03
  source_model:
    disorder: iid N(0,I_N)
    kappa: -1
    radius: sqrt(N) exactly
  source_threshold:
    before: [6.30297437506, 12.3196344462]
    after: [6.30297437506, 12.319634446195]
    width_before: 6.01666007114
    width_after: 6.016660071135
    rigorous_upper_gain: 5.0e-12
    status: PARTIAL / computer-assisted / pending independent review
  mechanism_gain:
    exact:
      - prescribed-positive-gap dimensionless four-overlap compiler
      - lambda-free density reconstruction
      - all-five-moment outer monotonicity and common explicit tails
      - covariance-form analytic Jacobian using inner moments through order four
    demonstrated_candidate:
      delta: 1.0e-3
      alpha: 12.3164333569306
      status: CONDITIONAL / NUMERICAL_ONLY pending outward 4D inclusion
      prospective_gain_vs_current: 0.0032010892644
  residual_obstruction:
    - outward one-dimensional endpoint moment evaluator on a parameter box
    - weighted four-variable Krawczyk inclusion
  next_attack:
    - certify delta=1e-3 dimensionless root in (w0,w1,x,m)
    - then continue toward the companion 12.28722222161 branch
  artifacts:
    checker_commit: 05569b3d3cdb31172806f7c6b777d8621dd8f31f
    output_commit: b0567890613e35b0d431eab60c1d4691483945db
```
