SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-23T08:42:05Z.
attacking: a genuinely dense four-coordinate rank-three Hadamard stress, with an exact cone-tip density certificate and comparison to the diffuse sharp obstruction.

# Early substantive checkpoint: dense Hadamard rank-three witness

Let

\[
O=\frac12\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix},\qquad
J_0=\operatorname{diag}(1,1,-1,0),\qquad A=OJ_0O^T.
\]

Then `O` is orthogonal and

\[
A=\frac14\begin{pmatrix}
1&-1&3&1\\
-1&1&1&3\\
3&1&1&-1\\
1&3&-1&1
\end{pmatrix},
\qquad \operatorname{spec}(A)=\{1,1,-1,0\}.
\]

All sixteen physical entries are nonzero. Thus this is an exact source-valid dense shared-coordinate matrix, not a separated-bank or diagonal control.

Take independent `X_i~Unif[-1/2,1/2]`, so every physical density has cap exactly one. Put `Q=X^TAX`. I claim

\[
\boxed{p_Q(0)=8(\sqrt2-1)=3.313708498984\ldots>\pi.}
\tag{1}
\]

This already gives a finite exact rotated witness whose central density beats the sharp diagonal constant pi (while remaining below the known diffuse obstruction `3 sqrt(2)`).

## Derivation

Use spectral coordinates `(y_1,y_2,y_3,z)=O^TX`. Since the change is orthogonal,

\[
Q=y_1^2+y_2^2-y_3^2.
\]

Parametrize the two nappes of the cone by

\[
y=r(\cos\theta,\sin\theta,\sigma),\qquad r\ge0,\ \sigma\in\{\pm1\}.
\]

For the Lorentz form, the coarea element on each nappe is exactly

\[
\frac{dS}{|\nabla Q|}=\frac12\,dr\,d\theta.
\tag{2}
\]

For `sigma=+1`, the four cube constraints `|X_i|<=1/2`, after multiplying by two, become four unit-radius intervals for the null coordinate `z`, whose centers are `r b_j(theta)` with

\[
(b_1,b_2,b_3,b_4)=
(-c-s-1,\,-c+s+1,\,c-s+1,\,c+s-1),
\qquad c=\cos\theta,\ s=\sin\theta.
\]

Their intersection length is

\[
L(r,\theta)=\bigl(2-rD(\theta)\bigr)_+,
\qquad D(\theta)=\max_j b_j-\min_j b_j.
\tag{3}
\]

The six pairwise differences show

\[
D(\theta)=2\left(1+\max\{|\cos\theta|,|\sin\theta|\}\right).
\tag{4}
\]

Indeed the candidates `2(1+|c|)` and `2(1+|s|)` dominate `2|c+s|` and `2|c-s|`. Hence

\[
\int_0^\infty L(r,\theta)\,dr=\frac{2}{D(\theta)}.
\tag{5}
\]

The `sigma=-1` nappe gives the same angular integral by central symmetry. Combining (2)-(5),

\[
p_Q(0)=2\int_0^{2\pi}\frac{d\theta}{D(\theta)}.
\]

By eightfold symmetry and `max(c,s)=c` on `[0,pi/4]`,

\[
\begin{aligned}
p_Q(0)
&=2\cdot8\cdot\frac12\int_0^{\pi/4}\frac{d\theta}{1+\cos\theta}\\
&=8\tan(\pi/8)=8(\sqrt2-1),
\end{aligned}
\]

proving (1).

The strict comparison with the diagonal constant is elementary: `pi<22/7`, while `8(sqrt(2)-1)>22/7` because `sqrt(2)>39/28`. Also `8(sqrt(2)-1)<3sqrt(2)` because `5sqrt(2)<8`.

## Scope

This is a cone-tip certificate, not yet a proof that zero is the global mode. It deliberately leaves the off-center/two-sheet side unpaid. It uses no post-rotation independence, arbitrary-joint coarea bound, conditional-density moment, or pointwise one-dimensional stationary phase.
