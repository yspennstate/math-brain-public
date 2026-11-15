# Checks of the first-projection estimate

All checks are analytic. No simulation or numerical optimization was run.

## 1. Normalization and a second derivation of the projection

Let X,X' be independent uniform query points, independent of S. Define
a_n(x)=E_S d(x;S). The common deleted-tour expectation cancels from
the difference of the two conditional tour means. Thus

\[
 n\operatorname{Var}(\mathbb E[L_n\mid X_1])
 =\frac n2\mathbb E_{X,X'}(a_n(X)-a_n(X'))^2
 =\frac12\mathbb E_{X,X'}(U_n(X)-U_n(X'))^2.
\]

The last expression is exactly Var(U_n(X)). This checks the sqrt(n)
scale without using the centered version of (8) in PROOF.md.
In particular the boundary-strip integrals in that proof already have
the correct scale for V_{n,1}; multiplying them by another n would be
an error.

This is a variance of an expectation over S, not the expected variance
over X conditional on S. The latter is E_n/n before normalization and
is a different quantity. No interchange of those two variances occurs.

## 2. Uniform boundary bound by an order-statistic argument

For fixed x define the homothety gauge

\[
 p_x(y)=\inf\{t\in[0,1]:y\in x+t(Q-x)\}.
\]

For uniform Y, the squared gauge p_x(Y)^2 is uniform on [0,1],
because a homothetic square of parameter t has area t^2. With n-1
points, the expected minimum squared gauge is

\[
 \int_0^1(1-s)^{n-1}\,ds=\frac1n.
\]

The point attaining the minimum gauge has squared distance from x at
most twice that squared gauge. The nearest Euclidean point can only
be closer, giving E R(x;S)^2<=2/n. Therefore
U_n(x)^2<=4n E R(x;S)^2<=8 by Jensen. This checks (10) through
an order statistic rather than the Euclidean distance-tail calculation.
The argument works for corners and edges without any disk-area formula.

For n=2 one can check the scale more directly. Here S={Y} and
U_2(x)=2sqrt(2) E|x-Y|. Direct integration gives

\[
 \mathbb E|x-Y|^2
 =(x_1-1/2)^2+(x_2-1/2)^2+1/6\le2/3,
\]

so U_2(x)^2<=16/3<8. The general constant is conservative and does
not fail at the smallest sample size. No asymptotic estimate is applied
to n=2.

## 3. The constant 1/4 without a shrinking-strip calculation

For each fixed interior x and t>=0,

\[
 \mathbb P(\sqrt n R(x;S)>t)\longrightarrow e^{-\pi t^2}.
\]

The homothetic-square bound gives the integrable upper bound
exp(-t^2/4) for every n>=2 and x. Integrating in t by dominated
convergence gives

\[
 \sqrt n\,\mathbb E R(x;S)
 \longrightarrow\int_0^\infty e^{-\pi t^2}\,dt=1/2.
\]

Hence limsup U_n(x)<=1 at every interior x. Together with U_n>=0,
this implies

\[
 \limsup_n(U_n(x)-1/2)^2\le1/4.
\]

The uniform bound U_n<=2sqrt(2) supplies a constant integrable
majorant. Applying Fatou's lemma to that majorant minus the square
gives

\[
 \limsup_n V_{n,1}
 \le\limsup_n\int_Q(U_n(x)-1/2)^2\,dx\le1/4.
\]

This independently establishes the principal constant, without the
finite-n interior error or the particular strip width in PROOF.md.
The uniform moment bound is essential: the fact that the boundary itself
has area zero would not by itself justify this integral passage.

For a separate finite-n check, split a replacement pair X,X' according
to whether both are in I_a. With p=1-b_a, its interior contribution to
half the mean squared difference is p^2 W_{n,a}. On the remaining event
the squared difference is at most 8, and that event has probability
1-p^2<=2b_a. Since the range of U_n on I_a has length at most
1+delta_n(a), centering at its midpoint gives
W_{n,a}<=(1+delta_n(a))^2/4. Thus

\[
 V_{n,1}\le\frac{(1+\delta_n(a))^2}{4}+8b_a.
\]

This second finite-n bound has the same limiting constant as (4).

## 4. Boundary comparison with different conditional means

Let m_B and W_B be the mean and variance on the boundary strip, and
m_I,W_I those on I_a. Total variance gives exactly

\[
 V_{n,1}=pW_I+b_a W_B+p b_a(m_I-m_B)^2.
\]

The last two terms together equal

\[
 b_a\mathbb E[(U_n-m_I)^2\mid X\notin I_a]
       -b_a^2(m_I-m_B)^2\le8b_a.
\]

They are nonnegative, so pW_I<=V_{n,1}<=pW_I+8b_a.
This checks (16)-(17) directly, including any difference between the
two conditional means. A possible mean difference is not discarded.
The centered integral on the strip is at most 8b_a because both the
global mean and the field lie in the same interval of length 2sqrt(2).

The strip area is exactly 1-(1-2a)^2=4a-4a^2. Thus the boundary
error vanishes for every a tending to zero, even if sqrt(n)a does not
diverge. That last condition matters only for the interior range bound.

## 5. Interior error and strip width

The disk-area formula is used only for r<=a<1/2; therefore pi r^2<1.
The tail beyond a uses the homothetic square, not an invalid full-disk
formula near the boundary. The Gaussian first-moment integral gives
2sqrt(n)/(2sqrt(n-1))=sqrt(n/(n-1)), accounting for the first term
in delta_n(a). The tail integral is bounded by replacing 1 by r/a,
so its coefficient is 2sqrt(n)/((n-1)a), with no missing square root.

For a_n=sqrt(8 log(n)/n), the void exponential is
n^{-4+4/n}<=n^{-2}. Its prefactor is
2n/((n-1)sqrt(8 log n))<=4/sqrt(8 log n). This reproduces the
second term in (19). The square-root error is at most 1/(2(n-1)).
The boundary error is O(sqrt(log(n)/n)) and dominates those two terms.
The shrinking width is used only for sufficiently large n, so its value
exceeding 1/2 at small n has no bearing on any finite-n theorem.

The stronger integrated error (5a) avoids selecting a width. A second
derivation of its coefficient 8 uses the four sides of the square.
If s_i(x) is the distance to side i, then
1_{s(x)<=r}<=sum_{i=1}^4 1_{s_i(x)<=r}. For a particular side,
integrating its indicator over Q gives min(r,1)<=r. Multiplication by
2sqrt(n), integration against exp(-(n-1)r^2/2), and summation over
four sides give 4 times 2sqrt(n)/(n-1), exactly the coefficient in
(14a). Overlaps near corners only improve this union bound.

For the remaining scalar step, u in [0,1] has u^2-u<=0, while
u in [1,2sqrt(2)] has u^2-u=u(u-1)<=2sqrt(2)(u-1).
This verifies the positive-part inequality in both ranges. The error
epsilon_n is therefore at most

\[
 2\sqrt2\left\{\frac1{2(n-1)}+\frac{8\sqrt n}{n-1}\right\},
\]

which is O(n^{-1/2}). No hidden boundary convergence assumption is used.

## 6. Earlier result and total-variance consequence

For the round 4 energy bound, the replacement identity reads

\[
 E_n=\frac12\sum_i\mathbb E(L_n-L_n^{(i)})^2
    =n\mathbb E\operatorname{Var}_X(d(X;S)\mid S).
\]

Translation between its two disks has distance 3c/(4sqrt(n)), so
the scaled Lipschitz difference is at most 3c/2. The deficit pair is
at least (c/2)(5c/2-3c/2)=c^2/2. Disk area pi c^2/(64n) gives
pi c^4/(128n), which verifies the weaker pi c^4/(256n) used there.
Its isolated-site count is
(n-1)(1-6c/sqrt(n))^2(1-9pi c^2/n)^{n-2}. Division by n gives
the required exponential limit. The supports are disjoint because their
radii are 3c/(2sqrt(n)), while admissible sites are separated by more
than 3c/sqrt(n). No independence of different site events is needed.

The scalar envelope expectation can be checked from W=pi Z^2,
which is exponential. With t=pi c^2,

\[
 \mathbb E[Z^2\mathbf1_{Z>c}]=(c^2+1/\pi)e^{-t},\qquad
 \mathbb E[Z\mathbf1_{Z>c}]
 =ce^{-t}+\tfrac12\operatorname{erfc}(\sqrt\pi c).
\]

Substitution into c^2+4 E[Z(Z-c)1_{Z>c}] recovers F(c),
including the factor -2c multiplying erfc. Thus the old K is verified.

The spectral factor in (20) can be checked by exact subtraction:

\[
 E_n+V_{n,1}-2\operatorname{Var}(L_n)
 =\sum_{j\ge3}(j-2)V_{n,j}\ge0.
\]

It is an equality for spectra supported in orders one and two. Taking
limit superiors of the sum is legitimate because both sequences have
finite uniform upper bounds. No matching lower bound is used.

For strict improvement, the envelope average gives
F(c)>=E[(Z-c)^2+Z^2]>=2/pi-1/4. The deficit maximum is found
by differentiating t^2 exp(-t): its derivative is t(2-t)exp(-t),
so the maximum is at t=2. The denominator is
256 times 9^2 times pi =20736 pi; multiplying by the maximum 4/e^2
gives 1/(5184 pi e^2). Finally

\[
 \left(\frac7{11}-\frac14-\frac1{5184}\right)-\frac14
 =\frac3{22}-\frac1{5184}>0.
\]

This checks the magnitude and sign of the strict bound K>1/4.

## 7. What these estimates do not prove

Range bounds and negligible boundary contributions do not imply that
the interior profile becomes constant. For a concrete test set

\[
 q(x)=2\{(x_1-1/2)^2+(x_2-1/2)^2\}.
\]

It is continuous, invariant under the square's symmetries, and takes
values in [0,1]. Take artificial profiles equal to q for even n and
q/2 for odd n. Direct integration gives E[(X_i-1/2)^2]=1/12 and
E[(X_i-1/2)^4]=1/80. Thus Var((X_i-1/2)^2)=1/180, and
Var(q)=2/45 while Var(q/2)=1/90. These profiles have negligible
shrinking boundary contributions but nonconvergent variances. They are
not TSP insertion fields; they only test the insufficiency of the new
range and boundary bounds as an abstract convergence argument.

Likewise the leading asymptotic E L_n~beta sqrt(n) would not alone
imply mu_n->beta/2. For the deterministic sequence
m_n=beta sqrt(n)+epsilon(-1)^n/sqrt(n), with 0<epsilon<beta/4,
the same leading asymptotic holds, and the consecutive increments are
eventually positive. Nevertheless sqrt(n)(m_n-m_{n-1}) has two limits
beta/2+2epsilon and beta/2-2epsilon. This is a sequence test, not a
claim about actual expected tour lengths.

No counterexample to the stated new inequalities was found. Convergence
of the first projection, of fixed-noise covariance, and of the full tour
variance all remain unproved here.
