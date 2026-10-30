SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-23T16:30:00Z.
attacking: uniform strict cone-tip gap for the one-heavy N3 family via an exact cap-one/Gaussian Laplace comparison.

# QFORM B17 — uniform strict gap for the entire one-heavy N3 cone-tip family

Run: `20260923T163000Z-fleet03-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: sharp constant and witnesses  
Status: **NEW SUPPORTING ANALYTIC THEOREM; FULL QFORM OPEN / NOT PROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Result and scope

The preceding B17 run reduced the one-heavy/shared-diffuse no-pivot family to the exact cone-tip extremal value
\[
C(a)=\sup_{0\le f\le1,\ \int f=1}p_{Q_a}(0),\qquad 0<a\le1,
\]
where
\[
Q_a=-aX^2+2\sqrt{1-a^2}\,XB+aB^2+C^2,
\]
`X` has an arbitrary cap-one density and `B,C` are independent `N(0,1/12)`, independent of `X`.  It also proved that the unique optimizer is `X~Unif[-1/2,1/2]`.  The unpaid implication was a uniform analytic comparison of `C(a)` with the known lower obstruction `3sqrt(2)`.

This report closes that implication.  Put
\[
R_1=\sqrt{\frac\pi3}\,\operatorname{erf}\sqrt{\frac32}.
\]
Then for every `0<a<=1`,
\[
\boxed{
C(a)\le {3\sqrt2\over2}(1+R_1)<3\sqrt2.
}
\tag{1.1}
\]
Numerically, only as a diagnostic,
\[
{3\sqrt2\over2}(1+R_1)=4.11137318108064699\ldots,
\quad
3\sqrt2=4.24264068711928515\ldots,
\]
so the proved uniform gap is at least `0.1312675060...` throughout the genuinely coupled one-heavy family.  No compact-support, connected-support, moment, symmetry or log-concavity assumption is imposed on the heavy law; the cap-one optimizer theorem already pays arbitrary fragmentation.

The null endpoint `a=0`, namely `2XB+C^2`, was proved separately in the earlier B17 report `6e6b31c077cd37e28c1edd78ed7ab9520b1aa2d0`, where its exact cap-one optimum was shown strictly below `3sqrt(2)` as well.

This is a cone-tip theorem for this stress architecture, not the full QFORM theorem and not a global-in-output-level bound.

## 2. Exact kernel representation

Let `v=1/12`, `d=sqrt(1-a^2)`, and
\[
F_a(\theta)=\frac{(\cos\theta-d)^2}{a^2}+\frac{\sin^2\theta}{a}.
\tag{2.1}
\]
The previous run's exact coarea calculation gives the conditional zero-density kernel
\[
K_a(x)=\frac{3}{\pi\sqrt a}\int_0^{2\pi}e^{-6F_a(\theta)x^2}\,d\theta.
\tag{2.2}
\]
`K_a` is even and strictly decreasing in `|x|`, hence bathtub rearrangement over all probability densities `0<=f<=1` gives the centered unit interval as the exact optimizer.  Therefore, with
\[
L(s):=\int_{-1/2}^{1/2}e^{-6s x^2}\,dx,
\tag{2.3}
\]
we have
\[
\boxed{
C(a)=\frac{3}{\pi\sqrt a}\int_0^{2\pi}L(F_a(\theta))\,d\theta.
}
\tag{2.4}
\]

## 3. A strict Laplace comparison with monotone ratio

Define
\[
R(s):=\sqrt{1+s}\,L(s),\qquad s\ge0.
\tag{3.1}
\]
Then `R(0)=1` and `R` is strictly decreasing on `(0,infinity)`.

Indeed put
\[
M(s)=\int_{-1/2}^{1/2}x^2e^{-6sx^2}\,dx.
\]
Integration by parts gives
\[
L(s)-12sM(s)=e^{-3s/2}.
\tag{3.2}
\]
Also
\[
\begin{aligned}
L(s)
&=e^{-3s/2}\int_{-1/2}^{1/2}
   e^{6s(1/4-x^2)}dx\\
&>e^{-3s/2}\int_{-1/2}^{1/2}
  \left[1+6s(1/4-x^2)\right]dx\\
&=(1+s)e^{-3s/2},
\end{aligned}
\tag{3.3}
\]
for every `s>0`.  Using `L'(s)=-6M(s)` and (3.2),
\[
\frac{d}{ds}\log R(s)
=\frac1{2(1+s)}-\frac{L(s)-e^{-3s/2}}{2sL(s)}<0
\tag{3.4}
\]
by (3.3).

Consequently
\[
\boxed{L(s)<\frac1{\sqrt{1+s}}\quad(s>0),}
\tag{3.5}
\]
which is exactly the matched-variance comparison between the centered unit interval and `N(0,1/12)` for the Laplace transform of the square.  More importantly, the ratio in (3.5) is itself strictly decreasing.

## 4. Exact Gaussian normalization for every coupling parameter

Put
\[
\alpha=\sqrt{1+a},\qquad \beta=\sqrt{1-a}.
\]
A direct algebraic identity gives
\[
\boxed{
a^2(1+F_a(\theta))
=(\alpha-\beta\cos\theta)^2.
}
\tag{4.1}
\]
For `0<a<1` the bracket is positive, hence
\[
\frac1{\sqrt{1+F_a(\theta)}}
=\frac{a}{\alpha-\beta\cos\theta}.
\tag{4.2}
\]
The classical elementary integral
\[
\int_0^{2\pi}\frac{d\theta}{\alpha-\beta\cos\theta}
=\frac{2\pi}{\sqrt{\alpha^2-\beta^2}}
=\frac{2\pi}{\sqrt{2a}}
\tag{4.3}
\]
therefore yields
\[
\boxed{
\frac3{\pi\sqrt a}\int_0^{2\pi}
\frac{d\theta}{\sqrt{1+F_a(\theta)}}=3\sqrt2.
}
\tag{4.4}
\]
At `a=1`, `F_1(theta)=1`, and (4.4) remains true directly.

Thus the matched isotropic Gaussian model has the same cone-tip value `3sqrt(2)` for every physical rotation parameter `a`, exactly as rotational invariance predicts, but here the identity is proved directly in the physical-frame kernel.

## 5. Half of the Gaussian comparison weight lies where F>=1

Normalize the Gaussian comparison weight by
\[
d\nu_a(\theta)
=\frac{(1+F_a(\theta))^{-1/2}
      d\theta}{\pi\sqrt{2a}}.
\tag{5.1}
\]
Equation (4.4) shows that `nu_a` is a probability measure.  From (2.4),
\[
\boxed{
\frac{C(a)}{3\sqrt2}
=\int R(F_a(\theta))\,d\nu_a(\theta).
}
\tag{5.2}
\]

We now prove
\[
\boxed{\nu_a\{F_a\ge1\}\ge\frac12.}
\tag{5.3}
\]
For `a=1` this is immediate because `F_1 identically 1`.  Assume `0<a<1`.  By (4.1), `F_a<1` iff
\[
\cos\theta>c_a:=\frac{\alpha-a\sqrt2}{\beta}.
\tag{5.4}
\]
Let `theta_0=arccos(c_a)` and
\[
\kappa=\sqrt{\frac{\alpha+\beta}{\alpha-\beta}}.
\]
Using (4.2) and the tangent-half-angle antiderivative,
\[
\nu_a\{F_a<1\}
=\frac2\pi\arctan\left(\kappa\tan\frac{\theta_0}{2}\right).
\tag{5.5}
\]
Now
\[
c_a-\frac\beta\alpha
=\frac{a(2-\sqrt2\,\alpha)}{\alpha\beta}\ge0
\tag{5.6}
\]
because `alpha=sqrt(1+a)<=sqrt2`.  The inequality `c_a>=beta/alpha` is equivalent to
\[
\kappa\tan(\theta_0/2)\le1.
\]
Equation (5.5) then gives `nu_a{F_a<1}<=1/2`, proving (5.3).

## 6. Uniform strict gap below 3sqrt(2)

Since `R` is decreasing, `R(s)<=R(1)` on `s>=1`, while `R(s)<=1` everywhere.  Combining (5.2) and (5.3),
\[
\frac{C(a)}{3\sqrt2}
\le \frac12+\frac12R(1).
\tag{6.1}
\]
Finally
\[
R(1)=\sqrt2\int_{-1/2}^{1/2}e^{-6x^2}dx
=\sqrt{\frac\pi3}\operatorname{erf}\sqrt{\frac32}<1
\tag{6.2}
\]
by (3.5).  This proves (1.1).

This is stronger than the previous endpoint-only estimate: the whole continuously rotated one-heavy/shared-diffuse cone-tip architecture has a uniform analytic separation from the current sharp lower obstruction.

## 7. Exact finite source-valid provenance and designated-partner transfer

For each fixed `0<a<=1`, use the exact finite Parseval frame from the preceding B17 report: one physical row `r`, `m` copies of `b/sqrt(m)`, and `m` copies of `c/sqrt(m)`, where in spectral coordinates
\[
r^T J r=-a,\quad b^TJb=a,\quad r^TJb=\sqrt{1-a^2},\quad c^TJc=1,
\]
with `J=diag(1,1,-1)`.  The resulting physical matrix
\[
A_{a,m}=R_m J R_m^T
\]
has exact nonzero spectrum `{1,1,-1}` for every finite `m`, and all physical inputs are independent `Unif[-1/2,1/2]`.  The exact form is
\[
Q_{a,m}=-aX^2+2\sqrt{1-a^2}\,XB_m+aB_m^2+C_m^2.
\tag{7.1}
\]

The designated partner `fleet04/B17` proved at

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260922T211900Z-fleet04-B17-QFORM-r3/REPORT.md`

the weighted local Edgeworth expansion
\[
g_m(y)=\gamma_\sigma(y)
\left[1-\frac1{20m}H_4(y/\sigma)\right]
+O(m^{-2})(1+|y|)^{-8},\qquad \sigma^2=1/12,
\tag{7.2}
\]
and an exact rotated finite witness establishing
\[
C_*\ge3\sqrt2
\tag{7.3}
\]
for every possible universal constant `C_*`.

Apply (7.2) to the two actual diffuse-bank densities in the coarea formula for (7.1).  For every fixed `a>0`, the Gaussian cone kernel and the polynomially weighted remainders are integrable, so termwise integration gives
\[
\boxed{
p_{Q_{a,m}}(0)=C(a)+O_a(m^{-1}).}
\tag{7.4}
\]
Hence the partner theorem is applied to an actual inequality:
\[
\boxed{
\limsup_{m\to\infty}p_{Q_{a,m}}(0)
=C(a)
\le {3\sqrt2\over2}(1+R_1)
<3\sqrt2\le C_*.
}
\tag{7.5}
\]
In particular, for every fixed `a>0`, all sufficiently large finite exact cap-one members of this rotated family have cone-tip density strictly below the partner's sharp lower obstruction.  No post-rotation independence is asserted; independence remains in the original physical coordinates.

## 8. Verification and nonclaims

`check.py` verifies the perfect-square identity (4.1), the Gaussian normalization (4.4), the monotonicity margin from (3.3), and diagnostic values of `C(a)`.  It prints

`PASS QFORM_ONE_HEAVY_UNIFORM_GAP`.

The diagnostic uniform ceiling is
\[
4.11137318108064699019\ldots,
\]
and the diagnostic sampled `C(a)` values rise from about `3.6226` at `a=.01` to `3.9801` at `a=1`, all below the proved uniform ceiling.  These decimals are checks only; the theorem is analytic.

What is **not** proved here:

- no global-in-level bound `sup_s p_{Q_a}(s)` is claimed for this family;
- no statement is made for two or more macroscopic shared physical rows;
- no uniform finite-`m` remainder in `a` is claimed in (7.4);
- arbitrary added spectrum is not controlled;
- the full QFORM bounded-density conjecture remains OPEN;
- the full-target continuous-density conclusion remains OPEN.

The next nonredundant B17 mechanism is therefore either an off-tip global peak for a one-heavy family, or a genuinely two-heavy/multiple-shared-row construction whose surviving non-Gaussian component cannot be represented as an independent shift of the minimum-variance Gaussian core.

## Source pins and corrections consumed


The live correction inbox was refreshed before publication.  This proof does not use the refuted uniform pointwise van-der-Corput decay, post-rotation independence, arbitrary-joint rank-three coarea, positive conditional-density moments, naive fiber-supremum integration, or one-heavy same-square absorption.  It uses only the exact one-heavy kernel proved in the preceding B17 report, elementary one-dimensional Laplace comparison, and the completed fleet04/B17 weighted local Edgeworth theorem in its stated source-valid scope.
