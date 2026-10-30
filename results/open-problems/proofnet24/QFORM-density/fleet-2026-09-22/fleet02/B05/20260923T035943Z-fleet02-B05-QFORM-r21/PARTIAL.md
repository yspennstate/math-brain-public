SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B05, 2026-09-23T03:59:43Z.
attacking: a rough-input interval form of the ruled one-sheet theorem, then the exact reciprocal-shear geometry of the two-sheet side.

# Early substantive checkpoint

Status: `ESSENTIAL_STEP_APPLIED` in progress; full QFORM remains open.

## Source pins actually used

- newest required source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`. The ruled one-sheet calculation and Theorem F are used below.
- exact-rank-three scalar-pivot dependency: `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.
- designated partner actually read: fleet03/B05 r20, `yspennstate/math-open-problems@929322485c85c8a08367589be2b8e2e73839c65f`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260923T014000Z-fleet03-B05-QFORM-r20/REPORT.md`.

## 1. Rough-input ruled interval theorem

Let `X=(X_1,...,X_n)` have independent coordinate densities bounded by one. Let `R` be `n x 3` with `R^T R=I_3`, write `Y=R^T X`, and let `rho` be its three-dimensional density. For `lambda_1,lambda_2,mu >=1`, put

`q(y)=lambda_1 y_1^2+lambda_2 y_2^2-mu y_3^2`.

Then for every Borel interval `J subset [0,infinity)`, including intervals meeting zero,

`P(q(Y) in J) <= C_+(lambda_1,lambda_2,mu) |J| <= pi sqrt(2) |J|`,

where

`C_+ = (lambda_1 lambda_2 mu)^(-1/2) integral_0^{2pi} [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2) dtheta`.

This is an interval statement for arbitrary rough input laws; it does not assume that the output already has a pointwise density or that `rho` is continuous.

Proof. Put `D=diag(sqrt(lambda_1),sqrt(lambda_2),sqrt(mu))`, `z=Dy`, `e_theta=(cos theta,sin theta,0)` and `e_theta^perp=(-sin theta,cos theta,0)`. For `s>0`,

`z=sqrt(s)e_theta+t(e_theta^perp+e_3)`

parametrizes the one-sheet level `z_1^2+z_2^2-z_3^2=s`. In coordinates `(s,theta,t)` its absolute Jacobian is exactly `1/2`: in the moving basis `(e_theta,e_theta^perp,e_3)` the derivative columns are

`(1/(2sqrt(s)),0,0)`, `(-t,sqrt(s),0)`, `(0,1,1)`.

Hence Tonelli/change of variables gives, first for intervals bounded away from zero,

`P(q(Y) in J)=(2 sqrt(lambda_1lambda_2mu))^(-1) integral_J ds integral dtheta integral_R rho(D^(-1)[sqrt(s)e_theta+t(e_theta^perp+e_3)]) dt`.

For fixed `theta`, the line direction in the original `y` variables is

`d_theta=D^(-1)(e_theta^perp+e_3)`,

so `|d_theta|^2=sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu`. The line integral in `t` is `|d_theta|^(-1)` times a line integral with respect to arclength. The latter is a value of a two-dimensional orthogonal marginal of the product measure. The sharp product-projection theorem used in the newest source gives that marginal density at most `2`. Thus the line integral is at most `2/|d_theta|` for almost every transverse point, enough after the `(s,theta)` integration. This yields the displayed `C_+`.

Finally

`lambda_1lambda_2mu |d_theta|^2=lambda_2mu sin^2(theta)+lambda_1mu cos^2(theta)+lambda_1lambda_2 >=2`,

so the integrand defining `C_+` is pointwise at most `1/sqrt(2)` and `C_+<=pi sqrt(2)`. The cone `q=0` has three-dimensional Lebesgue measure zero, hence no output atom at zero; monotone convergence includes intervals meeting zero. QED.

This upgrades the newest source's pointwise ruled calculation to the exact rough-input small-interval statement needed by the conjecture on the whole one-sheet side.

## 2. Exact two-sheet reciprocal-shear coordinates

For the negative level write `q(y)=-u`, `u>0`. For each sheet `sigma in {+1,-1}`, define

`n_{theta,sigma}=e_theta+sigma e_3`, `m_{theta,sigma}=-e_theta+sigma e_3`,

and, for `T>sqrt(u)/2`,

`y_sigma(u,theta,T)=D^(-1)[T n_{theta,sigma}+(u/(4T))m_{theta,sigma}]`.

Then `q(y_sigma)=-u` exactly, since the positive radial coordinate is `T-u/(4T)` and the signed third coordinate is `sigma(T+u/(4T))`. The map `(u,theta,T)` parametrizes the two sheets up to null sets, and its absolute Jacobian is

`[2 sqrt(lambda_1lambda_2mu)]^(-1) [1-u/(4T^2)]`.

Equivalently, for every interval `J subset (0,infinity)`,

`P(q(Y) in -J)` equals

`(2 sqrt(lambda_1lambda_2mu))^(-1) sum_sigma integral dtheta integral_{T>0} integral_{u in J, u<4T^2} rho(y_sigma(u,theta,T)) [1-u/(4T^2)] du dT`.

Thus for a.e. `u>0` the negative-side density is the angularly averaged reciprocal-shear transform

`p_q(-u)=(2 sqrt(lambda_1lambda_2mu))^(-1) sum_sigma integral_0^{2pi} integral_{sqrt(u)/2}^infinity rho(y_sigma(u,theta,T))[1-u/(4T^2)] dT dtheta`.

Derivation of the Jacobian: start from the standard hyperbolic coordinates `z=sqrt(u)sinh(v)e_theta+sigma sqrt(u)cosh(v)e_3`, whose volume Jacobian is `sqrt(u)sinh(v)/2`; set `T=sqrt(u)e^v/2`. Then `dv=dT/T` and `sqrt(u)sinh(v)=T-u/(4T)`, giving the stated factor.

This formula isolates the obstruction without taking an unrestricted fiber supremum. At `u=0` the reciprocal displacement vanishes and the traces become null rays. For `u>0`, however, the trace is the genuinely curved map

`T n + (u/(4T))m`,

so a straight-line X-ray bound does not control it. This matches the live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE`: generic line-marginal information alone is insufficient on the two-sheet side. The still-usable structure is that `rho` is a projection of the original product measure.

## 3. Immediate source-bound reduction of the two-sheet debt

Let `r_i` denote row `i` of `R`, `c_i=||r_i||^2` and `a_i=A_ii=r_i^T Lambda r_i`, where `Lambda=diag(lambda_1,lambda_2,-mu)`.

- If every `c_i<=1/2`, Theorem F in the required newest source applies with `I` equal to all coordinates and gives `||p_Q||_infinity<=12`. Hence the entire reciprocal-shear transform above, not merely the one-sheet side, is already paid in the diffuse-leverage regime.
- Otherwise there is a heavy physical row `c_i>1/2`. If for some heavy row `|a_i|>=delta`, the exact-rank-three scalar-pivot theorem at commit `e542...` gives `||p_Q||_infinity <=128(c_i |a_i| |det Lambda|)^(-1/4) <=128(2/delta)^(1/4)`.
- Consequently, after fixing for example `delta=1/16`, any exact-rank-three two-sheet survivor must have every heavy row near null: `c_i>1/2` implies `|a_i|<1/16`. There are at most five such rows because `sum_i c_i=3`. Moreover each such row has a strong physical cross arm:

`||A_{i,-i}||_2^2=(A^2)_ii-a_i^2=r_i^T Lambda^2 r_i-a_i^2 >=c_i-a_i^2 >1/2-1/256=127/256`.

So the surviving branch has cross-arm norm strictly larger than `sqrt(127)/16`, despite the small physical pivot. The missing factor is therefore not absence of linear cross mass; it is how to spend that strong arm jointly with the two remaining curvatures while retaining original-coordinate product structure.

The designated partner fleet03/B05 r20 is compatible exactly here: whenever the remaining product coordinates can be routed into its three disjoint coefficient resources with `||r|| ||c|| ||D||_HS>=eta` and the smoothing side is affine, its proved theorem gives `||p_Q||_infinity <=K_3 eta^(-1/3)`. Therefore an unpaid near-null heavy-row state must either fail that three-resource extraction or contain the partner's explicit residual obstruction: same-side quadratic curvature on the smoothing banks. This is a real narrowing of the two-sheet debt, not a new assumption on the full theorem.

## First unpaid implication

`QFORM-TWOSHEET-RECIPROCAL-SHEAR-PRODUCT-TRACE-v1`: prove a dimension-free bound on the angularly averaged reciprocal-shear transform above for product-projection densities in the finite-heavy-row near-null regime, or convert the strong cross arm plus remaining rank-three curvature into the partner's three-arm coarea packet while allowing same-side quadratic curvature. A proof may average over `theta`; it must not replace the curved traces by unrestricted fiber suprema.
