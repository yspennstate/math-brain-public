SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-23T13:00:31Z.
attacking: close the off-tip/two-sheet gap for the canonical dense Householder cube witness by proving its global density maximum occurs exactly at the cone tip.

# QFORM B17 — exact global maximum for the dense Householder cube witness

Run: `20260923T130031Z-fleet03-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **SUPPORTING ANALYTIC WITNESS THEOREM; FULL QFORM OPEN / NOT PROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact source-valid rotated family

Let
\[
e=(1,1,1)/\sqrt3,\qquad A=I-2ee^T
=\frac13\begin{pmatrix}1&-2&-2\\-2&1&-2\\-2&-2&1\end{pmatrix},
\]
and let `X=(X_1,X_2,X_3)` have independent `Unif[-1/2,1/2]` coordinates. Then `A^2=I`, `Ae=-e`, and `A|_{e^\perp}=I`, so the exact spectrum is
\[
\operatorname{spec}(A)=\{1,1,-1\}.
\]
This is an exact finite-dimensional instance of the owner target, with a genuinely dense physical matrix and no post-rotation independence claim.

The completed designated-partner report `fleet04/B17` proved the exact cone-tip value
\[
\boxed{p_Q(0)=6\sqrt3\,\operatorname{artanh}\!\left(\frac{\sqrt2-1}{\sqrt3}\right)}
=2.5343552034856026468\ldots,
\tag{1}
\]
for `Q=X^TAX`. Partner source:

`yspennstate/math-open-problems@a227d5dcd268ee481d19d1bd6fcf041f32183806`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260923T081528Z-fleet04-B17-QFORM-r4/REPORT.md`.

That report explicitly left the global off-tip/two-sheet maximum open. The present run closes exactly that gap.

## 2. Cylindrical density formula

Choose an orthonormal basis `u,v` of `e^\perp` and write
\[
x=w e+r d(\theta),\qquad d(\theta)=u\cos\theta+v\sin\theta,
\]
with `r>=0`. The Euclidean volume element is `r\,dr\,d\theta\,dw`, while
\[
Q(x)=r^2-w^2.
\]
For any real output level `s`, put
\[
r_s(w)=\sqrt{w^2+s}
\]
when `w^2+s>=0`, and let
\[
\Theta_s(w)=\left|\{\theta\in[0,2\pi):we+r_s(w)d(\theta)\in[-1/2,1/2]^3\}\right|.
\]
Integrating the delta constraint in `r` gives the canonical density formula
\[
\boxed{p_Q(s)=\frac12\int_{w^2+s\ge0}\Theta_s(w)\,dw.}
\tag{2}
\]
For every cube point, `|w|=|x_1+x_2+x_3|/\sqrt3<=\sqrt3/2`. Thus all integrals below are over a fixed compact `w` interval.

## 3. The ruled side `s>0` is pointwise dominated by the cone

Fix `w`. The planar slice
\[
K_w=\{y\in e^\perp:we+y\in[-1/2,1/2]^3\}
\]
is convex and contains the origin whenever it is nonempty, because the slice center `we` itself lies in the cube for `|w|<=\sqrt3/2`.

For `s>0`,
\[
r_s(w)=\sqrt{w^2+s}\ge |w|=r_0(w).
\]
If the point `we+r_s(w)d(\theta)` lies in the cube, then convexity of `K_w` implies the point on the same radial segment at the smaller radius `|w|` also lies in the cube. Therefore
\[
\Theta_s(w)\le\Theta_0(w)
\]
for every `w`. Integrating (2),
\[
\boxed{p_Q(s)\le p_Q(0)\qquad(s\ge0).}
\tag{3}
\]
This is sharper for this exact witness than the previously used ball-envelope bound.

## 4. Exact two-sheet comparison for `s=-a<0`

Let `a>0` and first take `w>0`. On the level `Q=-a`,
\[
r=\sqrt{w^2-a}<w.
\]
For any unit `d\in e^\perp`, each coordinate satisfies `d_i>=-\sqrt{2/3}`. Hence
\[
(we+rd)_i\ge \frac{w}{\sqrt3}-r\sqrt{\frac23}
>\frac{w}{\sqrt3}(1-\sqrt2).
\]
Any cube point has `w<=\sqrt3/2`; consequently the right side is at least `(1-\sqrt2)/2>-1/2`. Thus on the positive `w` sheet the three lower cube faces are automatically inactive. Only the upper faces matter.

Set
\[
m(\theta)=\max_i d_i(\theta),\qquad b(\theta)=\sqrt3\,m(\theta)>0,
\qquad c_0=\frac{\sqrt3}{2}.
\]
The cube condition on the positive sheet is exactly
\[
w+b(\theta)\sqrt{w^2-a}\le c_0.
\tag{4}
\]
For fixed `theta`, the left side is strictly increasing for `w>=\sqrt a`. When `0<a<c_0^2=3/4`, there is a unique endpoint `W_a(\theta)>\sqrt a` satisfying equality in (4). By central symmetry the negative `w` sheet contributes the same amount, and (2) becomes
\[
\boxed{p_Q(-a)=\int_0^{2\pi}\bigl(W_a(\theta)-\sqrt a\bigr)\,d\theta.}
\tag{5}
\]
At `a=0`, the endpoint is explicit:
\[
W_0(\theta)=\frac{c_0}{1+b(\theta)},
\tag{6}
\]
and hence
\[
p_Q(0)=\int_0^{2\pi}W_0(\theta)\,d\theta.
\tag{7}
\]

Now let `r_0=\sqrt a` and `L=W_0(\theta)`. Evaluate the left side of (4) at `w=r_0+L`:
\[
\begin{aligned}
F_a(r_0+L)
&=r_0+L+b\sqrt{(r_0+L)^2-r_0^2}\\
&=r_0+L+b\sqrt{L^2+2r_0L}\\
&>r_0+(1+b)L=r_0+c_0>c_0.
\end{aligned}
\]
Since `F_a` is strictly increasing and `F_a(W_a)=c_0`,
\[
\boxed{W_a(\theta)-\sqrt a<W_0(\theta)}
\tag{8}
\]
for every angle whenever `0<a<3/4`. Integrating (8) in (5),
\[
\boxed{p_Q(-a)<p_Q(0)\qquad(0<a<3/4).}
\tag{9}
\]
For `a>=3/4`, the level has zero three-dimensional probability density support (at `a=3/4` only the two cube corners on the `e` axis remain), so (9) covers the entire negative-output range.

## 5. Exact global norm and continuity for this family

Combining (3), (9), and the partner's exact formula (1),
\[
\boxed{
\|p_Q\|_\infty=p_Q(0)
=6\sqrt3\,\operatorname{artanh}\!\left(\frac{\sqrt2-1}{\sqrt3}\right)
=2.5343552034856026468\ldots .
}
\tag{10}
\]
Thus the canonical maximally shared three-heavy Householder cube is globally harmless: its off-tip two-sheet branch cannot exceed the cone-tip value.

The density in (2) has a continuous representative for this family. Away from zero, the circle/cube intersection changes continuously except on a measure-zero set of tangencies, with compact domination. On the negative side, (5) and the implicit endpoint equation show `W_a(theta)` is continuous and (8) supplies domination as `a downarrow0`; therefore `p_Q(-a)->p_Q(0)`. On the positive side, radial slice indicators converge to the cone indicators except at polygon-boundary angles, so dominated convergence gives `p_Q(s)->p_Q(0)` as `s downarrow0`. Hence family-level continuity is proved. This does **not** prove continuity for the full owner target.

## 6. Quantitative witness implication

The exact global value satisfies
\[
2.5343552034\ldots<\pi<3\sqrt2=4.2426406871\ldots.
\]
An elementary analytic comparison follows from `artanh(x)<x/(1-x^2)` for `0<x<1`:
\[
p_Q(0)<9\left(1-\frac1{\sqrt2}\right)<3.
\]
Therefore this exact dense three-variable rotated witness is separated by more than `1.7` from the current source-valid lower obstruction `3\sqrt2` generated by the diffuse growing-dimensional partner family.

This completes the designated partner's open equation-level question: their exact tip certificate plus the inequalities (3) and (9) give the **global** `L^infinity` norm of the same law, rather than merely a cone-tip sample.

## 7. Scope and next witness mechanism

This theorem is not a proof of full QFORM. It uses the centered unit cube and the specific Householder minority axis `e=(1,1,1)/sqrt3`. It does not cover arbitrary cap-one fragmented marginals, unequal axes, extra spectrum, or growing-dimensional coupled constructions.

The sharp-witness search should therefore move away from this canonical finite dense cube. Remaining plausible mechanisms include asymmetric/fragmented laws in several genuinely coupled heavy coordinates, unequal Householder axes with optimized product supports, or growing-dimensional multiscale constructions not reducible to a Gaussian core plus independent shift.

## 8. Source/correction discipline

Fresh owner control at publication remained revision `2026-09-22.15`, QFORM-only, no paused accounts/slots, resolved from brain main during this run. Consumed the current `CURRENT_RESEARCH.md`, `CLAIMS.json`, assignment card, memory protocol, and live correction stream, including the newly posted `QFORM-BLOCKPRODUCT-PARABOLIC-SHELL-GRADIENT-TRACE-FAIL-v1`. That correction concerns an ambient grouped-gradient trace interface and is not used here. This proof uses only exact cube geometry, convex planar slices, and the partner's source-pinned cone-tip identity; it uses no arbitrary-joint coarea bound, no conditional projection moment, no pointwise van-der-Corput claim, no post-rotation independence, and no histogram extremality inference.

Full QFORM status: **OPEN / NOT PROVED**.  
Full-target continuity: **OPEN**.  
This family: exact bounded continuous density with global norm given by (10).
