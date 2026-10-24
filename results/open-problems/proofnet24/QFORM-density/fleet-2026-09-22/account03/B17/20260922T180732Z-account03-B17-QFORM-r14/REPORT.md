# account03/B17 — exact six-variable symmetric rotation and a one-coordinate fragmentation barrier

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T180732Z-account03-B17-QFORM-r14`  
**Assignment:** sharp constant and witnesses  
**Status:** `SUBSTANTIVE_SUPPORTING_LEMMAS / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and what is new in this run

The full target remains: for every dimension, every product law with one-dimensional densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a dimension-independent essential density bound for `X^T A X`, or give a counterexample.

This run does **not** claim the full theorem. It changes mechanism from the preceding fixed-frame Edgeworth analysis to exact finite-dimensional coarea plus a source-valid fragmentation optimization.

Two new statements are proved.

1. An exact genuinely rotated six-variable unit-interval witness with spectrum `{1,1,-1,0,0,0}` has

   `p_Q(0) = 4.06307061680603726012548442259...`.

   This is larger than the preceding exact six-variable cross witness `4.02959666899...`, though still below the already known asymptotic lower bound `3 sqrt(2)=4.24264068711...`. Thus it is a stronger **finite-dimensional exact benchmark**, not a new global lower bound.

2. For the preceding cross witness, if five input laws remain centered unit intervals and the sixth is allowed to be **any** probability density bounded by one (hence arbitrary fragmentation and translation), the centered unit interval is the unique a.e. maximizer of the density at zero. Thus a one-coordinate fragmentation attack cannot improve that witness; any improvement from that geometry must move at least two coordinate laws jointly or change the spectral orientation.

The second statement directly applies the completed account04/B14 extreme-product/bathtub mechanism to an explicit target-level density functional.

## 2. Compatible partner mathematics actually applied

The designated `account04/B17` had no completed QFORM artifact discoverable at the coherent prepublication check. I therefore did not fabricate one. I used the compatible completed account04/B14 result instead:

- repository `yspennstate/math-open-problems`;
- commit `8fcc9ba5db68dfd4cd5daeb181a39666ceeda322`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T114319Z-b14-qform-extreme-reduction-r1/REPORT.md`.

Its one-coordinate bathtub lemma and exact extreme-product reduction say that cap-one product-law interval probabilities may be optimized using indicator densities of measure-one sets; compact finite unions of intervals suffice without loss. In Section 5 below, its bathtub step is applied to the explicit kernel `W(x)` and gives a genuine inequality, not merely a citation.

## 3. Exact symmetric rotated six-variable witness

Let `X_1,...,X_6` be iid uniform on `[-1/2,1/2]`, and set

`Y_j=(X_{2j-1}+X_{2j})/sqrt(2)`,  `j=1,2,3`.

The `Y_j` are independent with triangular density

`g(y)=sqrt(2) (1-sqrt(2)|y|)_+`.

Put

`v=(1,1,1)/sqrt(3)`,  `B=I_3-2 v v^T = I_3-(2/3) 11^T`,

and

`Q=Y^T B Y`.

If `P` is the `6 x 3` pair-sum isometry whose columns are the normalized indicators of the three coordinate pairs, then the physical matrix is

`A=P B P^T`.

Since `P^T P=I_3` and `B` has characteristic polynomial

`(lambda-1)^2(lambda+1)`,

the physical matrix has exact spectrum

`{1,1,-1,0,0,0}`.

Thus this is a source-valid, genuinely rotated exact target witness.

## 4. Exact coarea evaluation at zero

Write

`q(y)=|y|^2-2(v.y)^2`.

In spherical coordinates `y=r u`, the zero cone on `S^2` is the union of the two circles

`u_s(theta)=(s v+w(theta))/sqrt(2)`, `s=+/-1`,

where `w(theta)` is a unit vector in `v^perp`. On the zero cone,

`|grad_{S^2} q|=2`,

and each circle has line element `dtheta/sqrt(2)`. Since

`prod_i g(r u_i)=2 sqrt(2) prod_i (1-sqrt(2) r |u_i|)_+`,

the coarea constants cancel exactly and

`p_Q(0)=sum_{s=+/-1} int_0^{2pi} J(a_s(theta)) dtheta`,

where

`a_{s,i}(theta)=|s v_i+w_i(theta)|`

and, if `M=max_i a_i`,

`J(a)=int_0^{1/M} prod_i(1-a_i r) dr`

`     =1/M-S1/(2M^2)+S2/(3M^3)-S3/(4M^4)`.

For the symmetric vector `v`, choose

`w_i(theta)=sqrt(2/3) cos(theta+2pi(i-1)/3)`.

Homogeneity of `J`, sign-sheet symmetry, permutation periodicity, and reflection reduce the whole integral to

`p_Q(0)=12 sqrt(3) int_0^{pi/3} J(b(theta)) dtheta`,

with

`b_i(theta)=|1+sqrt(2) cos(theta+2pi(i-1)/3)|`.

On `0<=theta<=pi/3`, the maximum component is always the first. The only sign change is the third component at `theta=pi/12`. Therefore there are exactly two elementary cells. With `t=tan(theta/2)` the breakpoints are

`t_*=tan(pi/24)=-2-sqrt(3)+sqrt(2)+sqrt(6)`,

`t_2=tan(pi/6)=1/sqrt(3)`.

The two rational tangent-substitution integrands have the exact partial fractions reproduced by `check_exact.py`. Elementary integration gives

`p_Q(0) = -165/4 + 12 sqrt(3) + 15 sqrt(2)`

`         + 22 sqrt(3) log((sqrt(6)+3 sqrt(2))/6)`

`         + sqrt(3) log((1+sqrt(2)-1/sqrt(3))/(1+sqrt(2)+1/sqrt(3)))`.

Numerically,

`p_Q(0)=4.06307061680603726012548442259349995675...`.

Consequently every universal QFORM constant must in particular satisfy

`C >= 4.0630706168060372601...`

already in dimension six. This does **not** improve the stronger known asymptotic requirement `C>=3 sqrt(2)`, whose gap here is

`3 sqrt(2)-p_Q(0)=0.17957007031324788627958175003559...`.

No claim is made here that the symmetric spectral orientation globally maximizes all six-variable rotations.

## 5. Exact one-coordinate fragmentation barrier for the cross witness

Now consider the previous cross orientation

`Q_x = Y_3^2-2 Y_1 Y_2`

with `X_2,...,X_6` centered unit intervals, but allow `X_1` to have an arbitrary probability density `0<=f_1<=1`.

In unscaled pair sums put

`A=X_1+X_2`, `B=X_3+X_4`, `C=X_5+X_6`.

Then

`Q_x=C^2/2-A B`.

The variables `B,C` have triangular density `tau(s)=(1-|s|)_+` on `[-1,1]`. For fixed `|A|=q>0`, the density at zero is

`H(q)=int_0^{min(1/2,q)} (sqrt(2) w^{-1/2}-2) q^{-1}(1-w/q) dw`.

The integral is elementary:

`H(q)=(4 sqrt(2)/3) q^{-1/2}-1`, for `0<q<=1/2`,

`H(q)=q^{-1}-(12 q^2)^{-1}`, for `q>=1/2`.

The two formulas agree at `q=1/2`, where `H(1/2)=5/3`. Moreover `H` is strictly decreasing on `(0,infinity)`: on the first cell this is immediate, and on the second

`H'(q)=(1/6-q)/q^3<0` for `q>=1/2`.

Averaging over the fixed centered `X_2` gives the one-coordinate kernel

`W(x)=int_{-1/2}^{1/2} H(|x+u|) du`.

It is even, finite, and strictly decreasing in `|x|`. Indeed, for `x>0`, differentiating the sliding integral away from its harmless breakpoints gives the difference of two values of the strictly decreasing `H`, with the farther endpoint always smaller; continuity fills the breakpoints.

Tonelli/approximation by small output intervals therefore gives

`p_{Q_x}(0)=int_R f_1(x) W(x) dx`.

Apply the account04/B14 bathtub lemma (after harmless rescaling of the bounded kernel `W`). Among all `0<=f_1<=1` with total mass one, the unique a.e. maximizer is

`f_1=1_{[-1/2,1/2]}`.

Thus arbitrary one-coordinate fragmentation, distant support pieces, or translation cannot raise this peak when the other five laws are fixed centered intervals.

At that maximizer,

`p_{Q_x}(0)=2 int_0^1 (1-q) H(q) dq`

`            =91/36+(13/6) log 2`

`            =4.02959666899099261484844737427...`.

This is a global coordinatewise optimization, not a first-order calculation.

## 6. Implication for sharp-witness search

The current sharp-witness picture is therefore more constrained:

- the symmetric six-variable spectral orientation gives a new exact finite peak `4.0630706168...`, improving the earlier exact six-variable rotated benchmark;
- the known diffuse/asymptotic witness still supplies the stronger universal lower bound `3 sqrt(2)`;
- on the cross six-variable geometry, changing a single coordinate law to an arbitrary cap-one fragmented law cannot improve its zero peak at all.

Hence a source-valid attempt to exceed `3 sqrt(2)` should not spend another run on a one-coordinate fragment swap around the cross witness. A genuinely different candidate must at least use a coordinated multi-coordinate support deformation, a different finite spectral orientation, or a growing/multiscale shared-coordinate architecture.

## 7. Regularity scope and unresolved target implication

For the two explicit finite uniform witnesses in this report, the coarea representations give finite point densities at zero; the first witness has a continuous density at zero by the explicit compact piecewise-polynomial integral. The one-coordinate barrier proves the stated value/optimization at zero, not a universal `L^infinity` bound over all output levels.

No full-target continuity statement is proved. No universal upper bound is proved. The arbitrary dimension/sign/rotation/additional-eigenvalue QFORM conjecture remains **OPEN**.

The next B17 step should search coordinated multi-coordinate extreme-product deformations of the symmetric orientation, or derive a global orientation/support barrier strong enough to explain why the `3 sqrt(2)` diffuse limit remains dominant.

## 8. Reproducibility

`check_exact.py` symbolically verifies:

- the exact target spectrum;
- the two tangent-cell partial fraction identities;
- the radical/log closed form for the symmetric six-variable peak;
- the cross-witness piecewise kernel and exact centered peak.

The saved checker output is `CHECK_OUTPUT.txt`.
