# A continuity criterion for extending bounded-data uniqueness

Let T = R/Z have Lebesgue measure one, let H = L2(T), and write
S_t = exp(t Delta). All norms without a subscript below are H norms.
Suppose 0 < beta < 1 and

    |g(z)-g(w)| <= L |z-w|^beta,       |g(z)| >= c > 0.             (1)

There is no upper bound on g. Fix a deterministic u0 in H. A solution means
an adapted, continuous H-valued weak mild solution of

    U_t = S_t u0 + Z_t,
    Z_t = integral_0^t S_(t-s) M_(g(U_s)) dW_s.                  (2)

Here W is cylindrical Brownian motion on H, and M_h denotes multiplication
by h before heat smoothing. No common probability space for two solutions
is required.

## Known input and the additional hypothesis

Put E = L-infinity(T), viewed as a subset of H. Use the bounded-initial-data
uniqueness result in Yi Han, *Weak uniqueness for the stochastic heat equation
with nondegenerate diffusion: the full Hölder regime*,
[arXiv:2611.07310v1, Proposition 8.1](https://arxiv.org/html/2611.07310v1).
For v in E, let P_s(v, .) be the resulting transition probability on H and
write P_s f(v) = integral f(w) P_s(v,dw).

Use its Borel continuation kernels and deterministic-time conditional restart:
once a solution is in E, its conditional future law is the unique law from
that state. These are the usual martingale-problem interpretation of the
bounded-data result. In particular, for deterministic delta > 0,

    E[f(U_t) | G_delta] = P_(t-delta) f(U_delta),     t > delta,  (3)

where G_delta = sigma(U_r:0<=r<=delta), whenever U_delta is in E almost
surely. Conditioning on this canonical state history avoids a regular-
conditional-probability assumption on an arbitrary ambient filtration.
The martingale-problem disintegration
is performed on the Polish space C([0,T];H); it does not require a strong
solution or pathwise uniqueness. The set E is Borel in H: it is the union over
integers n of {v: |v| <= n almost everywhere}, and each such set is H-closed.
Uniqueness of the bounded-start martingale problem provides Borel state-law
kernels on E. Conditioning the cylinder martingale identities at delta gives
a solution from U_delta, and bounded-start uniqueness gives (3).

Here is the extra estimate to be proved, not an assumption known from Han:

(UC) For each f:H->R with sup |f| <= 1 and Lipschitz constant <= 1, each
0 < a <= b < infinity and each R < infinity, define

    omega_(f,R,a,b)(r)
      = sup |P_s f(v)-P_s f(w)|,

where the supremum is over a <= s <= b, v,w in E,
||v||,||w|| <= R, and ||v-w|| <= r. Then

    lim_(r down to 0) omega_(f,R,a,b)(r) = 0.                    (4)

The bound is in H norms. No bound on ||v||_infinity or ||w||_infinity is
allowed in the modulus.

**Theorem.** Under (1), the bounded-start result and (UC) imply uniqueness
in law from every deterministic u0 in H. More precisely, for any two solutions
U,V, each fixed t>0, and each f as above, there are constants M,C, independent
of the two solutions, such that, for R>||u0||, r>0 and
0<delta<min(t/2,1),

    |E f(U_t)-E f(V_t)|
       <= 2 omega_(f,R,t/2,t)(r)
          + 4 C sqrt(delta)/r^2 + 4 M/R^2.                     (5)

If, more strongly, omega_(f,R,a,b)(r) <= K r^alpha for some 0<alpha<=1,
the right side in (5) can be replaced by

    2 K C^(alpha/2) delta^(alpha/4) + 4 M/R^2.                  (6)

The constant K may depend on f,R,a,b. Formula (6) is useful only with that
dependence retained. This theorem does not establish (UC).

## 1. Moment bounds using only the H norm of the initial state

The growth consequence of (1) is

    |g(z)| <= A(1+|z|^beta),
    ||g(v)||_2^2 <= B(1+||v||^(2 beta)).                        (7)

The second inequality follows from the first, (a+b)^2 <= 2a^2+2b^2,
and integral |v|^(2 beta) <= (integral |v|^2)^beta on a space of measure one.

Let p_r be the periodic heat kernel. For 0<r<=T,

    ||S_r M_h||_HS^2
      = integral_T integral_T p_r(x-y)^2 |h(y)|^2 dx dy
      = p_(2r)(0) ||h||_2^2
      <= k_T r^(-1/2) ||h||_2^2.                              (8)

The equality uses symmetry and the heat semigroup property. The final bound
follows either by periodizing the Gaussian or by its Fourier series.

Here are localization details for the needed moments. For n>||u0|| let
tau_n = inf{t:||U_t||>=n}, and define the stopped-integrand convolution

    U_t^[n] = S_t u0
       + integral_0^t 1_(s<=tau_n) S_(t-s) M_(g(U_s)) dW_s.

It equals U before tau_n. For any fixed p>=2 the Hilbert-space BDG inequality,
followed by Minkowski's integral inequality and (7)-(8), gives

    (E||U_t^[n]||^p)^(2/p)
       <= 2||u0||^2
          + C_(p,T) integral_0^t (t-s)^(-1/2)
                [1+(E||U_s^[n]||^p)^(2 beta/p)] ds.            (9)

Indeed 1_(s<=tau_n)||U_s||^(2 beta) <= ||U_s^[n]||^(2 beta);
Lyapunov's moment inequality handles the power beta p. The stopped
integrands have bounded H norm depending on n, so all quantities in (9)
are finite before any absorption is used.

Set A_n = sup_(t<=T)(E||U_t^[n]||^p)^(2/p). Integrating the kernel yields

    A_n <= a + b A_n^beta,                                    (10)

with finite a,b independent of n and of the solution. If A_n>2a, (10) gives
A_n^(1-beta)<=2b. Otherwise A_n<=2a. Thus

    A_n <= max(2a, (2b)^(1/(1-beta))).

Continuous H paths are bounded on every compact time interval, so tau_n>T
eventually on each path. Fatou's lemma at each fixed t now proves

    sup_(t<=T) E||U_t||^p <= M_(p,T,u0) < infinity.              (11)

These constants depend only on p,T,beta,A and ||u0||, not on a spatial
supremum of u0. A continuous stopped-convolution version may be obtained
by the factorization below, or by its H-valued version with p>4. Only
fixed-time moments are asserted in (11).

## 2. Positive-time boundedness for rough initial states

This step verifies the applicability of (3). It does not prove uniqueness.
For 0<r<=T, Holder's inequality in space and the Gaussian heat bound give

    integral_T p_r(x-y)^2 |g(v(y))|^2 dy
       <= C_T r^(-(1+beta)/2) (1+||v||^(2 beta)).               (12)

For the term |v|^(2 beta), use conjugate exponents 1/beta and 1/(1-beta).
The squared kernel has L^(1/(1-beta)) norm bounded by
C_T r^(-(1+beta)/2). Its constant term has integral O(r^(-1/2)),
which is also bounded by the displayed expression on a fixed time interval.

Choose 0<eta<(1-beta)/4 and then an integer p>3/(2 eta). Define

    Y_s(x) = integral_0^s (s-r)^(-eta)
                 integral_T p_(s-r)(x-y) g(U_r(y)) W(dr,dy).

Scalar BDG, Minkowski, (11), and (12) imply

    (E|Y_s(x)|^p)^(2/p)
       <= C integral_0^s (s-r)^(-2 eta-(1+beta)/2) dr < infinity.

The bound is uniform in s<=T and x. The exponent is less than one precisely
because 2 eta+(1+beta)/2<1. Thus Y belongs almost surely to
L^p([0,T] x T).

Stochastic factorization gives

    Z_t = (sin(pi eta)/pi)
           integral_0^t (t-s)^(eta-1) S_(t-s) Y_s ds.           (13)

For completeness, the time integral behind the identity is

    integral_r^t (t-s)^(eta-1)(s-r)^(-eta) ds
       = B(eta,1-eta) = pi/sin(pi eta).

The semigroup property combines the spatial kernels. Stochastic Fubini,
first with truncated time singularities and then by the integrability just
proved, gives (13).

The map on the right of (13), without its constant factor, sends
L^p([0,T] x T) continuously into C([0,T] x T). To see this, use
||S_r h||_infinity <= C_T r^(-1/(2p)) ||h||_p and Holder's inequality in time.
The time kernel is r^(eta-1-1/(2p)); it belongs to L^(p/(p-1))(0,T)
exactly when eta>3/(2p). It follows that the map has a uniform supremum
bound. Approximating its input in L^p by smooth functions proves continuity
of the output, including value zero at time zero. In particular Z has a
continuous representative on [0,T] x T with Z_0=0.

Heat smoothing makes S_t u0 continuous in x for t>0. Consequently U_t is
in E almost surely at each positive time, and its positive-time path is
continuous with values in C(T). The H identity between this version and (2)
holds simultaneously in time: first take a common probability-one event on
a countable dense set of times and then use H continuity. Boundedness of u0
was not used.

## 3. The initial stochastic error and its sharp exponent

By stochastic isometry and (7)-(8), for 0<delta<=min(T,1),

    E||U_delta-S_delta u0||^2
      = integral_0^delta p_(2(delta-s))(0) E||g(U_s)||_2^2 ds
      <= C sqrt(delta).                                     (14)

Here (11) with p=2 bounds E||U_s||^(2 beta) uniformly, and
integral_0^delta (delta-s)^(-1/2) ds = 2 sqrt(delta).
Thus the root-mean-square error is at most sqrt(C) delta^(1/4).

The power cannot be improved uniformly over this class. For g identically
sigma nonzero, stochastic isometry gives exactly

    E||Z_delta||^2 = sigma^2 integral_0^delta p_(2r)(0) dr.

Periodizing the real Gaussian gives

    p_(2r)(0) = (8 pi r)^(-1/2)
                   sum_(m in Z) exp(-m^2/(8r)).

The m=0 term integrates to sqrt(delta/(2 pi)); the other terms are
o(sqrt(delta)). Hence

    lim_(delta down to 0) E||Z_delta||^2/sqrt(delta)
        = sigma^2/sqrt(2 pi).                                (15)

An independent Fourier derivation is given in the audit below.

## 4. Reduction to the transition estimate

Fix t>0 and let v_delta = S_delta u0. Heat contraction gives
||v_delta||<=||u0||, and heat smoothing gives v_delta in E for delta>0.
Let M bound the second moments in (11) for both solutions on [0,t], and
let C be the common constant in (14). By (3),

    E f(U_t) = E P_(t-delta) f(U_delta).

For R>||u0|| and r>0, on the event

    A = {||U_delta||<=R, ||U_delta-v_delta||<=r},

the difference between this integrand and
P_(t-delta) f(v_delta) is at most omega_(f,R,t/2,t)(r), since
delta<t/2. On its complement the difference is at most 2. Markov's
inequality and (14) give

    |E f(U_t)-P_(t-delta) f(v_delta)|
       <= omega_(f,R,t/2,t)(r)
          + 2 C sqrt(delta)/r^2 + 2 M/R^2.                    (16)

The same deterministic comparison term works for V. Adding its bound gives
(5). First let delta decrease to zero with R,r fixed. Next let r decrease
to zero, using (UC). Finally let R increase to infinity. The two expectations
are equal. This order of limits imposes no uncontrolled condition on the
R-dependence of the continuity modulus.

For (6), instead bound the difference on {||U_delta||<=R} by
K||U_delta-v_delta||^alpha. Lyapunov's inequality and (14) give its expectation
at most K C^(alpha/2) delta^(alpha/4). The tail contributes at most 2M/R^2.
Add the corresponding estimate for V.

Bounded Lipschitz functions determine probability measures on the separable
Hilbert space H. Thus U_t and V_t have the same distribution for every t>0.
For 0<t1<...<tk, repeated conditional restart identifies the joint law as

    Law(U_t1)(dv1) P_(t2-t1)(v1,dv2) ... P_(tk-t(k-1))(v(k-1),dvk).

All states at these positive times are in E almost surely. This identifies
all finite-dimensional distributions. Evaluations at a countable dense set
of times generate the Borel sigma field of C([0,T];H), and the initial
state is fixed. The state-path laws are therefore equal. This proves the
conditional theorem.

## 5. Checks and the unresolved step

The endpoint beta=1 is excluded from the factorization parameters above;
globally Lipschitz coefficients have the usual separate uniqueness theory.
For every beta<1, however close to one, eta can be chosen positive and p
finite. No claim for merely continuous coefficients is made.

The ellipticity bound is used in the bounded-start uniqueness input, not in
(7)-(15). Those estimates alone cannot resolve uniqueness. In particular the
proof cannot be applied to a vanishing coefficient without replacing the
bounded-start uniqueness input.

For an independent check of (15), Fourier modes of the torus have
eigenvalues -4 pi^2 k^2, so for sigma=1,

    E||Z_t||^2 = t + 2 sum_(k>=1)
                       (1-exp(-8 pi^2 k^2 t))/(8 pi^2 k^2).    (17)

With h=sqrt(t), division by sqrt(t) turns this into a Riemann sum for
integral_R F(x) dx, where

    F(x) = (1-exp(-8 pi^2 x^2))/(8 pi^2 x^2),    F(0)=1.

The integral equals 1/sqrt(2 pi). Indeed, for a>0, Tonelli applied to
(1-exp(-a x^2))/x^2 = integral_0^a exp(-q x^2) dq gives integral_R
(1-exp(-a x^2))/x^2 dx = 2 sqrt(pi a). Divide by a and put a=8 pi^2.
The integrable bound F(x)<=min(1,(8 pi^2 x^2)^(-1)) also justifies the
Riemann-sum tails. This checks both the coefficient and the heat normalization
independently of the periodized-kernel calculation.

For constant g, synchronous coupling gives
|P_s f(v)-P_s f(w)|<=||S_s(v-w)||<=||v-w||. Thus (UC) passes this
consistency check. It remains unproved for the general coefficient (1).
Pointwise continuity for each bounded initial state, or an estimate involving
its spatial supremum, does not supply (UC).

There is a concrete reason a fixed spatial cutoff at time zero cannot simply
replace (UC). Choose u0(x)=dist(x,0)^(-a) near zero, cut off away from zero,
with 0<a<1/2. This belongs to H. A Gaussian lower bound over
|y|<=sqrt(t) gives S_t u0(0)>=c_a t^(-a/2). Since Z tends uniformly to zero
at time zero, ||U_t||_infinity is unbounded as t decreases to zero almost
surely. For every fixed R, inf{t>0:||U_t||_infinity>=R}=0. The positive
exit-time argument for bounded initial states therefore fails on this input.
This is an obstruction to that localization argument, not a nonuniqueness
example.
