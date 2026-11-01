SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-23T09:08:22Z.
attacking: a new unpaid dense rotated stress family with the same spectrum and range leverage as the preceding Hadamard core, but a larger exact global peak; compare it to the diffuse sharp mechanism using fleet02/B17.

# QFORM B17 — a 45-degree signature rotation raises the exact dense finite peak

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T090822Z-fleet01-B17-QFORM-auto11`  
Status: **NEW SUPPORTING SHARP-WITNESS THEOREM; FULL QFORM OPEN / NOT PROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`. Full-target continuity remains separately open, although the explicit family below has a continuous density.

## 1. An exact one-parameter rotated stress family

Fix the tetrahedral/Hadamard Parseval frame

\[
R=\frac12\begin{pmatrix}
1&1&1\\
1&-1&1\\
1&1&-1\\
1&-1&-1
\end{pmatrix},\qquad R^TR=I_3.
\]

For `alpha in [0,pi/4]`, put

\[
n_\alpha=(\cos\alpha,\sin\alpha,0)^T,
\qquad
B_\alpha=I_3-2n_\alpha n_\alpha^T,
\qquad
A_\alpha=RB_\alpha R^T.
\tag{1.1}
\]

Every `B_alpha` is an orthogonal reflection with spectrum `{1,1,-1}`. Therefore every finite physical matrix `A_alpha` has

\[
\boxed{\operatorname{spec}_{\ne0}(A_\alpha)=\{1,1,-1\}.}
\tag{1.2}
\]

All members also have the same range projection `RR^T`, hence exactly the same physical row leverages. Let `X_1,...,X_4` be independent `Unif[-1/2,1/2]`; every source density has cap exactly one. Put `Y=R^T X`. Integrating the physical cube along the one-dimensional null fibre gives the exact three-dimensional marginal

\[
\boxed{\rho(y)=2(1-M_1(y)-M_2(y))_+,}
\tag{1.3}
\]

where `M_1>=M_2>=M_3` are the ordered absolute coordinate magnitudes. This retains the original product provenance; no arbitrary-joint density bound is used.

Choose `m_alpha=(-sin alpha,cos alpha,0)` and `e_3=(0,0,1)`. On the cone `y^T B_alpha y=0`, write

\[
y=r\{\sigma n_\alpha+\cos\theta\,m_\alpha+\sin\theta\,e_3\},
\quad r\ge0,\quad \sigma\in\{\pm1\}.
\]

Let

\[
h_{\alpha,\sigma}(\theta)
=M_1(w_{\alpha,\sigma}(\theta))+M_2(w_{\alpha,\sigma}(\theta)),
\]

for the bracketed unit cone ray `w`. Since the Lorentz coarea element on either nappe is exactly `(1/2)dr dtheta`, (1.3) gives the exact cone-tip formula

\[
\boxed{
p_{A_\alpha}(0)
=\frac12\sum_{\sigma=\pm1}\int_0^{2\pi}
\frac{d\theta}{h_{\alpha,\sigma}(\theta)}.}
\tag{1.4}
\]

Thus (1.1)-(1.4) are an exact finite rotated stress family, not a Gaussian relaxation.

At `alpha=0`, (1.4) reduces to the preceding axis-Hadamard value

\[
p_{A_0}(0)=8(\sqrt2-1)=3.313708498984\ldots.
\tag{1.5}
\]

The new endpoint `alpha=pi/4` has a larger exact value and admits complete global-output control.

## 2. The 45-degree matrix is genuinely dense and exact-target

At `alpha=pi/4`,

\[
B:=B_{\pi/4}=
\begin{pmatrix}
0&-1&0\\
-1&0&0\\
0&0&1
\end{pmatrix},
\]

and

\[
\boxed{
A=RBR^T=\frac14\begin{pmatrix}
-1&1&-3&-1\\
1&3&-1&1\\
-3&-1&-1&1\\
-1&1&1&3
\end{pmatrix}.}
\tag{2.1}
\]

Every physical entry is nonzero, while `spec(A)={1,1,-1,0}`. In spectral coordinates

\[
Q=Y^TBY=Y_3^2-2Y_1Y_2.
\tag{2.2}
\]

Set

\[
u=(Y_1+Y_2)/\sqrt2,
\qquad v=(Y_1-Y_2)/\sqrt2,
\qquad z=Y_3.
\]

Then

\[
Q=v^2+z^2-u^2.
\tag{2.3}
\]

For the remainder of the proof write the density in these Lorentz coordinates as

\[
\widetilde\rho(u,v,z)
:=\rho\!\left(\frac{u+v}{\sqrt2},\frac{u-v}{\sqrt2},z\right).
\tag{2.4}
\]

This is a genuinely shared-coordinate physical stress even though (2.3) is Lorentz-diagonal after the exact three-dimensional marginal has already been computed from the original product cube.

## 3. Exact cone-tip value

On `Q=0`, write

\[
u=\sigma r,\qquad v=r\cos\theta,\qquad z=r\sin\theta.
\]

The absolute `Y`-coordinate multiset is

\[
r\left\{
\frac{1+|\cos\theta|}{\sqrt2},
\frac{1-|\cos\theta|}{\sqrt2},
|\sin\theta|
\right\}.
\tag{3.1}
\]

Moreover

\[
\sin^2\theta-\frac{(1-|\cos\theta|)^2}{2}
=\frac{(1-|\cos\theta|)(1+3|\cos\theta|)}2\ge0,
\]

so the two largest magnitudes in (3.1) have sum

\[
h(\theta)=\frac{1+|\cos\theta|}{\sqrt2}+|\sin\theta|.
\tag{3.2}
\]

Applying (1.4), quadrant symmetry, and `t=tan(theta/2)` gives

\[
\begin{aligned}
p_Q(0)
&=\int_0^{2\pi}\frac{d\theta}{h(\theta)}\\
&=4\int_0^{\pi/2}\frac{d\theta}{(1+\cos\theta)/\sqrt2+\sin\theta}\\
&=4\int_0^1\frac{dt}{t+1/\sqrt2}\\
&=\boxed{4\log(1+\sqrt2)}
=3.525494348078\ldots .
\end{aligned}
\tag{3.3}
\]

This is already strictly larger than the diagonal sharp constant `pi`. Indeed

\[
\log(1+\sqrt2)=\operatorname{arsinh}(1)
=\int_0^1(1+x^2)^{-1/2}dx
>\int_0^1(1-x^2/2)dx=5/6,
\]

so `4 log(1+sqrt2)>10/3>pi`. It remains below the diffuse obstruction because `arsinh(1)<1`, hence

\[
4\log(1+\sqrt2)<4<3\sqrt2.
\tag{3.4}
\]

The new orientation also strictly beats the axis-Hadamard orientation. For every `t>0`,

\[
\log(1+t)-\frac{2t}{2+t}>0
\]

because its derivative is `t^2/[(1+t)(2+t)^2]`. At `t=sqrt2`, `2t/(2+t)=2(sqrt2-1)`, and therefore

\[
4\log(1+\sqrt2)>8(\sqrt2-1).
\tag{3.5}
\]

Thus the same spectrum, same physical source cube, and same range projection can have different exact peaks solely because the signature is oriented differently inside the spectral range.

## 4. Two-sheet side: exact monotonicity away from zero

Let `tau>=0` and impose `Q=-tau`. For fixed `(v,z)`, set

\[
r_\tau=\sqrt{v^2+z^2+\tau}.
\]

Integrating the delta function in `u` over the two roots `u=+-r_tau` yields

\[
p_Q(-\tau)=\int_{\mathbb R^2}
\frac{\widetilde\rho(r_\tau,v,z)}{r_\tau}\,dv\,dz,
\tag{4.1}
\]

because the two signs of `u` give the same value of `widetilde rho`. Since `r_tau>=|v|`, the first two absolute `Y` magnitudes are

\[
A(r)=\frac{r+|v|}{\sqrt2},
\qquad B(r)=\frac{r-|v|}{\sqrt2},
\]

with `A>=B`. Therefore the top-two sum entering (1.3) is

\[
H_-(r)=A(r)+\max\{B(r),|z|\},
\tag{4.2}
\]

which is nondecreasing in `r`. Consequently

\[
\widetilde\rho(r,v,z)=2(1-H_-(r))_+
\]

is nonincreasing in `r`, and so is `widetilde rho(r,v,z)/r`. Because `r_tau` increases with `tau`, (4.1) proves

\[
\boxed{p_Q(-\tau)\le p_Q(0)\qquad(\tau\ge0).}
\tag{4.3}
\]

The apparent `1/r` singularity at `tau=0` is integrable in the `(v,z)` plane.

## 5. One-sheet side: exact monotonicity away from zero

Let `tau>=0` and write

\[
v=r\cos\theta,\qquad z=r\sin\theta,
\qquad r=\sqrt{u^2+\tau}.
\]

Integrating `delta(r^2-u^2-tau)` in the radial variable and using the symmetry `u<->-u` gives

\[
p_Q(\tau)=\int_0^\infty\int_0^{2\pi}
\widetilde\rho\bigl(u,r\cos\theta,r\sin\theta\bigr)\,d\theta\,du.
\tag{5.1}
\]

Fix `u>=0`, put `c=|cos theta|`, `s=|sin theta|`, and let `r>=u`. The sorted pair of absolute magnitudes coming from `(Y_1,Y_2)` is

\[
A(r)=\frac{u+rc}{\sqrt2},
\qquad B(r)=\frac{|u-rc|}{\sqrt2},
\qquad A\ge B,
\]

while the third magnitude is `C(r)=rs`. The top-two sum is

\[
H_+(r)=A(r)+\max\{B(r),C(r)\}
=\max\{\sqrt2\max(u,rc),\ u/\sqrt2+r(c/\sqrt2+s)\}.
\tag{5.2}
\]

Both entries of the final maximum are nondecreasing in `r`. Hence `H_+(r)` is nondecreasing, the exact product-provenance density `widetilde rho=2(1-H_+)_+` is nonincreasing, and `r=sqrt(u^2+tau)` increases with `tau`. Thus (5.1) gives

\[
\boxed{p_Q(\tau)\le p_Q(0)\qquad(\tau\ge0).}
\tag{5.3}
\]

Combining (3.3), (4.3), and (5.3),

\[
\boxed{
\|p_Q\|_\infty=p_Q(0)=4\log(1+\sqrt2)=3.525494348078\ldots .}
\tag{5.4}
\]

The integral formulas also give a continuous representative: for positive levels use the bounded compact-support integrand in (5.1); for negative levels a neighbourhood of zero is dominated by a constant multiple of `(v^2+z^2)^(-1/2)`, which is locally integrable in two dimensions.

## 6. Structural witness: spectrum and leverage do not determine the sharp finite peak

The old axis member `A_0` and the new `A_{pi/4}` have identical nonzero spectrum `{1,1,-1}`, identical range projection `RR^T`, identical row leverages `(RR^T)_{ii}=3/4`, and the identical physical input law. Yet

\[
\|p_{Q_0}\|_\infty=8(\sqrt2-1)
<4\log(1+\sqrt2)
=\|p_{Q_{\pi/4}}\|_\infty.
\tag{6.1}
\]

Therefore any proposed *sharp* proof invariant that retains only the eigenvalue multiset and range-projection leverage data is insufficient in the high-leverage finite regime. The orientation of the positive/negative signature inside the physical product projection matters quantitatively.

This does not conflict with diffuse Gaussianisation: the orientation dependence is a finite/high-leverage effect.

## 7. Designated fleet02/B17 result applied to an actual inequality

The current completed partner theorem is

`math-open-problems@fefb4cf4f0af17c810341152311c3822c78d5b7f`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260923T082513Z-fleet02-B17-QFORM-r12/UNIFORM_EXTENSION.md`.

It gives one deterministic `Delta_m->0` such that, for every symmetric `3x3` core `C_m` with `s_3(C_m)>=1`, every normalized three-bank interval frame `P_m`, and arbitrary independent translations of all physical unit intervals,

\[
\|p_{X^TP_mC_mP_m^TX}\|_\infty\le3\sqrt2+\Delta_m.
\tag{7.1}
\]

Apply this theorem to the **actual core** `C_m=B` from (2.1), for which `s_3(B)=1`. For centered banks the Gaussian limit is rotationally invariant and has the same `{1,1,-1}` spectrum, so the partner theorem's sharpness statement gives

\[
\lim_{m\to\infty}\|p_{X^TP_mBP_m^TX}\|_\infty=3\sqrt2.
\tag{7.2}
\]

Equations (5.4) and (7.2) therefore give the concrete comparison

\[
\boxed{
4\log(1+\sqrt2)
<3\sqrt2
=\lim_{m\to\infty}\|p_{X^TP_mBP_m^TX}\|_\infty.}
\tag{7.3}
\]

Thus a 45-degree signature rotation makes the all-heavy four-coordinate core more dangerous than the axis orientation, but it is still strictly dominated by genuine diffuse Gaussianisation. The partner theorem additionally rules out arbitrary independent translations of the unit-smoothed diffuse comparator as an asymptotic escape mechanism.

## 8. Newest-Claude theorem applied to this same matrix

The current newest-Claude package, `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, proves its Theorem C for exact rank-three signature `(+,+,-)`: for arbitrary product inputs and `s>=0`,

\[
p_Q(s)\le\pi\sqrt2.
\tag{8.1}
\]

Applying (8.1) to the explicit matrix (2.1) pays its entire one-sheet side without any special cube algebra. The new exact formula (5.3) then sharpens that applied inequality for this stress family to

\[
\boxed{
\sup_{s\ge0}p_Q(s)=4\log(1+\sqrt2)<4<\pi\sqrt2.}
\tag{8.2}
\]

The genuinely new work is therefore the exact two-sheet control and the orientation-sensitive global peak.

## 9. Correction discipline and full-target gap

No refuted interface is used: there is no independence after spectral rotation, no arbitrary-joint coarea theorem, no worst-fibre density moment, no uniform pointwise stationary-phase decay, no fixed fragment-count extremality, and no assertion of a universally good physical minor. The three-dimensional density (1.3) is computed exactly from the original product cube before the Lorentz change of variables.

The certified universal lower obstruction remains

\[
C_{\rm univ}\ge3\sqrt2,
\]

from the existing exact finite diffuse sequence. The new finite exact witness is weaker as a lower bound but stronger as a structural test:

\[
C_{\rm univ}\ge4\log(1+\sqrt2)>\pi,
\]

and it demonstrates quantitatively that signature orientation survives at high leverage even when spectrum and range leverage are fixed.

The unrestricted QFORM theorem is still open. A witness exceeding `3sqrt(2)`, if one exists, must leave the two endpoint mechanisms paid here and in the partner theorem; plausible surviving locations remain asymmetric off-center fragmentation, higher-dimensional nonperiodic shared-coordinate cores, shrinking smoothing scales, and full-spectrum coupled tails. No claim is made that `3sqrt(2)` is the unrestricted sharp constant.
