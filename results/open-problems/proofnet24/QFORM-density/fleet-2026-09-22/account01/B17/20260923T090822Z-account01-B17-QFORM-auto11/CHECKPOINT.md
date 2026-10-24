# Early substantive checkpoint — a rotated dense Hadamard witness

Programme `QFORM-DENSITY-3EIG-20260922`; full conjecture remains OPEN. This checkpoint records a new exact unpaid stress family before the full argument is expanded.

Let

\[
R=\frac12\begin{pmatrix}
1&1&1\\
1&-1&1\\
1&1&-1\\
1&-1&-1
\end{pmatrix},\qquad
B=\begin{pmatrix}0&-1&0\\-1&0&0\\0&0&1\end{pmatrix},\qquad A=RBR^T.
\]

Then `R^T R=I_3`, `spec_nonzero(A)={1,1,-1}`, and explicitly

\[
A=\frac14\begin{pmatrix}
-1&1&-3&-1\\
1&3&-1&1\\
-3&-1&-1&1\\
-1&1&1&3
\end{pmatrix}.
\]

Thus all physical entries are nonzero and the family is genuinely shared-coordinate/nonseparable. Take independent `X_i~Unif[-1/2,1/2]`, so every input density has cap exactly one. For `y=R^T X`, the exact product-provenance marginal inherited from the physical cube is

\[
\rho(y)=2(1-M_1(y)-M_2(y))_+,
\]

where `M_1>=M_2>=M_3` are the ordered coordinate absolute values. The quadratic form is

\[
Q=y^TBy=y_3^2-2y_1y_2.
\]

Set `u=(y_1+y_2)/sqrt(2)`, `v=(y_1-y_2)/sqrt(2)`, `z=y_3`; then `Q=v^2+z^2-u^2`. On the cone `Q=0`, write `u=sigma r`, `v=r cos theta`, `z=r sin theta`. The absolute coordinate multiset in the original `y` coordinates is

\[
r\left\{\frac{1+|\cos\theta|}{\sqrt2},\frac{1-|\cos\theta|}{\sqrt2},|\sin\theta|\right\}.
\]

Because

\[
\sin^2\theta-\frac{(1-|\cos\theta|)^2}{2}
=\frac{(1-|\cos\theta|)(1+3|\cos\theta|)}2\ge0,
\]

the two largest magnitudes have sum

\[
h(\theta)=\frac{1+|\cos\theta|}{\sqrt2}+|\sin\theta|.
\]

The Lorentz coarea element on either cone nappe is `(1/2) dr dtheta`, hence

\[
p_Q(0)=\int_0^{2\pi}\frac{d\theta}{h(\theta)}
=4\int_0^{\pi/2}\frac{d\theta}{(1+\cos\theta)/\sqrt2+\sin\theta}
=4\log(1+\sqrt2).
\]

Numerically this is `3.525494348078...`, strictly above both `pi` and the previous axis-Hadamard value `8(sqrt(2)-1)=3.313708498985...`, but below `3sqrt(2)=4.242640687119...`.

Remaining step for this run: prove zero is the GLOBAL mode on both one-sheet and two-sheet sides by pointwise monotonicity of the exact product-provenance kernel, then apply the completed account02/B17 uniform diffuse-bank theorem and the newest-Claude one-sheet theorem to actual inequalities for this same matrix.
