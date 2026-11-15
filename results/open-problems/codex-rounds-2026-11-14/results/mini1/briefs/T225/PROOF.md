# A sharp proximal LSI obstruction with a fixed Gaussian prior

The result concerns a proximal Gibbs measure, not a lower bound on the time
needed by the nonlinear dynamics to reach small prediction risk.

## 1. Regression model and statement

Let the input be `X ~ N(0,1)`, let the activation be `sigma(z)=sin(z)`, and let
the teacher be `y(X)=sin(X)`. For a probability law rho on `(a,w) in R^2`, set

\[
 f_\rho(x)=\int a\sin(wx)\,d\rho(a,w),\qquad
 R(\rho)=\frac12\mathbb E[(f_\rho(X)-\sin X)^2].
\]

Take the fixed prior `pi = N(0,I_2)` and

\[
 F_\lambda(\rho)=R(\rho)+\lambda\operatorname{KL}(\rho\Vert\pi),
 \qquad \lambda>0.
\]

This is a smooth, one-neuron realizable regression problem with both teacher
weights equal to one. In particular, `inf R=0`. The same infimum holds among
laws with finite KL: the independent Gaussian law
`a ~ N(1,s^2), w ~ N(1,s^2)` has predictor
`exp(-s^2 x^2/2) sin(x)`, which tends to `sin(x)` in input L2 as `s` tends to
zero, by dominated convergence. Its KL relative to pi is finite for `s>0`.
Also `F_lambda >= 0`; no negative-entropy escape is involved.

For a probability measure mu, write alpha(mu) for its best log-Sobolev
constant in the convention

\[
 \operatorname{Ent}_\mu(h^2)
 \leq \frac{2}{\alpha(\mu)}\int\|\nabla h\|^2\,d\mu.
 \tag{1}
\]

Here `Ent_mu(k)=int k log(k) dmu - (int k dmu) log(int k dmu)`.
Write beta(mu) for its best Poincare constant, with
`Var_mu(h) <= beta(mu)^(-1) int ||grad h||^2 dmu`.

Define

\[
 g(w)=\mathbb E[\sin X\sin(wX)]
 =\frac{e^{-(w-1)^2/2}-e^{-(w+1)^2/2}}2
 =e^{-(1+w^2)/2}\sinh w,
 \qquad M=\max_{w\in\mathbb R}|g(w)|>0.
 \tag{2}
\]

At the initialization `rho_0=pi`, the proximal Gibbs measure is

\[
 p_\lambda(da,dw)
 =Z_\lambda^{-1}e^{a g(w)/\lambda}\,\pi(da,dw).
 \tag{3}
\]

**Theorem.** For this measure,

\[
 \boxed{\lim_{\lambda\downarrow0}\lambda^2\log\alpha(p_\lambda)
 =\lim_{\lambda\downarrow0}\lambda^2\log\beta(p_\lambda)
 =-\frac{M^2}{2}.}
 \tag{4}
\]

The maximum in (2) occurs at `w=+w_*` and `w=-w_*`, where `w_*>0` is the
unique positive solution of

\[
 w_*\tanh w_*=1.
 \tag{5}
\]

In particular, even at Gaussian initialization there cannot be constants
`c,C>0` independent of lambda such that
`alpha(p_lambda) >= c exp(-C/lambda)` for all small lambda. The same conclusion
holds for any uniform lower bound over proximal Gibbs measures that includes
this initialization.

## 2. Identifying the proximal measure

The prior has `f_pi=0` because its output weight a is centered and independent
of w. For the half squared loss, a representative of the first variation is

\[
 \frac{\delta R}{\delta\rho}(a,w)
 =\mathbb E[(f_\rho(X)-\sin X)a\sin(wX)].
\]

At pi this equals `-a g(w)`. The proximal Gibbs law is, by definition,
proportional to `exp(-(delta R/delta rho)/lambda) pi`, proving (3). Formula
(2) follows from `sin(u)sin(v)=(cos(u-v)-cos(u+v))/2` and
`E cos(tX)=exp(-t^2/2)`.

The function g is odd, tends to zero at both infinities, and is positive on
`w>0`. It has bounded derivative: differentiating its defining expectation,

\[
 |g'(w)|=|\mathbb E[X\sin X\cos(wX)]|
 \leq\sqrt{\mathbb E X^2\,\mathbb E\sin^2 X}\leq1.
 \tag{6}
\]

For `w>0`, direct differentiation of (2) gives

\[
 g'(w)=e^{-(1+w^2)/2}(\cosh w-w\sinh w).
\]

The function `w tanh(w)` is strictly increasing from zero to infinity on the
positive half-line, since its derivative is `tanh(w)+w sech(w)^2>0`.
Thus g increases up to the unique root (5) and decreases thereafter. Its
positive maximum exists and is M.

## 3. Square completion and a matching LSI lower bound

The following argument applies more generally to any bounded, odd C1 function
g with `M=sup |g|>0` and `L=sup |g'|<infinity`.

Completing the square gives the exact identity

\[
 -\frac{a^2+w^2}{2}+\frac{a g(w)}\lambda
 =-\frac{(a-g(w)/\lambda)^2}{2}-\frac{w^2}{2}
   +\frac{g(w)^2}{2\lambda^2}.
 \tag{7}
\]

Consequently, conditional on w, a is Gaussian with mean `g(w)/lambda` and
variance one. The w marginal is

\[
 \nu_\lambda(dw)=Z_\lambda^{-1}
   \exp\!\left(\frac{g(w)^2}{2\lambda^2}\right)\gamma(dw),
 \quad
 Z_\lambda=\int\exp\!\left(\frac{g(w)^2}{2\lambda^2}\right)\gamma(dw),
 \tag{8}
\]

where gamma is the standard one-dimensional Gaussian. In particular Z is
finite. Let `mu_lambda=gamma(db) tensor nu_lambda(dw)`. Then

\[
 T_\lambda(b,w)=(b+g(w)/\lambda,w),\qquad
 (T_\lambda)_\#\mu_\lambda=p_\lambda.
 \tag{9}
\]

We give the needed density comparison explicitly. Suppose a probability
measure mu has density r relative to a probability measure eta, and
`0<m<=r<=B<infinity`. For `s>=0, c>0`, put
`Psi(s,c)=s log(s/c)-s+c`, with the continuous convention at zero. This is
nonnegative, and direct minimization over c proves

\[
 \operatorname{Ent}_\mu(k)=\inf_{c>0}\int\Psi(k,c)\,d\mu.
\]

It follows that `Ent_mu(h^2)<=B Ent_eta(h^2)`. If eta satisfies (1) with
constant alpha_eta, then

\[
 \operatorname{Ent}_\mu(h^2)
 \leq\frac{2B}{\alpha_\eta}\int\|\nabla h\|^2d\eta
 \leq\frac{2B}{m\alpha_\eta}\int\|\nabla h\|^2d\mu.
 \tag{10}
\]

For mu_lambda relative to the standard two-dimensional Gaussian, the density
is `exp(g(w)^2/(2 lambda^2))/Z_lambda`. Since `0<=g^2<=M^2`, its supremum to
infimum ratio is at most `exp(M^2/(2 lambda^2))`. The standard Gaussian LSI
has constant one (a derivation is supplied in Section 7). Equation (10) gives

\[
 \alpha(\mu_\lambda)\geq e^{-M^2/(2\lambda^2)}.
\]

The derivative of T is the identity plus a matrix of operator norm at most
`L/lambda`, so `||DT_lambda||_op<=1+L/lambda`. Apply the last LSI to
`h composed with T_lambda`, and use the chain rule and (9), to obtain

\[
 \boxed{\alpha(p_\lambda)\geq
   \frac{e^{-M^2/(2\lambda^2)}}{(1+L/\lambda)^2}.}
 \tag{11}
\]

Since `lambda^2 log(1+L/lambda)` tends to zero,

\[
 \liminf_{\lambda\downarrow0}\lambda^2\log\alpha(p_\lambda)
 \geq-M^2/2.
 \tag{12}
\]

## 4. Matching bottleneck upper bound

Fix `0<delta<M/2`. By the definition of M and continuity, there is a bounded
interval `I` in the positive half-line with `gamma(I)>0` on which
`|g(w)|>=M-delta`. This uses oddness to choose the positive half-line if
necessary. Since `g(0)=0`, choose `r>0` so small that I lies outside `[-r,r]`
and `sup_{|w|<=r}|g(w)|<=delta`. Equation (8) gives

\[
 q_\lambda:=\nu_\lambda([-r,r])
 \leq\frac{\gamma([-r,r])}{\gamma(I)}
 \exp\!\left(-\frac{(M-\delta)^2-\delta^2}{2\lambda^2}\right).
 \tag{13}
\]

In particular `q_lambda` tends to zero. Take the odd, piecewise linear test
function

\[
 h_r(w)=\begin{cases}-1&w\leq-r,\\w/r&|w|<r,\\1&w\geq r.\end{cases}
\]

The marginal nu_lambda is even, so this test has mean zero under p_lambda.
Furthermore,

\[
 \operatorname{Var}_{p_\lambda}(h_r)\geq1-q_\lambda,
 \qquad
 \int\|\nabla h_r\|^2dp_\lambda=r^{-2}q_\lambda.
 \tag{14}
\]

The use of a Lipschitz test is legitimate: convolve h_r with a smooth even
mollifier, then let its width tend to zero. The functions remain odd and
bounded; their derivatives are bounded by `1/r` and converge almost
everywhere. The marginal has a smooth density in this example, so dominated
convergence gives both quantities in (14).

An LSI with constant alpha implies the Poincare inequality with the same
constant. Indeed insert `1+s h` into (1) for bounded mean-zero h: its entropy
is `2s^2 int h^2 dmu+o(s^2)`, and its energy is
`s^2 int ||grad h||^2 dmu`; divide by `2s^2` and let s tend to zero.
Consequently,

\[
 \alpha(p_\lambda)\leq\beta(p_\lambda)
 \leq\frac{q_\lambda}{r^2(1-q_\lambda)}.
 \tag{15}
\]

Using (13), taking logarithms and multiplying by `lambda^2` yields

\[
 \limsup_{\lambda\downarrow0}\lambda^2\log\beta(p_\lambda)
 \leq-\frac{(M-\delta)^2-\delta^2}{2}
 =-M^2/2+M\delta.
\]

Let delta decrease to zero and combine with (12) and `alpha<=beta`. This
proves both limits in (4). If `alpha>=c exp(-C/lambda)` held, its logarithm
multiplied by `lambda^2` would have lower limit at least zero, contradicting
(4).

## 5. Why this does not give a prediction-risk lower bound

Let `S(a,w)=(-a,-w)`. Both pi and p_lambda are invariant under S. However,
the feature itself is invariant:

\[
 (-a)\sin((-w)x)=a\sin(wx).
 \tag{16}
\]

The bottleneck test `h_r(w)` changes sign under S. For any `|eta|<1`, define

\[
 d\rho_\eta=(1+\eta h_r(w))\,dp_\lambda.
\]

This is a probability measure, since the h_r mean is zero, and its density is
positive. For every x, the integral of `a sin(wx) h_r(w)` against p_lambda
vanishes: changing variables by S negates the integrand and preserves the
measure. All integrals are finite by (7). Therefore

\[
 f_{\rho_\eta}(x)=f_{p_\lambda}(x),\qquad
 R(\rho_\eta)=R(p_\lambda).
 \tag{17}
\]

Thus the explicit mode used for the sharp upper bound has exactly zero
projection onto every prediction feature. Slow relaxation of that mode is
insufficient to prove slow learning. Also, p_lambda is the proximal law at
rho_0=pi, not a demonstrated equilibrium of the self-consistent dynamics.

## 6. Temperature convention

The prior in this result is fixed as lambda decreases. Thus

\[
 \lambda\operatorname{KL}(\rho\Vert\pi)
 =\lambda\int\rho\log\rho
  +\frac\lambda2\int(a^2+w^2)d\rho+\lambda\log(2\pi)
\]

for a Lebesgue density rho. The quadratic penalty coefficient also decreases
with temperature. This is the convention in the stated objective with fixed
Gaussian pi.

For comparison, if the objective instead contains a fixed quadratic penalty
`kappa(a^2+w^2)/2` plus `lambda` times Lebesgue entropy, completing the square
in the proximal exponent gives

\[
 -\frac{\kappa a^2}{2\lambda}+\frac{a g(w)}\lambda
 =-\frac\kappa{2\lambda}(a-g(w)/\kappa)^2
  +\frac{g(w)^2}{2\kappa\lambda}.
\]

That has a different temperature scale. The theorem makes no assertion of
the same `1/lambda^2` asymptotic under this alternative convention.

## 7. Gaussian LSI used in Section 3

For completeness, let gamma_n be standard Gaussian and let
`P_t k(x)=E[k(e^(-t)x+sqrt(1-e^(-2t)) Z)]`, `Z~gamma_n`, be its
Ornstein–Uhlenbeck semigroup. Its generator is `Delta-x dot grad` and its
invariant law is gamma_n, as follows directly from sums of independent
Gaussians. For smooth bounded positive k bounded away from zero, Gaussian
integration by parts gives

\[
 -\frac d{dt}\operatorname{Ent}_{\gamma_n}(P_t k)
 =\int\frac{\|\nabla P_t k\|^2}{P_t k}\,d\gamma_n.
\]

Differentiating the explicit formula for P_t gives
`grad P_t k=e^(-t) P_t grad k`. Cauchy–Schwarz inside the expectation implies

\[
 \frac{\|\nabla P_t k\|^2}{P_t k}
 \leq e^{-2t}P_t\left(\frac{\|\nabla k\|^2}{k}\right).
\]

As t tends to infinity, P_t k tends pointwise to its Gaussian mean and its
entropy tends to zero by bounded convergence. Integrating the last two
formulas, using invariance and `int_0^infinity e^(-2t)dt=1/2`, gives

\[
 \operatorname{Ent}_{\gamma_n}(k)
 \leq\frac12\int\frac{\|\nabla k\|^2}{k}\,d\gamma_n.
\]

Apply this to `k=h^2+u`, `u>0`, and let u decrease to zero. Since
`||grad k||^2/k<=4||grad h||^2`, bounded convergence for entropy gives
`Ent_gamma_n(h^2)<=2 int ||grad h||^2 dgamma_n`. Smooth approximation and
truncation extend this inequality to the bounded C1 and Lipschitz functions
with bounded gradients used above. This proves the Gaussian LSI input with
constant one.
