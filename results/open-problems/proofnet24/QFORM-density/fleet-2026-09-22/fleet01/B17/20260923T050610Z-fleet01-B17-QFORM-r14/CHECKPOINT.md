# Early substantive checkpoint — arbitrary weighted rank-one banks

Full QFORM remains **OPEN**. This checkpoint attacks an unpaid exact target family.

Let `a=(a_1,...,a_m)` satisfy `sum a_i^2=1`, let `U_i,V_i` be iid `Unif[-1/2,1/2]`, and put

\[
S_a=\sum_i a_iU_i,\qquad T_a=\sum_i a_iV_i.
\]

The physical matrix

\[
A_a=\operatorname{diag}(1,aa^T,-aa^T)
\]

has nonzero spectrum exactly `{1,1,-1}` for every finite `m`; all inputs remain independent in the physical coordinates.

Write `h` for the density of `S_a`. It is even and nonincreasing on `[0,\infty)` (convolution of scaled centered intervals). Ball's cube-slicing theorem applied to the unit coefficient vector `a` gives

\[
\|h\|_\infty\le\sqrt2.
\tag{1}
\]

There is a second norm bound that appears not to have been used in the preceding B17 branch. Since

\[
\|h\|_2^2=p_{S_a-S_a'}(0)
\]

and `(S_a-S_a')/\sqrt2` is a linear image of `2m` centered unit intervals with coefficient vector `(a,-a)/\sqrt2` of Euclidean norm one, Ball again gives

\[
\boxed{\|h\|_2^2\le1.}
\tag{2}
\]

For a centered unit-interval heavy coordinate `U`, polar coordinates give the exact central formula

\[
C(a):=p_{U^2+S_a^2-T_a^2}(0)
=4\int_0^{\pi/2}\int_0^{1/(2\cos\theta)}h(r\sin\theta)h(r)\,dr\,d\theta.
\tag{3}
\]

Extending the inner integral to infinity and using (1) gives

\[
J(\theta):=\int_0^\infty h(r\sin\theta)h(r)dr\le \frac1{\sqrt2}.
\tag{4}
\]

Cauchy--Schwarz and (2) give the complementary estimate

\[
J(\theta)\le\frac{1}{2\sqrt{\sin\theta}}.
\tag{5}
\]

Hence

\[
C(a)\le4\left[\frac{\pi}{6\sqrt2}+\frac12\int_{\pi/6}^{\pi/2}(\sin\theta)^{-1/2}d\theta\right].
\tag{6}
\]

Using concavity `sin theta >=2 theta/pi` on `[0,pi/2]`,

\[
\boxed{
C(a)\le B_0:=2\pi\left(1-\frac1{\sqrt3}+\frac1{3\sqrt2}\right).
}
\tag{7}
\]

This is strictly below `3sqrt(2)` by a completely elementary certificate: `pi<22/7`, `1/sqrt3>4/7`, and `1/(3sqrt2)<6/25`, so

\[
B_0<\frac{5148}{1225}<3\sqrt2,
\]

the last inequality following after squaring from `26,501,904 < 27,011,250`.

The remaining step for the final report is to transfer the designated fleet02/B17 exact heavy-law extremizer mechanism from equal banks to this arbitrary-weight bank. The needed hypotheses survive: `h` is even decreasing, so the density of `S_a^2-T_a^2` is even decreasing in absolute value. The partner's bathtub/two-shell stochastic comparison plus its symmetric-unimodal mode theorem can therefore be applied verbatim after writing out the hypotheses. If this transfer closes, every arbitrary cap-one heavy singleton law and every output level in the whole weighted family is bounded by (7), settling all intermediate finite `m` in the partner sequence at once.
