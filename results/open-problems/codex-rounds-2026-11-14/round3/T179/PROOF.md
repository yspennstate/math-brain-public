# Scalar order supplies the missing continuity estimate

Let T=R/Z, with Lebesgue measure one, H=L2(T), E=Linfinity(T),
and S_t=exp(t Delta). Suppose

    0<beta<1,
    |g(z)-g(z')| <= L|z-z'|^beta,     |g(z)| >= c>0.             (1)

No upper bound on g is imposed. A weak mild solution has continuous
H-valued paths and solves the equation with cylindrical Brownian noise
on H. All uniqueness statements below concern the state-path law.

The sole nonclassical uniqueness input is the following bounded-start
theorem:

    For every deterministic v in E, the equation with coefficient g
    has a weak solution and a unique law on C([0,T];H).           (B)

For (1), this is Proposition 8.1 of Yi Han, *Weak uniqueness for the
stochastic heat equation with nondegenerate diffusion: the full Hölder
regime*, [arXiv:2611.07310v1](https://arxiv.org/html/2611.07310v1).
Its proof is an external input; it is not independently proved here.
The extension below is conditional on that theorem. The continuity estimate
uses scalar order. Ellipticity enters through (B) and the convenient noise
representation in Section 2.

For v in E, let P_t f(v) denote expectation under the law in (B).

**Theorem.** Assume (1) and (B).

1. If f is a bounded function on L1(T) with L1 Lipschitz constant K, then

       |P_t f(v)-P_t f(w)| <= K ||v-w||_1,     v,w in E, t>=0.   (2)

2. For each R<infinity and 0<a<=b<infinity, there is a finite
   C_(R,a,b), independent of ||v||_infinity and ||w||_infinity, such that
   for every bounded H-Lipschitz f with Lipschitz constant at most one,

       |P_t f(v)-P_t f(w)| <= C_(R,a,b) ||v-w||_2^(1/2),         (3)

   whenever v,w are in E, ||v||_2,||w||_2<=R and a<=t<=b.

3. For every deterministic u0 in H, there is a weak mild solution with
   continuous H paths and its law on each finite horizon is unique.

Thus (3) proves (UC) in the earlier worker's PROOF.md, with alpha=1/2.
The third assertion extends (B) to the residual initial-data class.

## 1. Uniform estimates and coefficient approximation

The growth consequence of (1), on a space of measure one, is

    |g(z)| <= A(1+|z|^beta),
    ||g(h)||_2^2 <= B(1+||h||_2^(2 beta)).                      (4)

Let rho be a nonnegative smooth probability density supported in [-1,1]
and let g_n=g*rho_(1/n). There is a constant A' independent of n such that

    |g_n(z)| <= A'(1+|z|^beta),
    [g_n]_beta <= L,       ||g_n-g||_infinity <= L n^(-beta).
                                                                    (5)

The bound on the approximation error uses |y|<=1/n. For growth use
|z-y|^beta<=|z|^beta+|y|^beta. Differentiating the convolution and using
the zero integral of rho' gives ||g_n'||_infinity<=C L n^(1-beta).
Thus each g_n is globally Lipschitz. Since a continuous nonzero real
function has one sign, convolution also preserves |g_n|>=c. This last
fact is not needed for the classical approximating equations.

Write X_n^h for the unique strong mild solution with coefficient g_n
and initial state h in H. The usual globally Lipschitz mild construction
applies to each n; uniformity of its Lipschitz constants is not asserted.
The estimates that follow use only (4)-(5).

Here are the estimates, including the uniformity needed for taking limits.
They apply also to any given weak solution with coefficient g. Let p_r be
the periodic heat kernel. For 0<r<=T,

    ||S_r M_k||_HS^2 = p_(2r)(0)||k||_2^2
                    <= C_T r^(-1/2)||k||_2^2.                 (6)

The identity follows by integrating p_r(x-y)^2 first in x. Symmetry and
the semigroup identity give integral p_r(x-y)^2 dx=p_(2r)(0).

For every finite p>=2 and R,T there is M_(p,R,T)<infinity such that

    sup_(n,||h||_2<=R,t<=T) E||X_n^h(t)||_2^p <= M_(p,R,T).   (7)

To justify (7) without assuming moments a priori, stop at the first
H-norm hit of level m and stop the integrand, not the time variable in
the mild equation. Denote the resulting convolution plus S_t h by X^[m].
Before the hit it agrees with X. Hilbert-space BDG, Minkowski and (4),(6)
give

    (E||X^[m](t)||_2^p)^(2/p)
       <= 2R^2 + C integral_0^t (t-s)^(-1/2)
                  [1+(E||X^[m](s)||_2^p)^(2 beta/p)] ds.

Indeed the stopped factor 1_(s<=tau_m)||X(s)||_2^(2 beta) is bounded
by ||X^[m](s)||_2^(2 beta). Each stopped quantity is finite. Taking the
supremum up to T gives A_m<=a+b A_m^beta, with constants independent of
m,n,h. If A_m>2a, then A_m^(1-beta)<=2b; otherwise A_m<=2a.
Continuous H paths have bounded H norm on compact time intervals, so
Fatou's lemma as m increases proves (7). This argument also gives (7)
for every given continuous-H weak solution from h, with the same constants.

Write Z_n^h(t)=X_n^h(t)-S_t h. For sufficiently large finite p,

    sup_(n,||h||_2<=R) E||Z_n^h||_(C([0,T] x T))^p < infinity.  (8)

The following factorization proves both (8) and the compactness used below.
For any v in H, Hölder's inequality with exponents 1/beta and
1/(1-beta) gives

    integral p_r(x-y)^2 |g_n(v(y))|^2 dy
       <= C_T r^(-(1+beta)/2)(1+||v||_2^(2 beta)).             (9)

The squared kernel's L^(1/(1-beta)) norm has exponent
-1+(1-beta)/2=-(1+beta)/2. The constant part in (4) has the smaller
singularity r^(-1/2), absorbed on a finite horizon.

Choose

    eta=(1-beta)/8,     p>12/(1-beta),     p>=2.                (10)

Increasing p to an even integer is permitted. Define

    Y_n(s,x)=integral_0^s (s-r)^(-eta)
                 integral p_(s-r)(x-y)g_n(X_n^h(r,y)) W(dr,dy).

Scalar BDG, Minkowski, (7) and (9) imply

    (E|Y_n(s,x)|^p)^(2/p)
      <= C integral_0^s (s-r)^(-2eta-(1+beta)/2) dr <= C'.     (11)

The exponent equals (3+beta)/4<1. Constants are uniform in n,h,s,x
in the ranges above. In particular E||Y_n||_Lp([0,T]xT)^p is uniformly
bounded. Stochastic Fubini and the beta-integral identity give

    Z_n^h(t) = sin(pi eta)/pi * F_eta Y_n(t),
    F_eta y(t)=integral_0^t (t-s)^(eta-1) S_(t-s)y(s) ds.       (12)

Specifically, the inner time integral is
integral_r^t (t-s)^(eta-1)(s-r)^(-eta)ds=pi/sin(pi eta).
One can first truncate the singularities and then pass to the limit using
(11), which verifies stochastic Fubini here.

The heat estimate ||S_r k||_infinity<=C_T r^(-1/(2p))||k||_p and
Hölder's inequality in time show

    ||F_eta y||_C <= C ||y||_Lp,

because eta>3/(2p), exactly the second constraint in (10). Smooth inputs
are dense in Lp; their outputs are continuous and vanish at t=0.
Thus every output has those properties. This proves (8).

The same map is compact into C([0,T]xT). To see this explicitly, replace
its kernel at r=t-s by a smooth cutoff that vanishes for r<epsilon and
equals the original kernel for r>2epsilon. The resulting integral operator
has a continuous kernel in (t,x,s,y) on compact sets, including across the
cutoff, and maps bounded Lp sets to uniformly bounded equicontinuous sets.
Arzelà-Ascoli makes it compact. The removed part has operator norm at most

    C epsilon^(eta-3/(2p)),

by integrating r^(eta-1-1/(2p)) in L^(p/(p-1))(0,2epsilon).
The exponent is positive. Hence F_eta is a norm limit of compact operators.
Markov's inequality on ||Y_n||_Lp then makes the Z_n^h laws tight in C.
For each fixed h the X_n^h laws are tight in C([0,T];H), since
t -> S_t h is continuous in H. The deterministic heat part need not be
continuous in the spatial supremum norm at t=0.

The identical argument applies to weak solutions with coefficient g.
It proves positive-time spatial boundedness, a continuous stochastic
remainder through time zero, and

    E||U_delta-S_delta u0||_2^2 <= C_(R,T) sqrt(delta),          (13)

for ||u0||_2<=R and 0<delta<=min(T,1). For (13), use isometry, (4),(6),
and integral_0^delta (delta-s)^(-1/2)ds=2sqrt(delta).

## 2. Identification of approximation limits

For fixed h, every subsequential state-path limit of X_n^h is a weak mild
solution with coefficient g and initial state h. Here are the details
needed for this assertion.

For smooth periodic phi, the approximating processes

    M_n^phi(t)=<X_n^h(t),phi>-<h,phi>
                 -integral_0^t <X_n^h(s),Delta phi> ds

are continuous martingales, with cross brackets

    <M_n^phi,M_n^psi>_t
       =integral_0^t integral g_n(X_n^h(s,x))^2 phi(x)psi(x) dx ds.
                                                                    (14)

Use tightness and a Skorokhod representation on the Polish path space
C([0,T];H) along a convergent subsequence. The represented states converge
uniformly in H almost surely. The coefficient estimate

    ||g_n(v)-g(w)||_2 <= L n^(-beta)+L||v-w||_2^beta            (15)

uses Jensen on a measure-one space. Thus the quadratic expressions in
(14) converge uniformly in time on sets bounded in path H norm: use
||a^2-b^2||_1<=(||a||_2+||b||_2)||a-b||_2 and (4),(15).

Uniform path moments required to pass the martingale identities follow
from (8) and sup_t||S_t h||_2<=||h||_2. Choose p in (10) still larger
if necessary. They bound both the martingale coordinates and the brackets
in L^(1+epsilon). Multiplying martingale increment identities by bounded
continuous functions of finitely many past states and taking limits
therefore preserves those identities, and also the product-minus-bracket
identities. A monotone-class argument extends them to the canonical past
sigma field. Smooth trigonometric tests in a countable dense vector space
suffice, and continuity extends the identities to other smooth tests.

The resulting cylinder martingale problem is the weak stochastic heat
equation. Here are the representation details. The linear family M^phi
and its brackets define a martingale integral for predictable step
functions in time with smooth spatial values. The isometry is

    E|M(F)_t|^2 = E integral_0^t integral |F(s,x)|^2 g(U_s(x))^2 dx ds.

Completion extends this integral to all predictable F with finite
right-hand side. Smooth spatial functions are dense for this construction:
first use the finite deterministic measure E[g(U_s(x))^2] ds dx, whose
total mass is finite by (4),(7), and then predictable simple functions.
This gives the continuous orthogonal martingale measure with covariance
density g(U)^2. For deterministic spatial phi define

    W_t(phi)=M(1_[0,t](s) phi(x)/g(U_s(x))).

The integrand is predictable and square integrable in the displayed
isometry, since its weighted square is |phi|^2. Uniform nonvanishing of
g makes the division well defined. For phi,psi in H its cross bracket
is t<phi,psi>. Every finite vector of these continuous martingales is
Brownian by the continuous-martingale characterization. Thus W is a
cylindrical Brownian motion relative to the completed canonical filtration,
and reversing the division gives M=g(U)W. Testing the weak equation with
S_(t-s)phi yields the mild equation. The integrals are legitimate by
(4),(6),(7); finite Fourier tests followed by isometry give the H identity.
The represented state has continuous H paths. This identifies the limit
in the required solution class.

For h in E, (B) identifies every such limit with the unique bounded-start
law. Consequently the full sequence converges, and for every bounded
continuous f on H and fixed t,

    E f(X_n^h(t)) -> P_t f(h).                                 (16)

For h in H this argument still supplies existence; identification with a
unique law is not used until Section 5.

## 3. Comparison for the Lipschitz approximations

For each fixed n, put four solutions with coefficient g_n on the same
white-noise probability space, from the initial states

    h_-=v min w,       v,       w,       h_+=v max w.

They satisfy, simultaneously for every t, as H functions,

    X_n^(h_-)(t) <= X_n^v(t),X_n^w(t) <= X_n^(h_+)(t).        (17)

This is the classical scalar comparison principle. A proof that also
checks its applicability to bounded measurable initial states follows.

Fix a globally Lipschitz scalar coefficient sigma, with Lipschitz constant
L_sigma. First smooth only the noise in space, using Q_epsilon=S_epsilon
on the input cylindrical Brownian motion. For two solutions A,B with
A(0)<=B(0), set D=A-B. The diffusion in the D equation is
M_(sigma(A)-sigma(B)) Q_epsilon. This is an H-valued Hilbert-Schmidt
coefficient. Variational Itô's formula for ||D^+||_2^2 gives

    E||D^+(t)||_2^2
      <= L_sigma^2 p_(2epsilon)(0)
                  integral_0^t E||D^+(s)||_2^2 ds.             (18)

Indeed the Laplacian term is -2 integral 1_(D>0)|partial_x D|^2,
and the trace term is
integral 1_(D>0)|sigma(A)-sigma(B)|^2 sum_k|Q_epsilon e_k|^2.
The sum is p_(2epsilon)(0), and on {D>0} the coefficient difference
is bounded by L_sigma D^+. The stochastic integral has mean zero after
localization, with removal of localization by the usual Lipschitz moment
bounds. The formula for the C1 function (z^+)^2 follows by smoothing its
second derivative and then dominated convergence; that derivative is
bounded. Variational solutions lie in L2 in time with values in H1, as
follows from the H-norm energy identity for the trace-class-noise equation.
Thus the integration by parts above is valid also for initial states in H.
Gronwall applied to (18), whose initial value is zero, gives comparison
for each epsilon>0.

For completeness these colored-noise solutions converge to the white-noise
Lipschitz solution in L2(Omega;H) at every fixed time as epsilon->0. Write
their difference as a stochastic integral and split its integrand into

    S_r[M_(sigma(A_epsilon))-M_(sigma(A))] Q_epsilon
       + S_r M_(sigma(A)) (Q_epsilon-I).

Since ||Q_epsilon||<=1, (6) bounds the squared mean of the first term by
C integral_0^t (t-s)^(-1/2) E||A_epsilon(s)-A(s)||_2^2 ds.
For the second term let its squared mean be b_epsilon(t). For each r>0,
S_r M_(sigma(A(s))) is Hilbert-Schmidt. Strong convergence Q_epsilon->I,
self-adjointness, and finite-rank approximation of a Hilbert-Schmidt
operator give convergence of its product with Q_epsilon-I in HS norm.
Its squared norm is bounded by four times (6). The mild moment estimate
with ||Q_epsilon||<=1 bounds E||A_epsilon(s)||_2^2 uniformly in epsilon
and s<=T: use (6), linear growth of sigma and the integrable Volterra
kernel t^(-1/2). The same bound holds for the white-noise A.
These bounds and dominated convergence give b_epsilon(t)->0 and a uniform bound on
0<=t<=T. Hence, writing m_epsilon(t)=E||A_epsilon(t)-A(t)||_2^2,

    m_epsilon(t) <= 2b_epsilon(t)
                     +C integral_0^t (t-s)^(-1/2)m_epsilon(s)ds.

Iteration gives a convolution with the integrable Volterra resolvent of
C t^(-1/2). Its kth convolution has coefficient
C^k Gamma(1/2)^k t^(k/2-1)/Gamma(k/2); the resulting series is integrable
on each finite horizon. Dominated convergence in this resolvent bound
gives m_epsilon(t)->0. The positive cone is closed in H, so comparison
passes to each rational time for the white-noise solutions. Their H
continuity extends it to all times. Applying this to sigma=g_n proves (17).

This comparison proof needs a fixed finite L_sigma but no bound uniform
in n. There is no assertion of comparison for arbitrary two solutions
of the limiting Hölder equation driven by a preassigned common noise.

## 4. The contraction and the required H modulus

Set D_n=X_n^(h_+)-X_n^(h_-). It is nonnegative by (17). Testing the
two equations with the constant spatial function 1 removes the Laplacian.
The difference of their spatial integrals is a true martingale: its
quadratic variation has finite expectation by (4),(7). Consequently

    E||D_n(t)||_1
       = E integral D_n(t,x)dx
       = integral (h_+-h_-)(x)dx = ||v-w||_1.                 (19)

Pointwise (17) also gives |X_n^v-X_n^w|<=D_n. Thus

    E||X_n^v(t)-X_n^w(t)||_1 <= ||v-w||_1.                    (20)

For bounded L1-Lipschitz f, (20) gives (2) at level n. Such f is also
continuous on H since ||z||_1<=||z||_2. Taking limits by (16) proves (2).
This argument uses convergence of the individual laws only; it needs no
uniqueness for any four-component or common-noise limiting equation.

To prove (3), assume ||v||_2,||w||_2<=R. Pointwise,

    |h_-|^2+|h_+|^2=|v|^2+|w|^2,

so each of ||h_-||_2,||h_+||_2 is at most sqrt(2)R. The estimate (8)
and ||S_t h||_infinity<=C_b t^(-1/4)||h||_2 imply

    sup_(n,a<=t<=b) E||D_n(t)||_infinity <= B_(R,a,b)<infinity. (21)

For a nonnegative function D, ||D||_2^2<=||D||_1||D||_infinity.
Use this inequality, (17), and Cauchy-Schwarz in probability to obtain

    E||X_n^v(t)-X_n^w(t)||_2
      <= E sqrt(||D_n(t)||_1||D_n(t)||_infinity)
      <= sqrt(E||D_n(t)||_1 * E||D_n(t)||_infinity)
      <= sqrt(B_(R,a,b)) ||v-w||_1^(1/2)
      <= sqrt(B_(R,a,b)) ||v-w||_2^(1/2).                     (22)

No independence of the two norms is assumed in the Cauchy-Schwarz step.
For bounded H-Lipschitz f, apply (22) at level n and pass to (16).
This proves (3), with C_(R,a,b)=sqrt(B_(R,a,b)). All constants depend
only on the indicated parameters and (1), including |g(0)|, and not on
the spatial suprema of either initial state. This is precisely the
uniformity absent from a pointwise Feller argument.

## 5. Extension to all deterministic H initial states

Existence from h in H was proved in Section 2. Let U,V be any two weak
mild solutions with common deterministic u0 in H, on possibly different
probability spaces. Section 1 proves (13) for both, and U_delta,V_delta
belong to E almost surely for every deterministic delta>0.

The deterministic-time restart formula is

    E[f(U_t) | sigma(U_r: r<=delta)]
       = P_(t-delta) f(U_delta),       0<delta<t.              (23)

Here one uses Borel bounded-start state-law kernels. The state space
C([0,T];H) is Polish, and E is a Borel subset of H: it is the union of
the H-closed sets {|v|<=m a.e.}. For each n, Picard construction for the
globally Lipschitz equation gives a Borel map from h to Law(X_n^h) on
this path space. Section 2 shows that these probability measures converge
weakly for each h in E to its unique law in (B). A pointwise limit of
Borel maps into the metrizable space of probability measures is Borel.
Its evaluation at any fixed time gives P_t, including its values on
bounded Borel tests. This construction avoids assuming continuity of the
limiting state-law map before it has been proved.

Disintegration of the cylinder martingale identities at delta gives a
conditional solution from U_delta. To verify this simultaneously, use
countably many smooth trigonometric tests, rational times and bounded
past-cylinder tests; a monotone-class argument gives all canonical-past
events. Moment bounds and localization allow the martingale identities
to be conditioned. The conditional future has continuous H paths, and
the representation above converts its martingale problem to a weak mild
solution. Since U_delta is in E almost surely, (B) identifies that
conditional law. This proves (23) for random bounded states. No assertion
of pathwise uniqueness or of a strong limiting solution enters this step.

There are two ways to finish. First, (3) is (UC), so the earlier worker's
conditional reduction applies. Explicitly, for ||u0||_2<R, put
w_delta=S_delta u0 and use (23) for a bounded H-Lipschitz f. On
{||U_delta||_2<=R}, (3) bounds the expectation of the difference from
P_(t-delta)f(w_delta) by

    C_(R,t/2,t) E||U_delta-w_delta||_2^(1/2)
        <= C_(R,t/2,t) C^(1/4) delta^(1/8).

The complement costs at most 2M/R^2 when ||f||_infinity<=1, by (7).
Adding the corresponding V bound gives

    |Ef(U_t)-Ef(V_t)|
      <= 2 C_(R,t/2,t) C^(1/4) delta^(1/8) + 4M/R^2.          (24)

First let delta->0, then R->infinity. H-bounded-Lipschitz functions
determine probability measures, so U_t and V_t have equal laws.

There is also a direct check that avoids the H interpolation entirely.
For bounded L1-Lipschitz f with constant K, (2),(13),(23) give

    |Ef(U_t)-P_(t-delta)f(w_delta)|
       <= K E||U_delta-w_delta||_1 <= K sqrt(C) delta^(1/4).

Therefore

    |Ef(U_t)-Ef(V_t)| <= 2K sqrt(C) delta^(1/4) -> 0.          (25)

To see that these tests determine the H laws, use the real and imaginary
parts of exp(i<z,phi>), for every real trigonometric polynomial phi.
They are bounded L1-Lipschitz functions, with constant ||phi||_infinity.
They identify the characteristic functions of every finite collection
of Fourier coordinates. Those coordinates generate the Borel sigma field
of the separable Hilbert space H, so their finite-dimensional laws determine
the probability measure on H. This proves the same one-time conclusion
without any claim that L1 and H have identical topologies.

Finally fix 0<t1<...<tk. Formula (23) and (B) identify the joint law by
the common first-time law followed by the kernels
P_(t2-t1),...,P_(tk-t(k-1)). All intermediate states belong to E.
The finite-dimensional distributions therefore agree. Evaluations at a
countable dense set of times generate the Borel sigma field on
C([0,T];H), and the time-zero value is deterministic. Thus the full
state-path laws agree. This proves the theorem.

## 6. Independent checks and limits of the conclusion

The exact L1 coefficient in (2) is one. It cannot be reduced uniformly:
for constant diffusion and initial states differing by a constant d>0,
the difference under synchronous coupling stays equal to d and the
spatial-integral means differ by d. Testing with bounded clipped spatial
integrals and sending the clipping level to infinity also witnesses the
sharp constant among bounded Lipschitz tests.

The identity behind (19) can be checked before any approximation limit:
spatial mass solves d<X,1>=integral g_n(X)W(dt,dx). Its expectation is
the initial mass because integral_0^T E||g_n(X)||_2^2 dt<infinity.
For the two bracket initial states their mass difference is exactly
integral |v-w|, even when v,w change sign and cross in space.

For example, take w=0 and v equal to 1 on half the torus and -1 on the
other half. Their signed mass difference is zero, while ||v-w||_1=1.
The enclosing initial states are h_-=0,-1 and h_+=1,0 on the two halves,
respectively; their mass gap is one. Using the signed mass of v-w itself
would therefore give a false bound.

The estimates also survive bounded initial states with unbounded spatial
suprema along a sequence. For h_N=sqrt(N)1_[0,1/N], ||h_N||_2=1 and
||h_N||_infinity=sqrt(N), while ||h_N||_1=N^(-1/2). Comparing h_N with
zero, (20) gives an L1 mean bound N^(-1/2), and (21)-(22) give an H mean
bound C_(1,a,b) N^(-1/4) for a<=t<=b. No constant contains sqrt(N).
This checks the particular uniformity needed at the rough initial time.

As a separate check on the L1 mechanism, Nicolas Fournier and Jacques
Printems, *Stability of the stochastic heat equation in L1([0,1])*,
[arXiv:1007.0896v1](https://arxiv.org/pdf/1007.0896), derive an L1
martingale dissipation inequality for Lipschitz equations with Neumann
boundary conditions. The present proof uses the periodic mass identity
and ordered brackets instead, and supplies that argument in full above.
No Hölder uniqueness conclusion is imported from their Lipschitz theorem.

The two closure calculations (24) and (25) use different test classes.
They give delta^(1/8) and delta^(1/4), respectively, after taking the
same squared stochastic error O(sqrt(delta)). These are comparison errors
at the initial restart; no rate of convergence of coefficient
approximations is claimed.

The argument is scalar. A componentwise minimum and maximum do not give
the required comparison for general vector-valued diffusion. It does not
prove pathwise uniqueness for the limiting scalar equation. If ellipticity
is dropped, input (B) can fail; the smooth approximations then need not
converge to the law of an arbitrary given bounded-start solution. This is
exactly where the argument stops in the known nonuniqueness examples.

The endpoint beta=1 has the classical globally Lipschitz theory. The
factorization in Section 1 handles every 0<beta<1 with finite p, however
large the required p becomes. No claim about merely continuous g is made.
The new ingredient here is the extension argument from (B), not an
independent proof of Han's bounded-start theorem or an audit of its
finite-expansion estimates.
