Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-03 / R14 — preconditioned stationarity certificate for the complete second lift

Status: **THEOREM PROVED / APPLICATION HYPOTHESES NOT YET RIGOROUSLY ENCLOSED / SOURCE ENDPOINT UNCHANGED**.

This artifact is the mathematics-first record for the bounded R14 iteration. It is complementary to the exact two-scalar reconstruction in `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-full2-two-scalar-reduction.md` and the closed Gaussian kernel in `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-closed-kernel-miranda-alpha12p75.md`. It does not overwrite either companion track.

The frozen source problem remains the Gaussian spherical perceptron at `kappa=-1`, radius `sqrt(N)`, with current rigorous bracket

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

width `6.48139658710`.

No number below is promoted into that bracket unless every analytical and numerical enclosure hypothesis is proved.

## 1. Exact two-scalar object being certified

Use the companion notation. For `(p,B)` in the complete second-lift interior branch let

`F(p,B) = ( H(p,B), alpha(p,B)-12.75 )`,

where `H` and `alpha` are reconstructed from the exact second-full stationarity system. The companion reduction proves that `F(p,B)=0` is equivalent to complete second-full stationarity at density `alpha=12.75`, provided the reconstructed point stays in the stated interior domain. The companion closed-kernel lemma turns all Gaussian quantities entering `F` into one-dimensional expectations.

The previous route proposed a Poincare--Miranda certificate on a relatively large axis-aligned rectangle and therefore needed continuous sign control on four full faces. The new route below instead preconditions the two equations by a fixed approximate inverse Jacobian. Its continuum obligation is a **single interval Jacobian enclosure on a much smaller weighted box**, plus a loose center residual bound.

## 2. General weighted contraction theorem

### Theorem R14-T03-PRECONDITIONED-NEWTON

Let `X=R^2`, let `x_c in X`, let `D=diag(r_1,r_2)` with `r_i>0`, and define the closed weighted box

`Q={x: ||D^{-1}(x-x_c)||_infty <= 1}`.

Let `F:Q->R^2` be continuously differentiable, and let `A` be an invertible fixed `2 x 2` matrix. Suppose

`q := sup_{x in Q} || D^{-1}(I-A DF(x))D ||_infty < 1`

and

`eta := ||D^{-1} A F(x_c)||_infty <= 1-q`.

Then `F` has a unique zero `x_*` in `Q`.

#### Proof

Define `T(x)=x-AF(x)`. For `x,y in Q`, the segment joining them is contained in `Q`, and the fundamental theorem of calculus gives

`T(x)-T(y) = int_0^1 [I-A DF(y+t(x-y))](x-y) dt`.

Therefore

`||D^{-1}(T(x)-T(y))||_infty <= q ||D^{-1}(x-y)||_infty`.

Also, for `x in Q`,

`||D^{-1}(T(x)-x_c)||_infty`
`<= ||D^{-1}(T(x_c)-x_c)||_infty + q||D^{-1}(x-x_c)||_infty`
`<= eta+q <=1`.

Hence `T` maps `Q` into itself and is a contraction in the weighted sup norm. Banach's fixed-point theorem gives a unique `x_* in Q` with `T(x_*)=x_*`. Since `A` is invertible, this is equivalent to `F(x_*)=0`. QED.

This theorem is purely deterministic. It does not rely on a mesh, floating-point root, or probabilistic approximation.

## 3. Exact rational compiler specialized to alpha=12.75

Take the rational center and weighted radii

`p_c = 645767064689/10^12`,

`B_c = 49292292009/10^10`,

`r_p = 1/1000`, `r_B = 1/25`,

and choose the fixed rational matrix

`A = [[-1601/20, -493/12500],[-60418/25,-5789/2500]]`.

Write

`J = DF = [[H_p,H_B],[alpha_p,alpha_B]]`.

The following four interval inclusions are a sufficient Jacobian certificate on the entire weighted box:

`H_p in [-131/5000,-63/2500]`,

`H_B in [21/50000,23/50000]`,

`alpha_p in [53/2,136/5]`,

`alpha_B in [-23/25,-43/50]`.

Because every entry of `D^{-1}(I-AJ)D` is affine in the four independent interval variables and the induced infinity norm is convex, its maximum over this rectangular Jacobian enclosure occurs at a vertex. Exact enumeration of the 16 vertices gives

`q <= 215437/1250000 = 0.1723496`.

The worst vertex is

`(H_p,H_B,alpha_p,alpha_B)=(-63/2500,23/50000,136/5,-43/50)`,

where

`D^{-1}(I-AJ)D`
`= [[13877/250000,14523/125000],`
`   [65093/1250000,18793/156250]]`,

and the larger absolute row sum is exactly `215437/1250000`.

Thus

`1-q >= 1034563/1250000 = 0.8276504`.

If, in addition, rigorous center enclosures establish only the deliberately loose bounds

`|H(p_c,B_c)| <= 1/200000 = 5e-6`,

`|alpha(p_c,B_c)-12.75| <= 1/1000`,

then exact rational arithmetic gives

`eta <= max(43969/100000,17999/50000)`
`= 43969/100000 = 0.43969`
`< 1034563/1250000 <= 1-q`.

Therefore these six interval statements alone certify a unique exact stationary point at `alpha=12.75` in the weighted box.

### Why this is a substantive reduction

The center tolerances are intentionally coarse, and the permitted Jacobian intervals are materially wider than the numerical variation observed by the companion finite-mesh scout. Unlike the prior face-sign approach, one does not need to preserve a `~3e-5` sign on an entire face. It is enough to prove four broad derivative intervals and two loose center residual bounds using outward-rounded one-dimensional Gaussian evaluation.

## 4. Comparison-value positivity compiler

The source-moving application also needs strict positivity of the complete second-lift comparison value `Psi` at the stationary point.

### Lemma R14-T03-PSI-BOX

On the same box, assume

`Psi(p_c,B_c) >= 0.014`,

`|Psi_p| <= 2`,

`|Psi_B| <= 0.1`.

Then every point `(p,B)` in the box satisfies

`Psi(p,B) >= 0.014 - 2(0.001) - 0.1(0.04) = 0.008 >0`.

#### Proof

Apply the fundamental theorem of calculus along the line segment from the center and use the coordinate derivative bounds. QED.

Consequently, after a rigorous enclosure of the Jacobian/center/Psi hypotheses above, the companion exact reconstruction plus the stationarized full-lifting feasibility implication would turn `alpha=12.75` into a rigorous UNSAT endpoint. The resulting bracket would be

`6.30297437506 <= alpha_c(-1) <= 12.75`,

with width `6.44702562494`, an improvement of `0.03437096216`.

**This endpoint is conditional at present. The current rigorous endpoint remains `12.78437096216`.**

## 5. Negation test: stationarity cannot simply be discarded

A tempting shortcut is to evaluate the lifted comparison functional at an explicit nearby parameter point with positive value and bypass root certification. I checked this route against the source formulation rather than assuming it was valid.

Stojnic's stationarized full-lifting statements explicitly impose stationarity of the non-fixed lifting parameters before invoking the strong random-duality/feasibility conclusion. Therefore a positive value at an arbitrary nonstationary numerical point is not, by the cited theorem, a certified source upper bound. The true-zero obligation in `F=(H,alpha-12.75)` is not bookkeeping; it is part of the source theorem's hypotheses for this route.

This kills the easiest possible shortcut and justifies spending the finite certification effort on the actual stationary system.

## 6. Third attack: cancel more Hermite overlap modes on the SAT side

The preceding R14 run enlarged the MZZ-type weight to an exponential quadratic tilt. To test whether its positive-overlap failure was merely family-specific, consider instead the nonnegative squared-polynomial family

`w_{a,b}(x)=(1+a x+b x^2)^2 1{x>=-1}`.

For `G~N(0,1)` define Hermite moments

`m_j=E[w(G) He_j(G)]`.

Imposing `m_1=m_2=0` annihilates the first two nonconstant terms in Mehler's expansion

`E[w(G_1)w(G_2)] = sum_{j>=0} m_j^2 q^j/j!`.

This is a genuinely different deformation from the previous exponential-quadratic family: it directly kills two low overlap modes while preserving nonnegativity.

For a correlated pair with `Y|X=x ~ N(qx,1-q^2)`, the inner expectation is reducible exactly to truncated Gaussian moments through degree four. If `t=(-1-qx)/sqrt(1-q^2)` and

`R_0(t)=Phi(-t)`, `R_1(t)=phi(t)`,

`R_j(t)=t^{j-1}phi(t)+(j-1)R_{j-2}(t)` for `j>=2`,

then each `E[Y^k 1{Y>=-1}|X=x]` is an explicit linear combination of `R_0,...,R_k`. Thus the full two-replica kernel for `w_{a,b}` is reduced exactly to one outer Gaussian integral. No overlap ansatz is introduced.

The accompanying numerical scout finds two moment-canceling branches but, on both, the global positive-overlap obstruction appears far below the already rigorous LP lower endpoint. These numerical values are diagnostics only; they are not rigorous bracket endpoints. The conclusion for route selection is that killing additional local Hermite modes does not by itself address the global-overlap obstruction.

## 7. What remains to make 12.75 rigorous

The remaining finite obligation is now sharply delimited:

1. Using the proved closed formulas for `f,f_B,f_mu`, outward-round the one-dimensional Gaussian expectations and enough derivatives to certify the four Jacobian intervals on the weighted box.
2. Rigorously certify the two center residual inequalities.
3. Rigorously certify the three `Psi` inequalities.
4. Recheck that every reconstructed point in the box remains in the interior branch assumed by the exact second-full reduction.
5. Only then invoke the source's stationarized feasibility implication and update the rigorous endpoint.

The theorem in Sections 2--4 is complete; items 1--4 are the computational-analysis hypotheses still missing. A finite mesh or ordinary double-precision quadrature does not discharge them.

No scheduler, public resource, email, Drive object, permission, workflow, shared claim, or peer-track file is changed by this artifact.
