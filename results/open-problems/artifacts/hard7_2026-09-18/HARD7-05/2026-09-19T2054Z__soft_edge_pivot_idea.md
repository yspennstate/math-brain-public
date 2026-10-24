Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# HARD7-05 route pivot — spend edge-covariance slack by adding independent Gaussian noise

This note records the structural pivot before the exact repository checker is installed.

The first B15 attack in this run replaced `U_j+U_{j-1}` by `U_j+aU_{j-1}`. For fixed `0<r<1` its covariance prefactor is

\[
A(a,r)=\frac{(r+a)(1+ar)}{1+a^2+2ar}.
\]

The exact identity

\[
\frac{1+r}{2}-A(a,r)
=\frac{(1-r)(a-1)^2}{2(1+a^2+2ar)}\ge0
\]

shows that the symmetric weight `a=1` maximizes this prefactor. Asymmetry can spend the available covariance slack, but it also makes the survival operator non-self-adjoint. Exploratory quadrature was used only as route selection and suggested that this nonnormal penalty erases the potential gain; no numerical value from that exploration is promoted as a theorem.

A cleaner B6/B11/B15 deformation spends the same slack **without losing self-adjointness**. Let `(U_j)` be stationary Gaussian AR(1), `Cov(U_0,U_k)=r^{|k|}`, let `(E_j)` be iid standard normal independent of `U`, and put

\[
Y_j=\frac{U_j+U_{j-1}}{\sqrt{2(1+r)}},\qquad
Z_j=\sqrt{s}\,Y_j+\sqrt{1-s}\,E_j,\qquad 0<s<1.
\]

Then `Var(Z_j)=1` and for `k>=1`

\[
\operatorname{Cov}(Z_0,Z_k)
=s\frac{1+r}{2}r^{k-1}.
\]

Thus `s` independently lowers every nonzero-lag covariance while leaving the AR mesh parameter `r` fixed. The finite source comparison can use precisely the slack already visible at `r=7/8`.

Conditional on an AR edge `(x,y)`, the probability of the noisy edge event is

\[
w_{r,s}(x,y)
=\Phi\!\left(-\sqrt{\frac{s}{1-s}}\frac{x+y}{\sqrt{2(1+r)}}\right).
\]

Hence the transfer operator is

\[
(K_{r,s}f)(x)=\int p_r(x,dy)\,w_{r,s}(x,y)f(y).
\]

Because `w_{r,s}(x,y)=w_{r,s}(y,x)` and the AR kernel satisfies Gaussian detailed balance, `K_{r,s}` is again self-adjoint. This avoids the main obstruction of the asymmetric route.

There is also a useful fourth-trace comparison. In the cyclic Gaussian representation of `tr(K_{r,s}^4)`, let `S_i=(X_i+X_{i+1})/sqrt(2(1+r))`. Under the normalized cyclic AR law all pairwise covariances of the four `S_i` are positive (the cyclic vertex covariance is `G_d=(r^d+r^{4-d})/(1-r^4)`). Replacing each `S_i` by `sqrt(s) S_i+sqrt(1-s)E_i` preserves centering and strictly reduces every standardized off-diagonal correlation. Gaussian comparison for the negative orthant therefore gives

\[
\operatorname{tr}(K_{r,s}^4)\le \operatorname{tr}(K_{r,1}^4).
\]

So the previously certified hard-edge fourth-trace cap at the same `r` remains valid, while the softened operator has smaller survival.

The concrete rational point selected for exact certification is

\[
r=q=\frac78,\qquad s=\frac{199}{200},\qquad
c:=s\frac{1+r}{2}=\frac{597}{640}.
\]

At this point the source covariance comparison has a small but positive exact margin, the tail comparison still has `c/r=597/560>1`, and the two-edge moment calculation remains algebraic because the adjacent noisy-edge correlation is the rational `597/640`. The exact checker will test whether this route is strong enough to move the frozen endpoint from `8071/50000` to the clean candidate `41/250`.

Methods remain **B6 / B11 / B15**: deform the comparator, dualize the spectral certificate through moments/trace, and break the hard-edge purity by independent noise rather than by asymmetric weights.
