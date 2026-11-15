# A time-resolved Brownian signed pair limit

Let f be a fixed real measurable function on R^2 with

    |f(x)| <= C exp(-a|x|),       m := integral f(x) dx > 0.       (1)

Set H=L^2(R^2;C), L=log N, and

    p_t(x)=(4 pi t)^(-1) exp(-|x|^2/(4t)),
    u=sqrt(|f|),       v=sgn(f)u,
    ell(h)=integral v(x)h(x) dx,
    P h=u ell(h)/m,       mu=m/(4 pi).

The generator of p_t* is Delta. An expression a tensor b denotes the
operator h -> a integral conjugate(b) h. In particular P=u tensor v/m
is a projection, usually not orthogonal. Multiplication is denoted M.

Define

    Q(t)=M_u exp(t Delta) M_v,
    A_N=L^-1 integral_0^N Q(t) dt.

Let Lambda_N be the unique dominant positive simple eigenvalue of A_N
for sufficiently large N. Its existence is recalled and verified below.
For a fixed real theta, take alpha_N>0 satisfying

    alpha_N L Lambda_N=1+(theta+epsilon_N)/L,
    epsilon_N -> 0.                                             (2)

Use the actual signed convolution series

    R_N(t)=sum_{k>=1} alpha_N^k Q^{*k}(t),
    F_N(t)=N R_N(Nt)/L.                                         (3)

Here convolution includes operator multiplication, in the order of the
factors. No renewal probability interpretation is imposed.

## Theorem

Put z_*=exp(theta-gamma), where gamma is Euler's constant, and for t>0 set

    g_theta(t)=integral_0^infinity z_*^s t^(s-1)/Gamma(s) ds.      (4)

This is finite, positive and continuous on (0,infinity). For every
0<delta<T<infinity,

    sup_{delta<=t<=T} ||F_N(t)-g_theta(t)P|| -> 0.                (5)

There is also norm convergence against every real continuous function
psi on [0,infinity) having a finite limit at infinity: for b>z_*,

    integral_0^infinity psi(t) exp(-bt) F_N(t) dt
        -> P integral_0^infinity psi(t) exp(-bt) g_theta(t) dt.   (6)

The same assertion for complex psi follows by real and imaginary parts.
The critical coefficient in (2) is the original sharp-time Lambda_N.
No vertical-line inversion estimate is required.

This is a fixed-profile Brownian pair theorem. It is not convergence of
the discrete or continuum stochastic flows in Conjecture 1.17.

## Proof

### 1. Verification of the input from the preceding work

The transform theorem used here is the theorem in
[the round 3 proof](~/codex_op_1114r3/briefs/T428/PROOF.md).
The needed real-axis statement and spectral bound are re-derived here.
All integrals of operators below are in operator norm.

The heat contraction and its pointwise kernel bound give, with
M=||f||_infinity,

    ||Q(t)||<=M,
    ||Q(t)||<=||Q(t)||_HS<=||f||_1/(4 pi t),       t>0.            (7)

Consequently the following sharp and exponentially damped integrals exist.
For r>0,

    S_N(r):=integral_0^N p_t(r) dt=(4 pi)^-1 E_1(r^2/(4N)),
    S_N(r)=L/(4 pi)+g(r)+r_N(r),
    g(r)=(log 4-gamma-2 log r)/(4 pi),
    0<=r_N(r)<=r^2/(16 pi N).                                   (8)

Indeed, substitute s=r^2/(4t) and use

    E_1(q)=-gamma-log q+integral_0^q (1-exp(-s)) ds/s,
    0<=1-exp(-s)<=s.

The constant follows by integration by parts in
Gamma'(1)=integral_0^infinity exp(-s)log s ds=-gamma.

The operator K with kernel u(x)g(|x-y|)v(y) is Hilbert--Schmidt.
Near x=y, use boundedness of f and integrability of log^2|x-y| on a
planar unit disk. Outside that disk use
|g(|x-y|)|<=C'(1+|x|+|y|) and the absolute moments of f. The same
weighted estimate and (8) give

    A_N=mu P+K/L+O(1/(NL)),
    I_f:=ell(Ku)=integral integral f(x)g(|x-y|)f(y) dx dy.        (9)

The integral defining I_f is absolutely convergent, by Cauchy--Schwarz
with weight |f(x)f(y)|. For the remainder in (9), square its weighted
kernel and use the finite fourth absolute moment of |x-y|.

For completeness, if E is small, the spectrum of mu P+E lies in small
disjoint disks about 0 and mu. This follows by a Neumann series from

    (w-mu P)^-1=w^-1(I-P)+(w-mu)^-1 P.

The contour integral on a fixed small circle about mu gives a spectral
projection Pi=P+O(||E||) of rank one. The rank is one since projections
at distance less than one have equal rank, by restricting each to the
range of the other. Normalize its eigenvector w_E by ell(w_E)=m.
Then w_E=u+O(||E||). Applying ell to its eigenvalue equation gives

    lambda=mu+ell(Eu)/m+O(||E||^2).

The complementary operator has norm O(||E||), since
(mu P+E)(I-Pi)=E(I-Pi)+mu P(P-Pi). Thus (9) gives

    Lambda_N=mu+I_f/(mL)+O(L^-2).                               (10)

Realness of A_N and the single eigenvalue near mu imply that Lambda_N
is real and positive. The complementary spectrum is O(1/L), so this
eigenvalue is dominant. This proves the claimed existence.

This is also the eigenvalue of the unweighted sharp-time operator
L^-1(S_N*)M_f used for the Brownian tuning coefficient. Indeed, take
X=L^-1(S_N*)M_v and Y=M_u. These are bounded because ||S_N*||<=N;
then XY=L^-1(S_N*)M_f and YX=A_N. The XY/YX resolvent identity written
below identifies their nonzero spectra. It identifies algebraic
multiplicities as well: X and Y intertwine the two operators and are
injective on generalized eigenspaces for nonzero eigenvalues; using
both injections gives equal dimensions. Both operators are compact:
for the full one, its squared kernel integral is
L^-2 ||S_N||_2^2 ||f||_2^2<infinity. Here S_N is logarithmic at zero
and has a Gaussian tail, by its E_1 expression. Thus no replacement
of the tuning coefficient is hidden in the weighted formulation.

For fixed real z>0 let

    J_N(z)=integral_0^infinity exp(-zt/N)Q(t) dt,
    B_N(z)=alpha_N J_N(z),
    d(z)=log z+gamma-theta.

Subtract the sharp time kernel and put t=Ns. With
w_z(s)=exp(-zs)-1_{s<=1}, the kernel difference is

    (4 pi)^-1 integral_0^infinity
                  w_z(s) exp(-r^2/(4Ns)) ds/s.                 (11)

The integral without its spatial exponential is -gamma-log z.
To see this, differentiate it in z to obtain -1/z; at z=1 integration
by parts as above gives -gamma. Differentiation is justified because
|w_z(s)|<=zs for s<=1 and exp(-zs) for s>1, locally uniformly in z>0.
Using |1-exp(-q/s)|<=sqrt(q/s), the error in removing the spatial
exponential is at most C_z r/sqrt(N). Its weighted Hilbert--Schmidt
norm is O_z(N^-1/2), since f has finite second absolute moments.
It follows that

    J_N(z)=L mu P+K+mu(-gamma-log z)P+O_z(N^-1/2).              (12)

Write eta=I_f/(m mu). From (2) and (10),

    alpha_N=(mu L)^-1
        [1+(theta+epsilon_N-eta)/L+O(L^-2)].                    (13)

Hence

    B_N(z)=P+L^-1[K/mu
              +(theta+epsilon_N-eta-gamma-log z)P]+O_z(L^-2).

The perturbation argument just given, now about P, yields a simple
eigenvalue b_N(z), its projection Pi_N(z), and a complement C_N(z), with

    b_N(z)=1+[-d(z)+epsilon_N]/L+O_z(L^-2),
    Pi_N(z)=P+O_z(L^-1),
    B_N(z)=b_N(z)Pi_N(z)+C_N(z),       ||C_N(z)||=O_z(L^-1),   (14)

and both cross products zero. Here ell(Ku)/(m mu)=eta cancels exactly
the eta in (13). If z>z_*, then d(z)>0, and

    L^-1 B_N(z)(I-B_N(z))^-1 -> P/d(z).                        (15)

This follows either from (14) or from the scalar Schur complement of
I-B_N in range(P) plus ker(P): its diagonal scalar is
(d(z)-epsilon_N)/L+O(L^-2), and the off-diagonal product is O(L^-2).

To identify (15) as an actual transform, set

    H_N=Delta+alpha_N M_f,       domain H^2(R^2).

This operator is self-adjoint, since the potential is bounded and real.
For any fixed c>z_*, put q=c/N, T_q=(q-Delta)^-1/2 and

    X=sqrt(alpha_N) M_u T_q,
    Y=sqrt(alpha_N) T_q M_v.

Then XY=B_N(c), while YX=alpha_N T_q M_f T_q is self-adjoint.
The elementary identity

    (w-XY)^-1=w^-1[I+X(w-YX)^-1Y],       w!=0,

and its version with X,Y interchanged show equality of the nonzero
spectra. By (14), b_N(c) is positive and strictly below one for large N,
and all other spectral values have modulus O(1/L). Thus
sup spectrum(YX)<=b_N(c)<1. For psi in H^1 put h=(q-Delta)^1/2 psi.
The quadratic forms satisfy

    <psi,(q-H_N)psi>=<h,(I-YX)h>
        >=(1-b_N(c))||h||^2
        >=q(1-b_N(c))||psi||^2.

Consequently

    sup spectrum(N H_N)<=c b_N(c)<c.                          (16)

The Volterra series (3) converges on bounded time intervals because
||Q^{*k}(t)||<=M^k t^(k-1)/(k-1)!. Its Duhamel expansion gives

    R_N(t)=alpha_N M_u exp(t H_N) M_v.                         (17)

The multiplication between consecutive heat operators is M_v M_u=M_f,
which checks both the potential and the factor alpha_N in (17).
For any real z>z_*, choose c strictly between z_* and z. Equation (16)
makes (17) Laplace integrable with damping exp(-zt/N). The resolvent
identity then gives, with G=(z/N-H_N)^-1,

    alpha_N M_u G M_v
        =B_N(z)+B_N(z)[alpha_N M_u G M_v]
        =B_N(z)(I-B_N(z))^-1.

Combining with (15) and changing variables proves the input

    integral_0^infinity exp(-zt)F_N(t) dt -> P/d(z),
                  for each real z>z_*.                        (18)

No interchange of a signed infinite series and a critical Laplace
integral has been used.

### 2. The scalar limiting density

The integrand in (4) is positive. Near s=0, use
1/Gamma(s)=s/Gamma(s+1)=O(s). For s>=1, the defining gamma integral
restricted to [s,s+1] gives

    Gamma(s)>=exp(-(s+1))s^(s-1).

For t in any compact subset of (0,infinity), this bounds the integrand
in (4) by a constant times s(e z_* T/s)^s for large s. This is integrable
and also bounds any fixed number of t derivatives after multiplication
by a polynomial in s. Thus g_theta is finite and continuous (in fact
smooth) on (0,infinity).

For real z>z_*, Tonelli's theorem and the gamma integral give

    integral_0^infinity exp(-zt)g_theta(t) dt
       =integral_0^infinity (z_*/z)^s ds
       =1/log(z/z_*)=1/d(z).                                  (19)

In particular exp(-bt)g_theta(t) is integrable for b>z_*, including
at t=0. Equation (19) fixes every normalization in the time limit.

### 3. Positivity after removing the endpoint sign

Let j(x)=sgn(f(x)) if f(x)!=0 and j(x)=1 otherwise, and put J=M_j.
Then J is a self-adjoint unitary, v=Ju, and M_v J=M_u. Define

    S_N(t)=F_N(t)J
          =(N alpha_N/L) M_u exp(t N H_N) M_u,
    A=PJ=u tensor u/m.                                        (20)

For every t>=0, S_N(t) is a positive self-adjoint bounded operator:
its quadratic form at h is
(N alpha_N/L)||exp(t N H_N/2)M_u h||^2. A is also positive, with
||A||=||f||_1/m. This uses alpha_N>0 and m>0, and does not require f>=0.

Fix b>z_*. Choose c in (z_*,b). By (16), for all sufficiently large N
the spectrum of N H_N lies below c<b. The spectral theorem shows that

    D_N(t):=exp(-bt)S_N(t)

is decreasing in the order of self-adjoint operators: if t_1<=t_2,

    0<=D_N(t_2)<=D_N(t_1).                                    (21)

Indeed, for every spectral parameter lambda<=c,
exp((lambda-b)t_2)<=exp((lambda-b)t_1), and sandwiching a positive
operator with M_u preserves order. For each N, D_N is integrable in
operator norm, since (16) gives an exponentially decreasing bound.

Multiplying (18) on the right by J yields

    integral_0^infinity exp(-zt)S_N(t) dt -> A/d(z),
                       real z>z_*.                            (22)

### 4. Convergence against continuous time tests

Regard D_N(t)dt as a finite positive operator-valued measure, and define
its candidate limit by

    D(t)dt=exp(-bt)g_theta(t)A dt.

Their total masses converge in norm by (19) and (22) at z=b. In
particular their norms are uniformly bounded. For any bounded real
measurable r, positivity gives

    -||r||_infinity integral D_N(t)dt
       <= integral r(t)D_N(t)dt
       <= ||r||_infinity integral D_N(t)dt,

and therefore

    ||integral r(t)D_N(t)dt||
       <=||r||_infinity ||integral D_N(t)dt||.                  (23)

The same bound holds for D. This estimate does not assert a bound on
integral ||D_N(t)||dt uniformly in N.

Let psi be real continuous on [0,infinity) with a finite limit at
infinity. Under x=exp(-t), it becomes a continuous function on [0,1],
using that limit at x=0. By polynomial approximation, for any eta>0
there is a real polynomial p such that

    sup_{t>=0}|psi(t)-p(exp(-t))|<eta.

For p(x)=sum_{k=0}^K a_k x^k, equations (19) and (22), at the finitely
many real parameters b+k, imply

    integral p(exp(-t))D_N(t)dt
        -> integral p(exp(-t))D(t)dt.                          (24)

Apply (23) to the two approximation errors. Their sum is at most eta
times a uniformly bounded constant. First take N to infinity in (24),
then eta to zero. This proves

    integral psi(t)D_N(t)dt -> integral psi(t)D(t)dt             (25)

in operator norm. Right multiplication by J proves (6).

### 5. Recovering each positive time from operator order

Fix t>0 and 0<h<t. Choose nonnegative continuous functions phi_- and
phi_+ of integral one, supported respectively in (t-h,t) and (t,t+h).
For example, rescaled triangular functions have these properties.
By (21),

    integral phi_+(s)D_N(s)ds <= D_N(t)
                           <= integral phi_-(s)D_N(s)ds.      (26)

Both integrals converge in norm by (25), since these functions are
continuous with compact support. Their limits are the corresponding
averages of D(s)=exp(-bs)g_theta(s)A. This D is norm-continuous at t.
Given eta>0, choose h so that ||D(s)-D(t)||<eta for |s-t|<h.
For sufficiently large N each average in (26) is then within 2 eta
of D(t) in norm. All operators here are self-adjoint. Thus (26) implies

    -2 eta I <= D_N(t)-D(t) <= 2 eta I,

so ||D_N(t)-D(t)||<=2 eta. This proves norm convergence at every t>0.

To make it uniform on [delta,T], use uniform norm-continuity of D to
choose a finite partition delta=t_0<...<t_k=T such that
||D(s)-D(t)||<eta whenever s,t lie in a common partition interval.
For large N, convergence at the finitely many endpoints gives
||D_N(t_i)-D(t_i)||<eta for every i. If t_i<=t<=t_{i+1}, then

    D_N(t_{i+1})<=D_N(t)<=D_N(t_i).

Subtract D(t), and bound each endpoint difference by 2 eta I in order.
It follows that sup_{[delta,T]}||D_N(t)-D(t)||<=2 eta. Multiplication
by exp(bt), bounded on this interval, proves uniform norm convergence
S_N(t)->g_theta(t)A. Finally J is unitary and AJ=P, so (5) follows.

## Independent scalar representation

There is a second expression for the density:

    g_theta(t)=z_* exp(z_* t)
         + integral_0^infinity exp(-rt)
                  /[(log(r/z_*))^2+pi^2] dr,       t>0.        (27)

Here the positive pole term is necessary. To verify it, let
h(w)=1/log(w/z_*), with its principal logarithm. For real z>z_*,
apply the residue theorem to h(w)/(w-z) on a large disk slit along
the negative real axis, omitting a small disk about zero. The poles
inside are at w=z, with residue h(z), and w=z_*, with residue
z_*/(z_*-z). The large circle contributes O(1/log R): its length
is O(R), |w-z| is bounded below by R-z, and |log(w/z_*)|
is bounded below by log(R/z_*). The small circle contributes
O(epsilon/|log epsilon|). Both terms vanish at their respective limits.

On the upper bank w=-r+i0, h(w)=1/(log(r/z_*)+i pi). On the lower
bank it is its conjugate. The upper bank runs from -R to -epsilon;
the lower bank runs in reverse. Their combined integral divided by
2 pi i is

    integral_0^infinity dr
          /[(z+r)((log(r/z_*))^2+pi^2)].

This integral converges at both endpoints. Equating it to the sum of
residues gives

    1/log(z/z_*)=z_*/(z-z_*)
       + integral_0^infinity dr
          /[(z+r)((log(r/z_*))^2+pi^2)].                       (28)

By Tonelli, the right side is the Laplace transform of (27). It equals
(19). Uniqueness of Laplace transforms therefore proves (27): after
multiplication by exp(-bt), both densities define finite measures;
their moments under x=exp(-t) agree for every integer k>=0 by using
z=b+k; polynomial approximation on [0,1] gives equality of those
measures. Both densities are continuous for t>0, so their equality is
pointwise. Continuity of the integral in (27) follows by domination
with exp(-delta r)/pi^2 when t>=delta>0.

As a further check, (27) implies that exp(-bt)g_theta(t) is decreasing
for b>z_*, exactly as required by the operator-order argument. Scaling
also gives g_theta(t)=z_* g_base(z_*t), where g_base is (4) with z_*=1.

## Scope

Hindy Drillick, Jonathan Hou and Shalin Parekh,
*A universality result for the critical 2d stochastic heat flow*,
[arXiv:2609.15832](https://arxiv.org/html/2609.15832v1), formulate the
signed exponential extension as Conjecture 1.17. The result above adds
a time-resolved signed pair estimate to the preceding Brownian transform
theorem, with the same sharp-time spectral tuning. The sign multiplier
only removes the endpoint sign for the order argument; the potential
in H_N remains alpha_N f throughout.

No estimate uniform down to t=0, no rate in (5), no diffusive spatial
endpoint limit, no general N-dependent gap process or profile theorem,
and no third- or fourth-moment convergence is proved here. The positive
mass assumption is essential to the rank-one argument used here. No
logarithm of a singular stochastic flow is taken, and no KPZ field is
constructed.
