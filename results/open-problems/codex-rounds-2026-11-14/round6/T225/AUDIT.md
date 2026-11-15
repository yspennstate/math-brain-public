# Independent checks and attempted counterexamples

## 1. Initial residual and loss normalization

The parameter-space density derivative is a ell_g(v) pi, since the
Gaussian OU contribution vanishes. Integrating it against a sin(vx)
and integrating by parts in v gives E[g(V)sin(Vx)+g'(V)x cos(Vx)].
In contrast, the earlier predictor calculation first integrates g sin
to obtain H, then obtains U=(1+x^2)H+xH'. Both give the same derivative.
Transforming H gives h, and transforming U gives -2h''-wh'. Thus the
reported coefficients 10,-2,5 in D are recovered without differentiating
the initial generator in time.

The independent loss check is parameter-gradient dissipation:
-dot R_0=E(g^2+g'^2). Gaussian MGF derivatives give

  E g^2=(exp(-1/3)-exp(-1))/(2sqrt(3)),
  E g'^2=(2exp(-1/3)+3exp(-1))/(9sqrt(3)).

Their sum is (13exp(-1/3)-3exp(-1))/(18sqrt(3)), also D(1).
The factor one half in the loss is therefore consistent.

## 2. Second derivative by differentiating the prediction kernel

For an input function r define

  T r(x)=E_V[<r,sin(V.)> sin(Vx)
                 +<r,X cos(VX)> x cos(Vx)].

At initialization T is the neural tangent operator. The predictor
equation has risk term T_{rho_t}(sin-f_t) and OU term
-lambda E_{rho_t}a[(1+x^2)sin(vx)+vx cos(vx)].

The first variation of T_{rho_t} at t=0 vanishes. Its two kernel
components involve no a and a^2, respectively; multiplying either by
dot rho_0/pi=a ell_g(v) gives zero Gaussian a expectation. Hence
the differentiated risk term is -T U. The differentiated OU term is
-lambda[(1+x^2)U+xU']. Therefore

  ddot f_0=-T U-lambda[(1+x^2)U+xU'].

After taking the negative sine transform, this is ddot G_0=E+lambda Z.
This route separately verifies the cancellation of the nonlinear
kernel variation, the sign, and the single copy of the temperature
term. The generator calculation in PROOF.md obtains these facts by
oddness and stationarity directly on L_0^2(aK).

## 3. Leading coefficient of E by input-space square completion

For odd input q, Gaussian trigonometric identities give

  Tq(x)=integral (1+xy) exp(-(x-y)^2/2) q(y) gamma(dy).

Indeed the full kernel is one half of
[(1+xy)exp(-(x-y)^2/2)+(xy-1)exp(-(x+y)^2/2)]; changing y to -y in
the second term gives the first term on odd functions.

Here

  U(y)=exp(-(1+y^2)/4)/sqrt(2)
        [(1+y^2/2)sin(y/2)+(y/2)cos(y/2)].

Completing the y square in T U leaves variance 2/5 and complex mean
2x/5+i/5. The common exponential factor is
exp(-3/10-3x^2/10)/sqrt(5), with phase x/5. The only degree-four
term comes from (xy)(y^2/2)sin(y/2); its coefficient is
(1/2)x(2x/5)^3=4x^4/125. Consequently the exact expression has form

  T U(x)=exp(-3/10-3x^2/10)/sqrt(5)
          [(4x^4/125+O(x^2))sin(x/5)+O(x^3)cos(x/5)],

where the O terms here denote polynomials of the indicated maximal
degrees, not asymptotic approximations to the Gaussian integral.

Taking its sine transform against gamma gives Gaussian Fourier
factor sqrt(5/8) exp(-5(w-1/5)^2/16) for the dominating branch.
Fourier transformation of x^4 contributes (5w/8)^4 to its leading
coefficient. Thus the leading coefficient of E is

  [4/(125sqrt(5))] [sqrt(5/8)/2] (5/8)^4
    =5/(4096sqrt(2)).

Its exponent is
-3/10-5(w-1/5)^2/16=-(5w^2-2w+5)/16.
These exactly match the parameter-space MGF calculation in PROOF.md.
The lower-degree cosine polynomial contributes degree at most three
in w and cannot cancel the positive degree-four leading term.

## 4. Coefficients in ell_D and the exact E formula

An independent single-branch calculation checks all coefficients.
Write the positive branch of D as

  p(v)exp(-(v^2-v+1)/3)/(18sqrt(3)), p=10+5v-2v^2.

For r=(-2v+1)/3, applying 1+v partial_v-partial_v^2 multiplies the
exponential by

  p(14+7v-10v^2)/9+p'(21v-6)/9-p''.

The numerator is
20v^4-64v^3-177v^2+269v+146. The negative branch recovers the
opposite parity coefficients. This verifies (23) in PROOF.md.

For M=exp(3b^2/16), with its constant prefactor suppressed, put c=3/8.
Then M'/M=cb, M''/M=c+c^2b^2,
M'''/M=3c^2b+c^3b^3, and M''''/M=3c^2+6c^3b^2+c^4b^4.
Substituting into 20M''''-177M''+146M and 269M'-64M''' gives

  A=405b^4/1024-297b^2/16+1409/16,
  C=-27b^3/8+591b/8.

This checks the full exact expression, including its cancellations at
w=0. Both branches are needed near zero; only the plus branch is used
for the asymptotic at positive infinity.

## 5. Temperature tail by an independent input calculation

Let A_input q=(1+x^2)q+xq'. Since H has Gaussian exponent -x^2/4,
U=A_input H has leading term x^2 H/2 and a lower-degree cosine term.
Applying A_input again gives leading term x^4 H/4.
The transform of H is h. The leading Fourier multiplier for x^4 is
(2w/3)^4. Therefore

  Z(w) ~ (1/4)(2/3)^4 w^4 h(w)
       ~ [2/(81sqrt(3))] w^4 exp(-(w^2-w+1)/3).

This independently verifies the sign and coefficient from applying
-2 partial_w^2-w partial_w directly to D.

At the teacher frequency there is another sign check. T is self-adjoint
and positive on input L2, so E(1)=<T U,sin>=<U,U>>0. Also (12) in
PROOF.md gives Z(1)=E ell_g(V)^2>0, since K(V,1)=g(V).
It follows independently that
ddot R_0=2||U||_2^2+lambda E ell_g(V)^2>0. This checks the signs of
both second-derivative contributions without a tail calculation.

## 6. Third derivative operator order and moment requirements

For any fixed test phi, m'=E L phi and m''=E(L^2+dot L)phi.
Differentiating the last display gives

  m'''=E[L^3+2L dot L+dot L L+ddot L]phi.

The two copies of L dot L come from the weak evolution of the law and
from differentiating L^2. Omitting either would make the formula wrong.
For phi=aK the four terms have maximal growth q^4,q^3,q^3,q^2.
The factor min(|w|,1) remains in every term because all are linear in
phi and its parameter derivatives. The coefficients depend on G and
its first two time derivatives, whose required spatial derivatives are
bounded first using the lower-order identities. There is no use of an
unknown third time derivative in this argument.

The moment check can also be made with scalar Ito calculus on
S=A^2+V^2. Its quadratic variation rate is 8lambda S, and applying
Ito to (1+S)^2 gives drift

  4(1+S)(AG+AVG'-lambda S)+8lambda+16lambda S.

Dropping the negative term and using AG+AVG'<=1/2+S gives
10+22S+4S^2<=20(1+S)^2. Initial expectation is 13. Thus all four
growth classes above are controlled by the same fourth moment bound.
Fourth moments need not be uniformly integrable at order four; the
cutoff argument instead uses pointwise tail convergence and dominated
convergence after time integration. At orders below four, uniform
integrability does give the continuity used at t=0.

## 7. Positivity scale and failed extensions

Balancing C3 t^3 with exp(-(1+L^2)/2)/4 gives
L^2=6log(1/t)-1-2log(4C3), independently recovering the coefficient
sqrt(6). A first-order expansion with an O(t^2) error instead yields 2.
The finite lower bounds of E/g and Z/g, rather than their positive
tail alone, are essential to make the quadratic tangent globally
positive for a common small time.

The estimate still fails to determine the sign outside its growing
finite interval. Positive tails of both initial derivatives do not
justify exchanging w->infinity and t->0. Higher-order truncations,
without a remainder adapted to their tail, cannot do that either.
The result does not address annealing; a nonconstant temperature
introduces derivatives of lambda in the time-dependent operator.
It does not imply a uniform quotient gap or a risk-time bound.
