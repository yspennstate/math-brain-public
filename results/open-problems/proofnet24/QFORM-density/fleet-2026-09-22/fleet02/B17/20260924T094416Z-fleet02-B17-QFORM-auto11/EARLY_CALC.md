# QFORM fleet02/B17 early calculation — tetrahedral tight-frame Poisson stress

Run: `20260924T094416Z-fleet02-B17-QFORM-auto11`.

Target remains the unrestricted cap-one product-law quadratic-form density problem. This note is only the early calculation for a source-valid witness family; it is not a proof of full QFORM.

Let
\[
t_1=(1,1,1)/\sqrt3,\quad t_2=(1,-1,-1)/\sqrt3,\quad
t_3=(-1,1,-1)/\sqrt3,\quad t_4=(-1,-1,1)/\sqrt3.
\]
Then
\[
\sum_{a=1}^4 t_at_a^T=\frac43I_3.
\]
For `m>=2`, put `m` physical rows in each of the four directions,
\[
r_{a,k}=\sqrt{\frac{3}{4m}}\,t_a,
\]
and let `T_m` be the `4m x 3` matrix with these rows. Hence
\[
T_m^TT_m=I_3,\qquad \|r_{a,k}\|^2=\frac{3}{4m}<\frac12.
\]
Take the dense reflection
\[
B=I_3-2nn^T,\qquad n=(1,2,3)^T/\sqrt{14}
=\frac17\begin{pmatrix}6&-2&-3\\-2&3&-6\\-3&-6&-2\end{pmatrix},
\]
so `spec(B)={1,1,-1}`. Define the physical matrix `A_m=T_m B T_m^T`. Its nonzero spectrum is exactly `{1,1,-1}`. Moreover the 4-by-4 table of group coefficients `t_a^T B t_b` is
\[
\begin{pmatrix}
-5/7&17/21&5/21&-1/3\\
17/21&5/21&-5/7&-1/3\\
5/21&-5/7&17/21&-1/3\\
-1/3&-1/3&-1/3&1
\end{pmatrix},
\]
so every physical entry of `A_m` is nonzero. This is therefore an entrywise-dense exact target matrix, not a diagonal-basis independence surrogate.

For fixed `lambda_a>0`, `R_a>0`, and `m>lambda_a`, use on each physical coordinate in direction group `a` the cap-one density
\[
f_{a,m}(x)=\mathbf1_{[-\ell_{a,m}/2,\ell_{a,m}/2]}(x)
+\mathbf1_{[R_a\sqrt m-\lambda_a/(4m),R_a\sqrt m+\lambda_a/(4m)]}(x)
+\mathbf1_{[-R_a\sqrt m-\lambda_a/(4m),-R_a\sqrt m+\lambda_a/(4m)]}(x),
\]
where `ell_{a,m}=1-lambda_a/m`. The support lengths sum exactly to one, hence `f_{a,m}` is a probability density with pointwise cap one. Its remote gap is order `sqrt(m)`.

Let `Y_m=T_m^T X`. For a fixed test vector `xi`, one coordinate in group `a` contributes, with `u=sqrt(3/(4m)) <xi,t_a>`,
\[
\chi_{a,m}(\xi)
=\ell_{a,m}\,\operatorname{sinc}(u\ell_{a,m}/2)
+\frac{\lambda_a}{m}\,\operatorname{sinc}(u\lambda_a/(4m))
\cos\!\left(\frac{\sqrt3}{2}R_a\langle\xi,t_a\rangle\right).
\]
Since `u^2=(3/(4m))<xi,t_a>^2`, for fixed `xi`
\[
\chi_{a,m}(\xi)
=1+\frac1m\left[\lambda_a(\cos(c_a\langle\xi,t_a\rangle)-1)
-\frac1{32}\langle\xi,t_a\rangle^2\right]+o(m^{-1}),
\qquad c_a=\frac{\sqrt3}{2}R_a.
\]
Thus the `m` coordinates in group `a` converge to a Gaussian-plus-symmetric-Poisson exponent. Multiplying the four groups and using `sum_a t_at_a^T=(4/3)I` gives
\[
\mathbb E e^{i\langle\xi,Y_m\rangle}
\to
\exp\left(-\frac{|\xi|^2}{24}
+\sum_{a=1}^4\lambda_a[\cos(c_a\langle\xi,t_a\rangle)-1]\right).
\]
Equivalently,
\[
Y_m\Rightarrow G+M,
\quad G\sim N(0,I_3/12),
\]
where `G` is independent of
\[
M=\sum_{a=1}^4c_a(N_{a,+}-N_{a,-})t_a,
\qquad N_{a,\pm}\stackrel{ind}{\sim}\mathrm{Poisson}(\lambda_a/2).
\]
The jump directions are four non-collinear tight-frame directions, so this is not an axis-bank construction.

The array is genuinely non-Lindeberg: for any fixed threshold smaller than `c_a`, the aggregate quadratic tail contribution from group `a` tends to `lambda_a c_a^2>0`. Hence an ordinary triangular-array Gaussian CLT cannot remove the macroscopic jump component.

Next step: apply the pinned Fresnel–Brascamp–Lieb theorem to the actual finite physical frame to obtain a common `L^1` Fourier envelope, upgrade the weak limit to uniform convergence of output densities, then apply the latest fleet03/B17 Gaussian full-target comparator to the random-location limit.
