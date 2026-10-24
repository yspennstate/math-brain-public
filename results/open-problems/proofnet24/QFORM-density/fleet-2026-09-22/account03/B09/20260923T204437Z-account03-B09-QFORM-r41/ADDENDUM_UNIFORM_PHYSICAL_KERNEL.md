# r41 addendum — uniform physical-kernel curvature/shear interpolation

## Why this addendum exists

After the first report was committed, the worker-owned memory pointer was refreshed and the immediately preceding same-slot run `20260923T194636Z-account03-B09-QFORM-r41` was consumed. That run proved `QFORM-3x2-KERNELSHEAR-L1-v1` for an arbitrary geometric kernel direction at the exact zero-curvature stratum and identified `QFORM-V1-CURVATURE-SHEAR-INTERPOLATION-AGGREGATE-v1` as the remaining implication.

The argument below advances that precise debt in the important **physical-kernel** case. It is stronger than the first theorem in `REPORT.md`: it gives the same fifth-degree invariant homogeneity as the preceding kernel-shear theorem, is uniform through *all* scalar kernel curvatures, and pays every positive physical-axis one-index-overlap packet. It uses original-coordinate factorization that is unavailable for a general rotated kernel direction.

Status: **supporting theorem proved, pending independent review; full QFORM open**.

## 1. Physical-kernel setup

Take five distinct original coordinates

\[
h,i_1,i_2,j_1,j_2.
\]

Condition on all other original coordinates. Put

\[
X=X_h,\qquad Y=(X_{i_1},X_{i_2}),\qquad Z=(X_{j_1},X_{j_2}).
\]

Assume the selected physical `3x2` cross block from the left triple `L={h,i1,i2}` to the right pair `R={j1,j2}` has the form

\[
A[L,R]=
\begin{pmatrix}
0&0\\
&\\[-2mm]
&C
\end{pmatrix},
\qquad C\in\mathbb R^{2\times2},\quad \det C\ne0.
\tag{1.1}
\]

Thus the one-dimensional left kernel is the literal physical coordinate direction `e_h`. Let the first column of the physical left self-block `P=A[L,L]` be

\[
P e_h=(d,p_1,p_2)^T,
\qquad p=(p_1,p_2),
\qquad R_*:=\sqrt{d^2+\|p\|_2^2}.
\tag{1.2}
\]

After outside conditioning the retained polynomial is, with arbitrary real quadratic-affine `F,G` and arbitrary `beta`,

\[
Q=dX^2+2X(p^TY+\beta)+F(Y)+2Y^TCZ+G(Z).
\tag{1.3}
\]

No assumption is made on `d`; in particular it may pass through zero. All same-side curvature on `Y,Z`, all outside couplings, and all affine terms are retained.

Let

\[
\Delta:=|\det C|.
\tag{1.4}
\]

The two columns of the literal physical `3x2` block (1.1) have cross product

\[
w=\pm\Delta e_h,
\tag{1.5}
\]

so

\[
\|w\|\,\|Pw\|
=\Delta^2 R_*.
\tag{1.6}
\]

## 2. Main interpolation theorem

### Theorem `QFORM-PHYSICALKERNEL-3x2-UNIFORM-v1`

If `R_*>0`, then the full ambient quadratic form has an `L^1` characteristic function and hence a bounded continuous density satisfying

\[
\boxed{
\|p_Q\|_\infty
\le C_{pk}(\Delta^2R_*)^{-1/5}
=C_{pk}(\|w\|\,\|Pw\|)^{-1/5},
}
\tag{2.1}
\]

where

\[
C_{pk}
=2^{1/10}\,2\left(\frac{10}{3}\right)^{4/5}
=5.616114990760686\ldots.
\tag{2.2}
\]

The same coefficient multiplies every interval length.

This theorem is uniform in `d`, including arbitrarily small nonzero `d` and exactly `d=0`. It closes the preceding run's curvature/shear interpolation debt **when the rank-two cross kernel is an original physical coordinate**.

The proof has two source-coordinate estimates with the same invariant homogeneity:

1. a fifth-power scalar Fresnel bound paying `|d|`;
2. a difference-variable/shear bound paying `||p||`, uniform in `d`.

At least one pays because `R_*>0`.

## 3. Common rank-two bilinear wrapper

Let

\[
H_y(t)=\int f_X(x)e^{it(d x^2+2x(p^Ty+\beta))}\,dx
\tag{3.1}
\]

and

\[
h(t)=\left(\int\rho_Y(y)|H_y(t)|^2dy\right)^{1/2}.
\tag{3.2}
\]

Exactly as in the first report, the characteristic function satisfies

\[
|\phi_Q(t)|\le h(t)
\tag{3.3}
\]

and, by two-dimensional source-coordinate bilinear Plancherel,

\[
|\phi_Q(t)|
\le\frac{\pi}{|t|\sqrt\Delta}h(t).
\tag{3.4}
\]

Hence

\[
|\phi_Q(t)|\le h(t)w_K(t),
\qquad
w_K(t)=\min(1,K/|t|),
\qquad
K=\pi\Delta^{-1/2}.
\tag{3.5}
\]

For exponent `5/4`,

\[
\int_{\mathbb R}w_K(t)^{5/4}dt
=10K,
\qquad
\|w_K\|_{5/4}=(10K)^{4/5}.
\tag{3.6}
\]

Therefore every `L^5` bound for `h` produces

\[
\|p_Q\|_\infty
\le\frac1{2\pi}\|h\|_5(10\pi\Delta^{-1/2})^{4/5}.
\tag{3.7}
\]

The rest of the proof supplies two different `L^5` budgets.

## 4. Curvature budget with fifth-degree homogeneity

Assume `d!=0`. For fixed `y`, complete the square in (3.1). It is enough to control

\[
G_m(t)=\int f_X(x)e^{itd(x-m)^2}dx
\tag{4.1}
\]

uniformly in `m`.

Let `S=(X-m)^2`. Its density is

\[
g_m(s)=\frac{f_X(m+\sqrt s)+f_X(m-\sqrt s)}{2\sqrt s}.
\tag{4.2}
\]

Writing `q=f_++f_-<=2`, the inequality `q^{5/4}<=2^{1/4}q` gives

\[
\int_0^\infty g_m(s)^{5/4}ds
\le\int_{\mathbb R}f_X(x)|x-m|^{-1/4}dx.
\tag{4.3}
\]

Bathtub rearrangement under `0<=f_X<=1` and total mass one yields

\[
\int_{\mathbb R}f_X(x)|x-m|^{-1/4}dx
\le\int_{-1/2}^{1/2}|u|^{-1/4}du
=\frac{2^{9/4}}3.
\tag{4.4}
\]

Thus

\[
\|g_m\|_{5/4}
\le\frac{2^{9/5}}{3^{4/5}}.
\tag{4.5}
\]

Hausdorff--Young with the angular Fourier convention and scaling by `d` gives

\[
\boxed{
\|G_m\|_5
\le (2\pi)^{1/5}
\frac{2^{9/5}}{3^{4/5}}|d|^{-1/5}.
}
\tag{4.6}
\]

The estimate is uniform in `m`, hence uniform in `y`. Minkowski applied to (3.2) gives the same bound for `||h||_5`. Substitution in (3.7) simplifies exactly to

\[
\boxed{
\|p_Q\|_\infty
\le C_d(\Delta^2|d|)^{-1/5},
\qquad
C_d=2\left(\frac{10}{3}\right)^{4/5}
=5.240020570644153\ldots.
}
\tag{4.7}
\]

Unlike the sharper `|d\Delta|^{-1/3}` bound in the first report, (4.7) deliberately uses the fifth-degree homogeneity matching the shear packet.

## 5. Shear budget uniform in the scalar curvature

Now assume `p!=0`; **no condition at all is placed on `d`**.

Let `X'` be an independent copy of the physical hub variable `X`, put

\[
D=X-X',
\qquad
T=p^TY.
\tag{5.1}
\]

Expanding the square of (3.1) and averaging over `Y` gives

\[
\begin{aligned}
h(t)^2
&=\mathbb E_{X,X'}
 e^{itd(X^2-X'^2)+i2t\beta D}
 \phi_T(2tD),
\end{aligned}
\tag{5.2}
\]

where `phi_T` is the characteristic function of `T`. Therefore

\[
h(t)^2\le\mathbb E_D|\phi_T(2tD)|.
\tag{5.3}
\]

This is the key interpolation step: the entire scalar curvature phase has disappeared only *after* squaring the hub transform, while the original-coordinate shear survives as the genuine product projection `T=p^TY`.

### 5.1 Difference negative moment

The difference `D=X-X'` has probability density

\[
f_D=f_X*\widetilde f_X,
\]

and

\[
\|f_D\|_\infty\le\|f_X\|_2^2\le1.
\tag{5.4}
\]

For every cap-one probability density the bathtub principle gives

\[
\mathbb E|D|^{-2/5}
\le\int_{-1/2}^{1/2}|u|^{-2/5}du
=\frac53\,2^{2/5}.
\tag{5.5}
\]

### 5.2 Physical shear projection

Because `Y_1,Y_2` are original independent coordinates with densities bounded by one, conditioning on the coordinate having the larger coefficient shows

\[
\|p_T\|_\infty
\le\frac1{\max(|p_1|,|p_2|)}
\le\frac{\sqrt2}{\|p\|}=:S.
\tag{5.6}
\]

No rotated independence is asserted. This is a direct original-coordinate conditioning bound.

Since `p_T` has mass one and cap `S`,

\[
\|p_T\|_{5/3}\le S^{2/5}.
\tag{5.7}
\]

Hausdorff--Young gives

\[
\|\phi_T\|_{5/2}
\le(2\pi)^{2/5}S^{2/5}.
\tag{5.8}
\]

### 5.3 L^5 hub budget

Apply Minkowski to (5.3) in `L^{5/2}(dt)`:

\[
\begin{aligned}
\|h\|_5^2
&=\|h^2\|_{5/2}\\
&\le\mathbb E_D\|\phi_T(2D\,\cdot)\|_{5/2}\\
&=2^{-2/5}\|\phi_T\|_{5/2}
  \mathbb E|D|^{-2/5}.
\end{aligned}
\tag{5.9}
\]

Using (5.5) and (5.8), the powers of two from the difference scaling cancel:

\[
\|h\|_5^2
\le\frac53(2\pi S)^{2/5}.
\tag{5.10}
\]

Therefore

\[
\boxed{
\|h\|_5
\le\sqrt{\frac53}
 (2\pi\sqrt2)^{1/5}\|p\|^{-1/5}.
}
\tag{5.11}
\]

Substituting into (3.7) yields

\[
\boxed{
\|p_Q\|_\infty
\le C_s(\Delta^2\|p\|)^{-1/5},
}
\tag{5.12}
\]

where

\[
C_s
=\frac12\sqrt{\frac53}
 2^{3/10}10^{4/5}
=5.014219919615765\ldots.
\tag{5.13}
\]

Most importantly, (5.12) is **uniform in `d`**. This removes the discontinuity between the preceding exact-zero-curvature kernel-shear theorem and the nonzero-curvature branch in the physical-kernel geometry.

## 6. Combine curvature and shear

Let

\[
R_*=\sqrt{d^2+\|p\|^2}>0.
\]

At least one of

\[
|d|\ge R_*/\sqrt2,
\qquad
\|p\|\ge R_*/\sqrt2
\]

holds. Use (4.7) in the first case and (5.12) in the second. Since `C_d>C_s`,

\[
\|p_Q\|_\infty
\le2^{1/10}C_d(\Delta^2R_*)^{-1/5},
\]

which is (2.1)-(2.2).

The characteristic function is `L^1` in either branch, so the density is continuous. The same constant times interval length gives the small-ball estimate.

## 7. Relation to the preceding same-slot theorem

The preceding same-slot report

`yspennstate/math-open-problems@cb5f7af03bad40481c80db84527c2799b27bd8aa:proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T194636Z-account03-B09-QFORM-r41/REPORT.md`

proved, for an **arbitrary geometric kernel direction** `n`, the exact stratum

\[
d=n^TPn=0,\qquad p=(I-nn^T)Pn\ne0,
\]

with

\[
\|p_Q\|_\infty
\le5.9501\,\Delta^{-2/5}\|p\|^{-1/5}.
\]

The present theorem is narrower geometrically because `n` must be a literal original-coordinate axis, but stronger analytically inside that geometry:

- it improves the shear constant to `5.0143`;
- it permits **arbitrary** kernel curvature `d`, including tiny nonzero values;
- combined with the scalar branch it pays the entire physical-axis packet whenever `Pn!=0`.

Thus `QFORM-V1-CURVATURE-SHEAR-INTERPOLATION-AGGREGATE-v1` is now reduced further: the interpolation issue remains only for genuinely non-coordinate kernel directions (or for a compiler that must aggregate many such packets without selecting a bad reciprocal scale).

## 8. Target-valid regression

For any real `d`, let the physical `5x5` matrix have

\[
A_{00}=d,
\quad A_{01}=A_{10}=1,
\quad A_{13}=A_{31}=1,
\quad A_{24}=A_{42}=1,
\]

and all other entries zero. For `d=0` its spectrum is

\[
\{-\sqrt2,-1,0,1,\sqrt2\},
\]

so it is target-valid. The same is true for small nonzero `d`; e.g. at `d=10^{-6}` the eigenvalues are approximately

\[
-1.41421331,-1,5\cdot10^{-7},1,1.41421381.
\]

Here `Delta=1`, `||p||=1`, and (5.12) gives, **uniformly through `d=0`**,

\[
\boxed{\|p_Q\|_\infty\le5.014219920.}
\tag{8.1}
\]

No two disjoint physical triples exist in dimension five, so this is again outside the literal disjoint `3x3` partner geometry.

## 9. Remaining implication

The genuinely new remaining B09 problem is now:

**`QFORM-NONCOORDINATE-KERNEL-INTERPOLATION-OR-COMPILER-v1`.**

Given a rank-two physical `3x2` cross block whose one-dimensional left kernel is a non-coordinate direction `n`, prove a bound uniform through small nonzero `d=n^TPn` while spending the shear `(I-nn^T)Pn`, *without* asserting independence in the rotated `(n,n^perp)` coordinates; or compile the global one-index-overlap volume into enough physical-axis packets that Theorem (2.1) pays the aggregate.

The obstruction is now sharply source-theoretic: for a non-coordinate `n`, the fiber law along `n` is correlated with the transverse projection, so the factorization used in (5.2) is no longer automatic. The exact-zero theorem can exploit a linear fiber Fourier transform even with that dependence, but the present difference-variable argument needs the literal physical hub to preserve independence from `Y`.

Full QFORM remains **OPEN**. Full-target continuity remains **OPEN**.
