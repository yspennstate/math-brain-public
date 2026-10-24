# Addendum — arbitrary collinear leverage vector

Run: `QFORM-B17-20260922T225652Z`

This strengthens the equal-weight theorem in `REPORT.md`. Full QFORM remains OPEN.

## Theorem

Let `r>=1` and let `a_1,...,a_r in R` satisfy

\[
\sum_{i=1}^r a_i^2=1.
\]

Let `X_1,...,X_r` be independent real random variables with probability densities `0<=f_i<=1`, and let `G_1,G_2` be independent standard Gaussians, independent of the `X_i`. Define

\[
T_a=G_1^2+G_2^2-12\Big(\sum_{i=1}^r a_iX_i\Big)^2.
\]

If `U_i` are iid `Unif[-1/2,1/2]`, then

\[
\boxed{
\|p_{T_a}\|_\infty
\le
\frac12\,\mathbf E\exp\!\left[-6\Big(\sum_{i=1}^r a_iU_i\Big)^2\right].
}
\]

This bound is sharp over all independent cap-one laws `f_i`, and equality is attained at output zero when every `X_i` is a centered unit interval. Therefore the exact physical branch constant is

\[
\boxed{
C(a)=6\,\mathbf E\exp\!\left[-6\Big(\sum_{i=1}^r a_iU_i\Big)^2\right].
}
\]

Signs of the `a_i` do not matter for the extremal value because the centered interval law is symmetric.

## Proof

Discard zero coefficients. Put `y_i=a_i x_i`. The density of `Y_i=a_iX_i` is

\[
g_i(y)=|a_i|^{-1}f_i(y/a_i),
\qquad 0\le g_i\le |a_i|^{-1},
\qquad \int g_i=1.
\]

Let `z=sum_i y_i`. Since `G_1^2+G_2^2` has density `(1/2)e^{-u/2}1_{u>=0}`, the density of `T_a` is

\[
p_{T_a}(t)=\int_{\mathbb R^r}\prod_i g_i(y_i)\,K_t\!\left(\sum_i y_i\right)dy,
\]

with

\[
K_t(z)=\frac12e^{-(t+12z^2)/2}\mathbf 1_{\{t+12z^2\ge0\}}.
\]

For `t>=0`, `K_t=e^{-t/2}K_0` and `K_0` is symmetric decreasing. Brascamp--Lieb--Luttinger rearrangement gives

\[
p_{T_a}(t)\le e^{-t/2}\int\prod_i g_i^*(y_i)K_0(\sum y_i)dy.
\]

Fix all factors except `g_i^*`. The resulting one-variable kernel is symmetric decreasing. Among probability densities bounded by `|a_i|^{-1}`, the bathtub principle maximizes its integral at

\[
g_i^{\rm ext}(y)=|a_i|^{-1}\mathbf 1_{[-|a_i|/2,|a_i|/2]}(y).
\]

Iterating over all coordinates replaces the original laws by centered unit intervals in the original `x_i` variables and gives the asserted zero-output quantity.

For `t=-r_0^2<0`, the exact symmetric-decreasing rearrangement of the two-shell kernel is

\[
K_{-r_0^2}^*(u)
=\frac12e^{-\sqrt{12}\,r_0|u|-6u^2}.
\]

This is the same exact shell identity used in account02/B17's completed collinear theorem: a shell beginning at `z_0=r_0/sqrt(12)` with thickness `d` has total length `2d`, and after centering its exponent increment is `sqrt(12) r_0d+6d^2`.

Applying BLL and the same coordinatewise bathtub replacement yields

\[
p_{T_a}(-r_0^2)
\le \frac12\mathbf E\exp\!\left[-\sqrt{12}\,r_0\left|\sum_i a_iU_i\right|-6\left(\sum_i a_iU_i\right)^2\right]
\le \frac12\mathbf E e^{-6(\sum_i a_iU_i)^2}.
\]

Thus the displayed bound holds globally in output. At `t=0` and centered interval laws every step is equality, proving sharpness for this branch.

## Exact source-valid frame

Take the same two diffuse positive banks as in `REPORT.md`, and use heavy physical rows `a_i e_3`. Since `sum_i a_i^2=1`, the frame still satisfies `R^T R=I_3`; hence every finite matrix `A=R diag(1,1,-1)R^T` has exact nonzero spectrum `{1,1,-1}`. This is an original-coordinate product family at every finite dimension.

The equal-weight specialization `a_i=1/sqrt(k)` recovers the hierarchy `C_k` in `REPORT.md` and therefore its limit `C_k->3sqrt(2)`.

## Scope

The theorem excludes **all finite collinear splittings of one minority-sign spectral direction**, with arbitrary leverage shares, arbitrary independent cap-one fragmentation/translations, and every output location, from producing a peak larger than the explicit `C(a)`. It does not prove the universal inequality `C(a)<=3sqrt(2)` for every leverage vector, although equal-weight diffuse sequences approach `3sqrt(2)` from below. It also does not treat non-collinear heavy rows, coupled spectral tails, or the full arbitrary-matrix problem.
