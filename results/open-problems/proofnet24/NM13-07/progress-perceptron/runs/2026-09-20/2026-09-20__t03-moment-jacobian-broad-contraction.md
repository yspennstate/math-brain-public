Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-07 / T03 — exact tilted-moment Jacobian compiler for the `alpha=12.75` second-full certificate

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03` comparison / feasibility theory  
Status: **PARTIAL / NEW EXACT DERIVATIVE THEOREM / SOURCE BRACKET UNCHANGED**

## 1. Short handoff and source-exact target

The preceding NM13-07 T03 report proved the exact two-scalar reduction of the complete second lifted system. The new companion NM13-03 report then removed the inner conditional Gaussian quadrature by deriving a closed scalar kernel and exhibited a robust numerical `alpha=12.75` Miranda candidate. The newest complementary R14/PROB10 T03 report proved a preconditioned contraction theorem and isolated a finite certification target: rigorous bounds for the Jacobian of

`F(p,B)=(H(p,B), alpha(p,B)-12.75)`

plus a positive objective bound on a small box.

I preserve all of that history and do not restart intake, P0282, or the one-parameter lift.

The source target remains exactly:

- `M=floor(alpha N)`;
- independent `g_a ~ N(0,I_N)`;
- `||sigma||_2=sqrt(N)` exactly;
- `<g_a,sigma> >= -sqrt(N)` for every `a<=M`;
- fixed `alpha` and `N -> infinity`.

Equivalently, for `x=sigma/sqrt(N)`, seek `x in S^{N-1}` with `Gx>=-1`. No radius change, ball relaxation, or replica-only computation is treated as closure.

### Frozen rigorous source metric

Repository-supported rigorous bracket entering this run:

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`,

`W = 6.48139658710`.

The lower endpoint is the rigorous Montanari--Zhong--Zhou linear-programming success threshold at `kappa=-1` after source normalization. The upper endpoint is the retained globally certified older one-parameter/partial-lift Gordon bound.

**Before:** `[6.30297437506, 12.78437096216]`, width `6.48139658710`.

**After:** `[6.30297437506, 12.78437096216]`, width `6.48139658710`.

There is **no rigorous source-bracket movement in this run**. I do not promote the numerical `12.75` stationary candidate without an outward-rounded one-dimensional integral enclosure.

## 2. Primary-source hypothesis and proof-status refresh

The source status was checked only to the extent needed for this argument.

1. **El Alaoui--Sellke, arXiv:2010.15811.** Their model is the exact Gaussian spherical perceptron on radius `sqrt(N)`. For negative margin, the algorithm uses the conjectural FRSB/Parisi structure and outputs a feasible point on radius `sqrt(qbar N)` with `qbar<1`; the paper itself notes the missing step to an exact radius-`sqrt(N)` solution. It therefore does not close T03.
2. **Stojnic, arXiv:2312.16531.** The paper places the negative spherical perceptron in stationarized fully lifted RDT. Theorem 1 / Corollary 1 explicitly require the non-fixed lifting parameters to solve the stationarity system, and the practical-realization section says substantial numerical work is needed. Thus a positive objective at an arbitrary nearby parameter point is not enough for the source implication used here.
3. **Montanari--Zhong--Zhou, arXiv:2110.15824.** This is rigorous and gives upper/lower threshold bounds and the LP threshold, but not equality at `kappa=-1`.
4. **Later physics calculations.** Annesi--Malatesta--Zamponi (arXiv:2410.06717, later SciPost) compute the SAT/UNSAT transition using a full-RSB ansatz; Winer--Herderschee (arXiv:2503.11761 / Phys. Rev. E 2025) use a jammed Parisi ansatz in the UNSAT phase. These are valuable numerical/structural guides but are not substituted for a rigorous full-radius comparison certificate here.

A bounded search through 20 September 2026 did not locate a later rigorous theorem plainly replacing the exact full-radius bracket above. This is bounded negative evidence, not a worldwide openness or priority certificate.

## 3. Consumed exact reduction

Retain the preceding NM13-07 notation

`q=p D^2`,

`gamma_p=(1-pD^2)/(2D(1-p))`,

`c=(1-D^2)/(D(1-p)(1-pD^2))`,

`B=c/(4 gamma)`.

Let

`Y = sqrt(p) z + sqrt(1-p) H - 1`,

`f_{p,B}(z)=E_H exp[-B (Y_+)^2]`,

`u(z)=log f_{p,B}(z)`,

`I=E_Z u(Z)`, `I_B=partial_B I`,

`K=E_Z u_z(Z)^2`.

The preceding report proved, on the interior complete-second-lift branch,

`D^2 = K/[-4 p^2 B^2 I_B]`,

`alpha = -c^2/[4B^2 I_B]`,

`gamma=c/(4B)`,

and stationarity reduces to

`H(p,B)=I-B I_B-4B^2 I_B A_0(p,D)=0`,

where

`A_0(p,D)=T_D/c_D`

and `T_D` is taken with `gamma` held fixed before the stationary substitution. The comparison objective is

`Psi=T(p,D,c/(4B))+cI/(4B^2I_B)`.

At fixed density `12.75`, the only root equations are `H=0` and `alpha=12.75`.

NM13-03's closed-kernel theorem writes, with `mu=sqrt(p)z-1`, `s=sqrt(1-p)`, and `A=1+2Bs^2`,

`J_0=A^{-1/2} exp(-B mu^2/A) Phi(mu/(s sqrt(A)))`,

`f=Phi(-mu/s)+J_0`.

The remaining obstruction was that the Jacobian of `(H,alpha)` and the derivatives of `Psi` were still being obtained numerically/automatically, so a rigorous contraction box appeared to require validated numerical differentiation as well as validated quadrature.

## 4. New theorem — the whole first Jacobian closes with four tilted moments

For `r>=0`, define the **unnormalized positive tilted moments**

`J_r(mu,s,B)=E[ Y_+^r exp(-B Y_+^2) ]`,  `Y~N(mu,s^2)`.

### Lemma NM07-T03-MOMENT-TOWER

For `A=1+2Bs^2`,

`J_1=(mu J_0+s phi(mu/s))/A`,

and for every `r>=2`,

`J_r=(mu/A)J_{r-1}+((r-1)s^2/A)J_{r-2}`.                    (4.1)

Moreover the conditional kernel and all derivatives needed for the first Jacobian satisfy

`f_B=-J_2`,

`f_BB=J_4`,

`f_mu=-2B J_1`,

`f_muB=-2J_1+2B J_3`,

`f_mumu=-2B J_0+4B^2J_2`.                                  (4.2)

Consequently, writing `u=log f`,

`u_B=f_B/f`, `u_mu=f_mu/f`,

`u_BB=f_BB/f-u_B^2`,

`u_muB=f_muB/f-u_mu u_B`,

`u_mumu=f_mumu/f-u_mu^2`.                                   (4.3)

Thus **`J_0,...,J_4` suffice for the complete first derivative of the two-scalar stationary map and of `Psi`**. No finite difference, automatic differentiation, or extra inner Gaussian integral is required.

### Proof

After multiplying the Gaussian density by `exp(-B y^2)` on `y>0`, complete the square. The new quadratic coefficient is `A/s^2`, and the shifted mean is `mu/A`. Integration by parts on `[0,infinity)` gives (4.1); for `r>=2` the boundary term vanishes, while for `r=1` the boundary is exactly `s phi(mu/s)/A`.

Differentiation with respect to `B` under the integral gives `partial_B J_r=-J_{r+2}`, hence `f_B=-J_2` and `f_BB=J_4`. NM13-03's closed formula already gives `f_mu=-2BJ_1`; differentiating it in `B` and using `partial_BJ_1=-J_3` yields `f_muB=-2J_1+2BJ_3`. Finally, Gaussian mean differentiation is differentiation in `y`; for `y_+ exp(-By_+^2)`, this gives `partial_mu J_1=J_0-2BJ_2`, hence `f_mumu=-2BJ_0+4B^2J_2`. The log derivatives are algebraic. Dominated differentiation is immediate on compact interior `(p,B)` boxes. QED.

## 5. Structural identities: entropy, Fisher information, and monotonicity

Normalize the conditional tilted law by

`d nu_B / d nu = exp(-B Y_+^2)/f`,

and put

`m_r(z)=J_r/f=E_{nu_B} Y_+^r`.

Then (4.2) gives the exact identities

`u_B=-m_2`,

`u_mu=-2B m_1`,

`u_BB=Var_{nu_B}(Y_+^2)>=0`.                                (5.1)

It follows that

`I_B=-E m_2 <0`,

`K=4pB^2 E m_1^2`.                                          (5.2)

Therefore the preceding reconstruction has the new probability interpretation

`boxed: D^2 = E[m_1(Z)^2] / (p E[m_2(Z)])`.                  (5.3)

This cancels the apparently delicate `B^2 I_B` quotient in `D^2` and is useful for interval conditioning.

There is also a relative-entropy identity. Pointwise,

`KL(nu_B || nu) = -B m_2 - log f`,

so

`boxed: I-BI_B = -E KL(nu_B||nu) <= 0`.                     (5.4)

Thus the first part of the stationarity residual is not an opaque difference of two quadratures: it is minus an averaged conditional relative entropy.

### Exact OU derivative closure

The Ornstein--Uhlenbeck identity from the predecessor is

`I_p=-K/(2p)`.

Differentiating in `B` gives

`I_Bp=-K_B/(2p)=-E[u_mu u_muB]`,                             (5.5)

because

`K_B=2p E[u_mu u_muB]`.                                     (5.6)

More importantly, the OU evolution gives an exact derivative of `K` with respect to `p`. If `v=u_z`, then

`partial_t u = L u + v^2`, `p=e^{-2t}`,

and Gaussian integration by parts yields

`d/dt E v^2 = -2E v_z^2 -2E v^2 +4E v^2 v_z`.

Since `u_z=sqrt(p)u_mu` and `u_zz=p u_mumu`,

`boxed: K_p = E[u_mu^2] + p E[u_mumu^2-2u_mu^2u_mumu]`.     (5.7)

Now `y -> exp(-B y_+^2)` is log-concave, and Gaussian convolution preserves log-concavity, so `u_mumu<=0`. Hence every term on the right side of (5.7) is nonnegative and the nonconstant branch has

`boxed: K_p>0`.                                              (5.8)

This sign is exact; it is not inferred from a numerical grid.

## 6. Closed analytic Jacobian of the stationary map

Let

`R=D^2=K/(-4p^2B^2I_B)`.

Equations (5.5)--(5.7) give

`R_p/R = K_p/K - 2/p - I_Bp/I_B`,

`R_B/R = K_B/K - 2/B - I_BB/I_B`,

therefore

`D_p=(D/2)(K_p/K-2/p-I_Bp/I_B)`,

`D_B=(D/2)(K_B/K-2/B-I_BB/I_B)`.                            (6.1)

Since `A_0=T_D/c_D` has no explicit `B` dependence after taking `T_D` with `gamma` fixed, direct differentiation gives

`H_p = I_p-BI_Bp`
`      -4B^2[ I_Bp A_0 + I_B(A_{0,p}+A_{0,D}D_p) ]`,       (6.2)

`H_B = -B I_BB -8B I_B A_0 -4B^2 I_BB A_0`
`      -4B^2 I_B A_{0,D}D_B`.                               (6.3)

For `alpha=-c^2/(4B^2I_B)`,

`alpha_p = alpha[ 2(c_p+c_DD_p)/c - I_Bp/I_B ]`,            (6.4)

`alpha_B = alpha[ 2c_DD_B/c -2/B - I_BB/I_B ]`.             (6.5)

Finally, setting `S=cI/(4B^2I_B)` and differentiating the already reduced objective gives similarly explicit formulas for `Psi_p,Psi_B`; the executable artifact evaluates them from the same four moments.

**Consequence:** the entire first-order contraction certificate is now a finite collection of one-dimensional expectations whose pointwise integrands are explicit rational combinations of `Phi`, `phi`, `J_0,...,J_4`. The previous numerical-differentiation layer is removed completely.

## 7. Exact broad-band contraction corollary

The complementary R14 report used the rational preconditioner

`A_* = [[-1601/20, -493/12500],[-60418/25,-5789/2500]]`

and weighted box half-widths

`D_* = diag(1/1000,1/25)`

around

`p_c=645767064689/10^12`,

`B_c=49292292009/10^10`.

Its earlier exact compiler used fairly tight derivative intervals. The new derivative closure allows a useful trade: **much looser whole-box derivative intervals are enough if the center residual is evaluated accurately.**

### Corollary NM07-T03-BROAD-CONTRACTION

Suppose on the whole weighted box one proves only

`H_p in [-7/250,-3/125] = [-0.028,-0.024]`,

`H_B in [3/10000,3/5000] = [0.0003,0.0006]`,

`alpha_p in [24,30]`,

`alpha_B in [-1,-4/5]`.                                     (7.1)

Exact enumeration of all 16 Jacobian vertices gives

`q = sup ||D_*^{-1}(I-A_* DF)D_*||_infinity`

`  <= 23849/25000 = 0.95396 < 1`.                            (7.2)

Hence `1-q >= 1151/25000 = 0.04604`.

If the center point is enclosed only to

`|H(p_c,B_c)| <= 10^{-7}`,

`|alpha(p_c,B_c)-12.75| <= 10^{-5}`,                        (7.3)

then exact rational arithmetic gives

`eta = ||D_*^{-1}A_*F(p_c,B_c)||_infinity`

`    <= 41997/5000000 = 0.0083994 < 0.04604 <= 1-q`.        (7.4)

Therefore the contraction theorem forces a unique true stationary root at `alpha=12.75` inside the box.

With the tighter point residuals `10^{-8}` and `10^{-6}`, respectively, the exact bound improves to

`eta <= 41997/50000000 = 0.00083994`.

### Proof

This is finite exact arithmetic. Evaluate `D_*^{-1}(I-A_*J)D_*` at the 16 vertices of the interval Jacobian box (7.1) and take the largest row-sum norm; the maximum is exactly `23849/25000`. The two residual bounds follow by multiplying the componentwise center-error box by `D_*^{-1}A_*`. Banach's contraction theorem is then exactly the R14 deterministic compiler. QED.

The point is not that `q=0.95396` is numerically impressive; it is that the derivative enclosure can now be **very coarse**. The remaining rigorous numerical work no longer needs to reproduce the sampled derivatives to four or five significant digits.

## 8. Executed sanity check after the mathematics

I created and executed

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_moment_jacobian_compiler.py`

creation commit `19a9e162f2ced8c61be4c906ddd012276cca5835`,

with actual output archived as

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_moment_jacobian_compiler.out`

creation commit `3d515124eb1fa50be6b32d123572b308dd0819c4`.

The **exact** portion checks the broad contraction arithmetic and ends with the exact fractions in (7.2)--(7.4). The quadrature portion is explicitly a **NUMERICAL SANITY CHECK**, not the missing rigorous enclosure.

At the inherited `alpha=12.75` scout point it reports

`H = 2.91e-16`,

`alpha = 12.749999999999961`,

`Psi = 0.015200993467164914`,

`D = 0.6601219023283817`,

and the new analytic derivatives

`H_p = -0.0257128403301171`,

`H_B = 0.000437906185349334`,

`alpha_p = 26.8356843806070`,

`alpha_B = -0.888882259891337`,

`Psi_p = 0.946635525536169`,

`Psi_B = -0.0313555455973423`.

The intermediate exact-identity scalars are numerically

`I_BB = 0.001987251921929727`,

`I_Bp = -0.015001050815129107`,

`K_p = 1.045956633137645`,

`K_B = 0.019374369104271427`.

The analytic Jacobian agrees with centered finite-difference falsification checks to the expected discretization scale.

On a `41 x 41` grid of the full R14 weighted box, **using the analytic formulas rather than finite differences**, the observed ranges are

`H_p      in [-0.02609011055,-0.02533620577]`,

`H_B      in [ 0.000427699435, 0.000448037895]`,

`alpha_p  in [26.66684471,27.00817520]`,

`alpha_B  in [-0.9062899883,-0.8719493061]`,

`Psi_p    in [0.9424341428,0.9509302352]`,

`Psi_B    in [-0.0319295618,-0.0307959004]`,

`I_BB     in [0.00195478907,0.00202044551]`,

`I_Bp     in [-0.01520744515,-0.01479815913]`,

`K_p      in [1.032199547,1.059855593]`,

`K_B      in [0.0190827313,0.0196713493]`,

`D        in [0.6586626494,0.6615897788]`.

Every sampled Jacobian value lies comfortably inside the deliberately broad exact target box (7.1). The identity (5.3) is independently checked at the center to `5.6e-17` numerical discrepancy. Output terminates `ALL_CHECKS_PASS`.

Again: a grid and Gauss--Hermite agreement are not an interval proof. They are used here only to falsify the new formulas and to verify that the broadened enclosure target has substantial slack.

## 9. Source-level movement versus demonstrated mechanism gain

### Source metric

Before:

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

After:

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

**Movement: none.**

The review-pending source candidate remains

`alpha_U=12.75`,

which would give width `6.44702562494` and improve the rigorous upper endpoint by `0.03437096216` if the final enclosure succeeds.

### Demonstrated mechanism gain

Before this run, the finite certificate still depended on numerical/automatic differentiation of scalar Gaussian quantities, and the R14 contraction theorem was formulated with relatively tight derivative boxes.

After this run:

1. `J_0,...,J_4` generate every kernel derivative needed for the first stationary Jacobian by the exact recurrence (4.1)--(4.3).
2. `D^2` has the exact tilted-moment ratio (5.3), `I-BI_B` is minus a conditional KL divergence, and `K_p>0` follows exactly from OU evolution plus log-concavity.
3. The whole `(H,alpha,Psi)` first derivative is analytic and one-dimensional; finite differences are eliminated.
4. Exact rational contraction arithmetic shows that the Jacobian only needs the broad bands (7.1), provided the center scalar integrals are enclosed accurately.

This is a genuine reduction in the mathematical/certification obligation directly connected to the `12.75` source endpoint, not a renamed auxiliary constant.

## 10. Failed / excluded route and residual obstruction

I also reconsidered a purely geometric dual-feasibility translation. With `y=-x`, the source constraints are equivalent to asking whether the polar of the Gaussian polytope `conv(g_1,...,g_M)` contains a unit vector; UNSAT is equivalent (when the origin is interior) to `conv(g_i)` containing the Euclidean unit ball. This is an exact reformulation. However the elementary facet first-moment route inherited from the earlier R14 history remains far too weak in the proportional regime and does not compete with `12.784...`; I did not spend the run manufacturing a new version of that failed bound.

The remaining obstruction is now precise:

> Rigorously enclose the one-dimensional expectations generated by `J_0,...,J_4` on the small `(p,B)` box sufficiently to prove the deliberately broad derivative intervals (7.1), center residual bounds such as (7.3), and a positive `Psi` enclosure.

No conceptual stationarity derivative remains. The finite proof can now use outward-rounded composite/Taylor quadrature on explicit scalar functions, with the old `|z|>9` Gaussian tails treated separately. If these broad bounds pass, the exact contraction theorem gives a true stationary point at `alpha=12.75`; the source theorem then turns positive `Psi` into the desired strict rigorous upper-endpoint improvement.

## 11. Next attack

Do **not** introduce another variational ansatz next. The next NM13-07 T03 run should execute the finite enclosure itself:

- use the recurrence (4.1) to evaluate `J_0,...,J_4` with directed interval/Taylor bounds on `|z|<=9`;
- propagate those intervals through (4.3), (5.5)--(6.5) on a modest `(p,B)` subdivision;
- use explicit Gaussian tail inequalities outside `|z|<=9` for `I,I_B,K,I_BB,I_Bp,K_p,K_B`;
- check the broad Jacobian target (7.1), a center residual target no weaker than (7.3), branch interiority, and a uniform `Psi>0` bound;
- only then change `alpha_U` from `12.78437096216` to `12.75`.

If the interval dependency problem prevents (7.1), the materially different fallback is to exploit the exact KL/Fisher representation (5.3)--(5.4) to bound `H` and `D` directly rather than enclosing their quotient formulas componentwise.

No peer file, root ledger, schedule, access control, email, Drive object, public resource, or posted result was modified.

```yaml
ledger_delta:
  worker: NM13-07
  parent: T03
  target: "negative spherical Gaussian perceptron, kappa=-1, iid Gaussian constraints, exact radius sqrt(N)"
  status: "PARTIAL / NEW EXACT MOMENT-JACOBIAN THEOREM / SOURCE BRACKET UNCHANGED"
  source_metric: "rigorous threshold bracket width alpha_U-alpha_L"
  certified_before:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  certified_after:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
    movement: "none; 12.75 still requires rigorous scalar integral enclosure"
  review_pending_candidate:
    alpha_U: "12.75"
    candidate_width: "6.44702562494"
    possible_upper_improvement: "0.03437096216"
  mechanism_gain:
    theorem: "NM07-T03-MOMENT-TOWER"
    identities:
      - "J_r recurrence closes f_B,f_BB,f_mu,f_muB,f_mumu with J_0..J_4"
      - "D^2=E[m1^2]/(p E[m2])"
      - "I-BI_B=-E KL(nu_B||nu)"
      - "K_p=E[u_mu^2]+pE[u_mumu^2-2u_mu^2u_mumu]>0"
    finite_compiler: "broad Jacobian bands imply exact contraction q<=23849/25000"
    residual_tradeoff: "with |H_c|<=1e-7 and |alpha_c-12.75|<=1e-5, eta<=41997/5000000<1-q"
  executed_artifacts:
    code: "proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_moment_jacobian_compiler.py"
    output: "proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_moment_jacobian_compiler.out"
    output_marker: "ALL_CHECKS_PASS"
    exact_part: "broad contraction and residual arithmetic"
    numerical_part: "GH260 analytic-derivative/grid sanity check; not a rigorous enclosure"
  residual_obstruction: "outward-rounded 1D Gaussian/Taylor enclosure for broad Jacobian bands, center residual, Psi>0, and interior branch"
  next_attack: "execute interval/Taylor enclosure using J_0..J_4; if dependency blows up, switch to direct KL/Fisher bounds"
  coordination:
    NM13-03: "consumed closed conditional kernel; this run supplies exact derivative/moment closure"
    R14_PROB10_03: "consumed preconditioned contraction theorem; this run broadens its admissible Jacobian box exactly"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
```
