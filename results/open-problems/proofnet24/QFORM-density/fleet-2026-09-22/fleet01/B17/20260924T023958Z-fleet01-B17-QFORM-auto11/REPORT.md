SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-24T02:39:58Z.
attacking: a genuinely entrywise-dense finite six-variable witness obtained by a controlled spectral rotation of the exact two-per-bank stress family, plus an actual target-matrix application of the completed fleet02/B17 sheared-square theorem.

# QFORM B17 — dense six-variable near-bank witness and rotation-stability lower bound

Programme: `QFORM-DENSITY-3EIG-20260922` revision `2026-09-22.5`.
Status: **NEW SUPPORTING SHARP-WITNESS THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED.** Full-target continuity remains separate.
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Main theorem: a fixed six-variable, entrywise-dense target witness above 3.9488

Let `X_1,...,X_6` be independent `Uniform[-1/2,1/2]` variables and define the `6 x 3` Parseval bank matrix

\[
R=\frac1{\sqrt2}
\begin{pmatrix}
1&0&0\\
1&0&0\\
0&1&0\\
0&1&0\\
0&0&1\\
0&0&1
\end{pmatrix},\qquad R^TR=I_3.
\]

Set `M=100000`, `D=M^2+5`, and

\[
n_M=\frac1D\,(2M,4M,M^2-5)^T.
\]

The identity

\[
4M^2+16M^2+(M^2-5)^2=(M^2+5)^2
\]

shows `||n_M||_2=1`. Put

\[
B_M=I_3-2n_Mn_M^T,\qquad A_M=RB_MR^T.
\]

Then `B_M` is a Householder involution, hence

\[
\operatorname{spec}_{\ne0}(A_M)=\operatorname{spec}(B_M)=\{1,1,-1\}.
\]

Thus `A_M` is an exact target matrix. Moreover every physical entry of `A_M` is nonzero. Indeed every `2 x 2` physical block equals the scalar `B_{ij}/2`, and

\[
\begin{aligned}
B_{11}&=\frac{M^4+2M^2+25}{D^2},\\
B_{22}&=\frac{M^4-22M^2+25}{D^2},\\
B_{33}&=\frac{-M^4+30M^2-25}{D^2},\\
B_{12}&=-\frac{16M^2}{D^2},\\
B_{13}&=-\frac{4M(M^2-5)}{D^2},\\
B_{23}&=-\frac{8M(M^2-5)}{D^2}.
\end{aligned}
\]

All six quantities are nonzero at `M=100000`.

Write `Y=R^T X`. Its three coordinates are independent and each has triangular density

\[
g(y)=\sqrt2\,(1-\sqrt2|y|)_+,\qquad |y|\le 1/\sqrt2.
\]

Hence

\[
X^TA_MX=Y^TB_MY.
\]

The density of this quadratic form has a continuous representative at the origin, and the explicit lower bound is

\[
\boxed{
 p_{X^TA_MX}(0)
 \ge 2\pi-\frac73-\frac{6\pi\sqrt{30}}{100000}
 >3.9488.
}
\tag{1}
\]

Consequently even in the fixed dimension `n=6`, with an entrywise-dense physical matrix and exact nonzero spectrum `{1,1,-1}`, one can force a peak above `3.9488`. This is a finite exact target witness, not a Gaussian limit and not a post-rotation independence argument.

## 2. Rotation-Lipschitz cone-tip lemma

The estimate behind (1) is useful independently of the chosen rational rotation.

Let

\[
J=\operatorname{diag}(1,1,-1),\qquad B=OJO^T,
\]

where `O` is orthogonal. Let `rho` be an `L`-Lipschitz compactly supported density on `R^3`, supported in the Euclidean ball of radius `R_0`. For the natural coarea density at zero,

\[
p_B(0)=\int_{\mathbb R^3}\delta(y^TBy)\rho(y)\,dy,
\]

one has

\[
\boxed{
|p_B(0)-p_J(0)|
\le \frac{\pi L R_0^2}{\sqrt2}\,\|O-I\|_{op}.
}
\tag{2}
\]

Proof. Change variables `y=Oz`. Since `O` is orthogonal,

\[
p_B(0)-p_J(0)
=\int \delta(z^TJz)\,[\rho(Oz)-\rho(z)]\,dz.
\]

The Lipschitz bound gives

\[
|\rho(Oz)-\rho(z)|\le L\|O-I\|_{op}|z|.
\]

On the unit sphere the null set of `q(omega)=omega^TJ omega` is the union of the two circles `omega_3=\pm1/\sqrt2`. Their total spherical length is `2\sqrt2\pi`, while on the null set

\[
|\nabla_{S^2}q|=2.
\]

Therefore

\[
\int_{S^2}\delta(q(\omega))\,d\sigma(\omega)=\sqrt2\pi.
\]

Using spherical coordinates and the homogeneity `q(r omega)=r^2 q(omega)`, the extra factor `|z|=r` gives

\[
\int_{|z|\le R_0}\delta(z^TJz)|z|\,dz
=\left(\int_0^{R_0}r\,dr\right)\sqrt2\pi
=\frac{\pi R_0^2}{\sqrt2}.
\]

This proves (2).

For the triangular product density

\[
\rho(y)=g(y_1)g(y_2)g(y_3),
\]

we have `||g||_infinity=sqrt(2)` and `Lip(g)=2`, hence by telescoping

\[
\operatorname{Lip}(\rho)\le4\sqrt3.
\]

Its support lies in the ball of radius `R_0=sqrt(3/2)`. Thus (2) specializes to

\[
\boxed{|p_B(0)-p_J(0)|\le 3\pi\sqrt6\,\|O-I\|_{op}.}
\tag{3}
\]

For a minimum-angle rotation carrying `e_3` to the negative eigenvector `n_M`,

\[
\|O-I\|_{op}=\|n_M-e_3\|_2
=\sqrt{\frac{20}{M^2+5}}
<\frac{2\sqrt5}{M}.
\]

Substitution into (3) gives the error term in (1).

This local rotation-stability statement does **not** use or assert the false arbitrary-joint global coarea cap from the correction inbox. It only compares two nearby spectral orientations for this fixed compact Lipschitz source.

## 3. Exact aligned value `2 pi - 7/3`

For `B=J`, put `Z=Y^2`. Since `g` is even,

\[
h(s)=\frac{g(\sqrt s)}{\sqrt s}
=\sqrt2\,s^{-1/2}-2,
\qquad 0<s<\frac12.
\]

For `0<s<1/2`, the density of `Z_1+Z_2` is

\[
\begin{aligned}
f_{12}(s)
&=\int_0^s h(u)h(s-u)\,du\\
&=2\pi-8\sqrt{2s}+4s.
\end{aligned}
\]

Therefore the density at the zero level of

\[
Y_1^2+Y_2^2-Y_3^2
\]

is

\[
\boxed{
 p_J(0)=\int_0^{1/2} f_{12}(s)h(s)\,ds
 =2\pi-\frac73
 =3.94985197384625\ldots .
}
\tag{4}
\]

For this compact Lipschitz source the rank-three indefinite pushforward has a continuous density at zero: away from a small ball the gradient is bounded away from zero and ordinary coarea varies continuously in the level; the contribution of a ball of radius `eta` is `O(eta)` after the quadratic scaling `y=eta u`. Hence (4) and (1) are genuine essential-supremum lower witnesses, not values assigned at an isolated point.

A useful structural corollary follows by letting `M -> infinity` through the rational family above:

\[
\boxed{
\sup_{\substack{A\in\mathbb R^{6\times6}\,\text{entrywise dense}\\
\operatorname{spec}_{\ne0}(A)=\{1,1,-1\}}}
\ \sup_{\substack{X_i\ \text{independent}\\f_i\le1}}
\|p_{X^TAX}\|_\infty
\ge 2\pi-\frac73.
}
\tag{5}
\]

The source-valid unrestricted obstruction remains the stronger asymptotic bound `C_univ >= 3 sqrt(2)` from the diffuse three-bank limit. The new point is finite-dimensional and geometric: exact entrywise density of the physical matrix does not force a meaningful gap below the bank witness.

## 4. Actual application of the completed fleet02/B17 theorem

The completed partner theorem is source-pinned at

`yspennstate/math-open-problems@5358d1f4f32d64254b0234463015b42f1d36bc13`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260924T004826Z-fleet02-B17-QFORM-7c2f/REPORT.md`.

It proves that for arbitrary independent cap-one laws and

\[
Q=rX^2+2aXY+2cXZ+bZ^2+uX+vY+wZ+q_0,
\]

\[
\|p_Q\|_\infty\le
\begin{cases}
\dfrac{2+\log(4|a|/|b|)}{|a|},&|b|\le4|a|,\\[1ex]
\dfrac4{\sqrt{|ab|}},&|b|\ge4|a|.
\end{cases}
\tag{6}
\]

Apply (6) to the new concrete physical target matrix

\[
A_{\rm leaf}=
\begin{pmatrix}
0&4&1\\
4&0&0\\
1&0&4
\end{pmatrix},
\qquad
Q_{\rm leaf}=8XY+2XZ+4Z^2.
\]

Here `a=4`, `b=4`, `c=1`. Thus

\[
\boxed{
\|p_{Q_{\rm leaf}}\|_\infty
\le \frac{2+\log4}{4}
=0.846573590279972\ldots .
}
\tag{7}
\]

This is an actual target inequality. Indeed

\[
A_{\rm leaf}^2-I=
\begin{pmatrix}
16&0&4\\
0&15&4\\
4&4&16
\end{pmatrix},
\]

whose leading principal minors are

\[
16,\qquad 240,\qquad3344.
\]

Hence `A_leaf^2-I` is positive definite, so every eigenvalue of `A_leaf` has absolute value strictly larger than one.

The comparison is sharp-witness information: the exact one-null-leaf architecture can be globally tiny even with strong shear and all three physical eigenvalues beyond threshold, whereas the six-variable shared-bank geometry already gives a dense finite peak above `3.9488`. Therefore a proof that collapses a general target instance to one affine physical leaf can discard a large amount of concentration and cannot be treated as a sharpness-preserving reduction.

## 5. Corrections and remaining frontier

Preserved corrections: no post-rotation independence; no arbitrary-joint coarea `||rho||_infinity^(2/3)` premise; no conditional-density-cap substitution; no universal fixed fragment-count reduction; no generic two-sheet X-ray-only bound; no uniform pointwise stationary-phase decay over arbitrary cap-one laws.

No claim here proves `C_univ=3sqrt(2)`. The strongest source-valid lower bound remains

\[
\boxed{C_{\rm univ}\ge3\sqrt2.}
\]

The new finite dense witness narrows what a sharp proof may erase: sparse bank geometry can be perturbed to an entrywise-dense physical matrix while retaining essentially the same cone-tip concentration. The still-interesting witness mechanisms are several genuinely shared/intermediate-leverage directions, off-zero/two-sheet peaks, rough fragmented cap-one laws, and extra active spectrum.
