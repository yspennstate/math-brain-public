# Independent checks and attempts to break the result

All checks are analytic. No numerical eigenvalue or nonlinear trajectory
is claimed.

## 1. A second derivation of the Gaussian residual

PROOF.md first integrates W to obtain H(x), then integrates X to obtain h(w).
An independent route integrates the two kernels directly:

\[
 h(w)=\mathbb E_V K(1,V)K(V,w)
 =e^{-(1+w^2)/2}\mathbb E_V[e^{-V^2}\sinh V\sinh(wV)].
\]

Using `2 sinh u sinh v = cosh(u+v)-cosh(u-v)` and
`E exp(-V^2+tV)=exp(t^2/6)/sqrt(3)` gives

\[
 h(w)=\frac{e^{-(1+w^2)/2}}{2\sqrt3}
 [e^{(1+w)^2/6}-e^{(1-w)^2/6}]
 =\frac{e^{-(1+w^2)/3}}{\sqrt3}\sinh(w/3).
\]

This confirms the factor `1/sqrt(3)`, the variance denominator 3, and
the argument `w/3` in (7). At w=1 this gives
`h(1)=(exp(-1/3)-exp(-1))/(2sqrt(3))=J`, independently of the squared-g
integration in PROOF.md.

The predictor norm can also be integrated exactly from (12):

\[
 \|H\|^2=\frac{e^{-1/2}}{4\sqrt2}(1-e^{-1/4})>0.
\]

Indeed the weighted Gaussian has variance 1/2, and
`sin^2(X/2)=(1-cos X)/2`. The risk identity is therefore exactly
`R(rho_eta)-R(pi)=-eta J+eta^2 exp(-1/2)(1-exp(-1/4))/(8sqrt(2))`.
The simpler inequality in (6) follows independently from Cauchy--Schwarz;
no decimal constants are needed.

## 2. KL and moment checks without a change-of-density calculation

The w marginal is unchanged, and the conditional output law moves from
`N(0,1)` to `N(eta g(w),1)`. The chain rule for relative entropy and the
one-dimensional Gaussian shift formula give `KL=eta^2 J/2`, reproducing
(10). The shift formula itself follows by integrating
`eta a g(w)-eta^2 g(w)^2/2` under that conditional Gaussian.
The construction with independent B,W gives
`E(B+eta g(W))^2=1+eta^2 J` directly, as `E B=0`.
Adding `E W^2=1` checks the total moment. Neither law nor these bounds
depends on lambda.

## 3. Unique zero without using the power-series test

The ratio h/g follows also by dividing their two exponential differences.
To recheck its monotonicity, put
`N(w)=w[1+2cosh(2w/3)]-4sinh(2w/3)`.
Direct differentiation gives

\[
 N(0)=0,\quad N'(0)=1/3,\quad
 N''(w)=\tfrac89\sinh(2w/3)+\tfrac{8w}9\cosh(2w/3)>0
 \quad(w>0).
\]

Thus N(w)>0, independently of the positive-coefficient expansion (19).
The ratio starts below one and diverges, so for every fixed eta in (0,1]
there is exactly one positive crossing. Negative residual values are not
an artifact of truncation, numerical underflow or a signed probability law.
Both g and h are positive for positive w; h has the slower Gaussian decay.

## 4. Exponent checked by the exact one-dimensional capacity

The linear interpolation in the proof need not be optimal. Choose fixed
`ell<r_eta<u` so that the left well maximum lies below ell, and the right
well maximum lies above u. Write q_lambda for the folded Lebesgue density,
and define

\[
 I_\lambda=\int_\ell^u\frac{dr}{q_\lambda(r)}.
\]

Among all cutoffs equal to 1 below ell and 0 above u, the derivative
`v'(r)=-1/[I_lambda q_lambda(r)]` on the bridge has energy exactly
`1/I_lambda`. Cauchy--Schwarz shows it is the minimizing derivative:
`1=(int_ell^u -v')^2 <= (int v'^2 q_lambda) I_lambda`.

The elementary Laplace bound (upper bound by the maximum, lower bound
on a neighborhood of a maximizer) gives

\[
 \begin{split}
 \lambda^2\log Z&\longrightarrow M_\eta^2/2,\\
 \lambda^2\log q_\lambda([0,\ell])
 &\longrightarrow(A_\eta^2-M_\eta^2)/2,\\
 \lambda^2\log q_\lambda([u,\infty))
 &\longrightarrow(B_\eta^2-M_\eta^2)/2.
 \end{split}
\]

For the last integral the unbounded tail causes no problem: the upper
bound uses total Gaussian mass one, and a compact neighborhood of its
attained maximum supplies the lower bound.
On the finite bridge, `1/q_lambda(r)` is Z times a fixed positive continuous
factor times `exp(-G_eta(r)^2/(2lambda^2))`. Its minimum potential is zero,
attained at r_eta. Its integral after dividing by Z therefore has logarithm
times lambda squared tending to zero. Thus
`lambda^2 log I_lambda -> M_eta^2/2`.

The test variance is at least the product of the two exterior masses.
Its Rayleigh quotient consequently has upper logarithmic exponent

\[
 -M_\eta^2/2-(A_\eta^2+B_\eta^2-2M_\eta^2)/2
 =-\min(A_\eta^2,B_\eta^2)/2.
\]

This reproduces (9) with a different, density-adapted transition function.
It also identifies the common mistake that would give the deeper-well
height: ignoring the exponentially small variance when one well is rare.

The lower comparison bound is checked against the original proof: the
oscillation of `G_eta^2/(2lambda^2)` is at most `M_eta^2/(2lambda^2)`;
the shear costs its squared derivative norm. No factor of lambda from
physical time enters a static Poincare constant. Multiplying the generator
by lambda would multiply a relaxation rate by lambda, which does not change
this logarithmic scale and does not supply a learning-time lower bound.

## 5. Prediction check by a second perturbation

Use the sharp gate `v_0(r)=1_{r<r_eta}`, only for this independent
prediction check; it need not have finite Sobolev energy. Let p_L,p_R
be the positive folded masses on the two sides. The derivative at x=0
of its centered predictor perturbation is

\[
 \lambda^{-1}\operatorname{Cov}_{q_\lambda}
 (rG_\eta(r),1_{r<r_\eta})
 =\lambda^{-1}p_Lp_R
 [\mathbb E_L(rG_\eta(r))-\mathbb E_R(rG_\eta(r))]>0.
\]

The conditional expectations have strictly opposite signs. Differentiation
is justified by finite `int r |G_eta(r)| q_lambda(dr)`; the marginal has
Gaussian tails for fixed lambda. The linear cutoffs converge pointwise to
this gate as s decreases to zero. Dominated convergence gives convergence
of the covariance and hence a nonzero derivative for every sufficiently
small s at fixed lambda. This confirms prediction visibility without
Fourier uniqueness. PROOF.md uses Fourier uniqueness to prove the stronger
claim for every permitted strip width s.

For a nonzero predictor change V, the two risks at opposite perturbations
cannot both equal the unperturbed risk: their sum differs by `t^2 ||V||^2`.
The factor 1/2 in squared loss is accounted for. This proves a change in
risk for at least one sign, not a quantitative lower bound on that change.

## 6. Cases that might invalidate an interpretation

- At eta=0 there is no negative lobe. The old polynomial restricted-gap
  result is consistent with this theorem, whose exponent depends on eta.
  In fact `B_eta <= eta sup h`, since `-G_eta=eta h-g` on the positive
  half-line. Thus D_eta tends to zero as eta tends to zero. No uniform
  nonzero barrier at eta=0 is asserted.
- Both lobes can have unequal depths. The proof retains their two masses,
  and the exponent is the smaller squared height, not the larger one.
- The rare well may have exponentially small mass and an exponentially
  small effect on predictions. Nonzero visibility does not establish an
  order-one or epsilon-sized risk obstruction.
- The law rho_eta is a positive Gaussian conditional shear, with finite KL
  and bounded moments. It is an explicit nearby law, not an evolved MFLD
  law. Freezing the initialization residual and omitting hidden-weight
  motion is precisely what would produce this shear; neither omission is
  justified for the actual trajectory.
- All cutoffs are functions of |w| and already S-invariant. Removing the
  odd sector cannot remove this mode. The origin w=0 is outside the
  transition strip, so its absolute-value coordinate creates no cusp.
- The construction keeps a fixed Gaussian prior as lambda changes. The
  scale need not agree with a temperature-independent L2 penalty.
- A static proximal inequality, even with prediction visibility, does not
  bound the nonlinear learning time from pi or under annealing. That
  implication has not been made.

No defect was found in the theorem as stated. The principal unresolved
condition is whether the changing residual on the actual trajectory
develops a quantitatively relevant secondary lobe.
