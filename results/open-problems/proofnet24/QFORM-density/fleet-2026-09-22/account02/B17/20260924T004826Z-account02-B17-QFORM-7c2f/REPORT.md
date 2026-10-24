# QFORM B17 — one-null-leaf sheared-square global barrier

Run: `20260924T004826Z-account02-B17-QFORM-7c2f`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Classification: **NEW SUPPORTING ANALYTIC THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Continuity: proved only for this branch; full-target continuity remains separate.

## 1. First unpaid implication paid

The preceding B17 witness map left a bounded-bank/intermediate-leverage gap around the exact null-pair family: can one add nontrivial curvature on one null-pair coordinate and simultaneously shear that coordinate into the square coordinate without producing a new sharp witness?

The answer is no, with exactly the same quantitative ceiling as the sharpened null-pair-plus-square theorem.

Let `X,Y,Z` be independent real random variables with probability densities `f_X,f_Y,f_Z <= 1`. Let `a,b` be nonzero and let `r,c,u,v,w,q0` be arbitrary real numbers. Define

\[
Q=rX^2+2aXY+2cXZ+bZ^2+uX+vY+wZ+q_0.
\tag{1}
\]

Then `Q` has a continuous density and

\[
\boxed{
\|p_Q\|_\infty\le \mathcal C(a,b):=
\begin{cases}
\dfrac{2+\log(4|a|/|b|)}{|a|},& |b|\le4|a|,\\[1.1ex]
\dfrac4{\sqrt{|ab|}},& |b|\ge4|a|.
\end{cases}}
\tag{2}
\]

Thus the bound is completely insensitive to the arbitrary same-side square coefficient `r`, the physical shear `c`, and all affine terms. In particular, if `|a|,|b|>=1`,

\[
\boxed{\|p_Q\|_\infty\le2+\log4<3\sqrt2.}
\tag{3}
\]

This is a genuinely larger physical family than `2aXY+bZ^2`: after conditioning on any ambient outside coordinates, (1) remains in the theorem because only the affine coefficients change.

## 2. Exact root formula after the only necessary translation

The `vY` term is removed by translating `X` by `v/(2a)`. Translation preserves independence and each one-dimensional density cap, and it changes only `r,c,u,w,q0`, not `a` or `b`. Hence assume `v=0`.

For fixed `x!=0`, write

\[
R_x(z)=bz^2+L(x)z+M(x),
\]

where `L(x)=2cx+w` and `M(x)=rx^2+ux+q0`. Resolving the level equation `Q=s` in the original physical coordinate `Y` gives

\[
y={s-R_x(z)\over 2ax},
\]

and therefore

\[
p_Q(s)=\int_{\mathbb R}{f_X(x)\over2|ax|}\,I_x(s)\,dx,
\qquad
I_x(s)=\int_{\mathbb R} f_Z(z)
 f_Y\!\left({s-R_x(z)\over2ax}\right)dz.
\tag{4}
\]

No rotated-coordinate independence is used.

## 3. Two simultaneous inner caps

First, since `f_Y<=1` and `f_Z` has probability mass one,

\[
I_x(s)\le1.
\tag{5}
\]

Second, since `f_Z<=1`,

\[
I_x(s)\le\int_{\mathbb R}
 f_Y\!\left({s-M(x)-bz^2-L(x)z\over2ax}\right)dz.
\tag{6}
\]

Complete the square in `z`:

\[
bz^2+L(x)z=b\left(z+{L(x)\over2b}\right)^2-{L(x)^2\over4b}.
\]

The translation of `z` has unit Jacobian. Thus (6) is exactly the same one-dimensional parabola-preimage bathtub appearing in the latest account03/B17 theorem, with

\[
\beta={|b|\over2|ax|}.
\]

The completed partner lemma gives the sharp translation-uniform estimate

\[
\int f_Y(C\pm\beta z^2)\,dz\le2\beta^{-1/2},
\]

hence

\[
\boxed{I_x(s)\le\min\left\{1,\ 2\sqrt{2|ax|/|b|}\right\}.}
\tag{7}
\]

This is the equation-level use of the latest completed partner result: its probability-mass/parabola-preimage cap survives arbitrary `x`-dependent vertex translation, and therefore survives both the shear `2cXZ` and the same-side curvature `rX^2`.

Substituting (7) in (4),

\[
p_Q(s)\le\int f_X(x)K_{a,b}(|x|)\,dx,
\quad
K_{a,b}(t)=\min\left\{{1\over2|a|t},{\sqrt2\over\sqrt{|ab|}\sqrt t}\right\}.
\tag{8}
\]

The kernel is even and decreasing in `|x|`.

## 4. Outer bathtub and exact constant

The cap-one probability constraint on `f_X` gives

\[
\int f_X(x)K_{a,b}(|x|)dx
\le2\int_0^{1/2}K_{a,b}(t)dt.
\tag{9}
\]

The two branches meet at

\[
t_0={|b|\over8|a|}.
\]

If `|b|>=4|a|`, then `t_0>=1/2` and (9) is `4/sqrt(|ab|)`. If `|b|<=4|a|`, splitting at `t_0` gives

\[
2\int_0^{1/2}K_{a,b}(t)dt
={2+\log(4|a|/|b|)\over|a|}.
\]

This proves (2). The target-range optimization `|a|,|b|>=1` is identical to the partner calculation and yields (3).

## 5. Explicit source-valid target matrix with real shear and curvature

Take

\[
A_*=
\begin{pmatrix}
1&2&1\\
2&0&0\\
1&0&2
\end{pmatrix},
\qquad
Q_*=X^2+4XY+2XZ+2Z^2.
\tag{10}
\]

This is not the exact null-pair direct sum: both the curvature `X^2` and the physical shear `XZ` are nonzero. The theorem uses `a=b=2`, so for **arbitrary independent cap-one laws**

\[
\boxed{\|p_{Q_*}\|_\infty\le1+\log2=1.693147180559945\ldots.}
\tag{11}
\]

The spectral hypothesis is checked in the physical basis without diagonalising the laws. Indeed

\[
A_*^2-I=
\begin{pmatrix}
5&2&3\\
2&3&2\\
3&2&4
\end{pmatrix}.
\]

Its leading principal minors are

\[
5,\qquad11,\qquad21,
\]

so `A_*^2-I` is positive definite. Therefore every eigenvalue `lambda` of `A_*` satisfies

\[
\boxed{|\lambda|>1.}
\tag{12}
\]

Numerically the eigenvalues are approximately

\[
-1.66907909,\quad1.52397640,\quad3.14510269.
\]

Thus (10) is a genuine finite, non-diagonal, intermediate/macroscopic-leverage QFORM instance, not merely a proof surrogate.

## 6. Required pinned-source inequality on the same witness

The completed pinned `e5f71d79...` `COUNTEREXAMPLE_SEARCH.md` Theorem C applies directly to every rank-three signature `(+,+,-)` form with all three eigenvalue magnitudes at least one and gives, on the one-sheet side,

\[
p_Q(s)\le\pi\sqrt2,\qquad s\ge0.
\tag{13}
\]

Because (12) verifies its spectral hypothesis for the **actual physical matrix** `A_*`, it yields the real inequality

\[
\sup_{s\ge0}p_{Q_*}(s)\le\pi\sqrt2.
\tag{14}
\]

The new original-coordinate root/bathtub argument strengthens this on the same witness to the global all-sign estimate (11). This comparison is useful structurally: the generic ruled-level-set constant is a correct universal one-sheet obstruction but is too large to prove the candidate sharp value `3sqrt2`; here the one-null-leaf algebra pays much more. Failure of the generic `pi sqrt2` constant to be sharp is a proof-constant limitation, not a QFORM counterexample.

## 7. Continuity in this branch

For each fixed `x!=0`, the variable `2axY` has an `L^1` density. The quadratic polynomial `R_x(Z)` has an `L^1` density (possibly with the usual square-root singularity at its vertex), so its convolution with `2axY` has a continuous density. The pointwise envelope obtained from (7), divided by `2|ax|`, is exactly `K_{a,b}(|x|)`, which is integrable against every cap-one probability density by (9). Dominated convergence in `x` gives a continuous representative of `p_Q`.

This is only a branchwise continuity statement and does not settle full-target continuity.

## 8. Sharp-witness consequence and remaining unpaid class

The whole family

\[
A=
\begin{pmatrix}
r&a&c\\
a&0&0\\
c&0&b
\end{pmatrix}
\]

is globally controlled by (2) for arbitrary one-dimensional cap-one product laws, independently of `r,c`. In particular, tuning same-side curvature or shearing the null-pair coordinate into the square receiver cannot create a new witness above the known lower obstruction when `|a|,|b|>=1`.

What remains genuinely unpaid is a perturbation that destroys the exact null leaf: a nonzero `Y^2` pivot, a nonzero `YZ` edge, or several non-collinear macroscopic rows/shared banks for which no original physical coordinate remains affine after conditioning the others. Those changes make the root denominator depend on two variables or replace the linear root by a two-root square kernel, and the present two-stage bathtub no longer applies. A peak above `3sqrt2` would refute only the proposed sharp constant; a true counterexample to QFORM must make the essential density unbounded across a target-admissible family.

## 9. Integrity notes

No moments, bounded support, connectedness, log-concavity, finite-fragment reduction, diagonal-basis independence, post-rotation independence, arbitrary-joint coarea theorem, or pointwise stationary-phase estimate is used. All integrations and conditioning are in original independent coordinates. The latest live corrections against generic two-sheet X-ray reduction, conditional cap substitutions, arbitrary-remainder absorption, and finite-fragment bathtub shortcuts are respected.

Status: **FULL QFORM REMAINS OPEN / NOT PROVED / NOT DISPROVED.**
