# A Brownian signed pair-resolvent limit

Let f be real and measurable on R^2, with

    |f(x)| <= C exp(-a|x|),       m := integral f(x) dx > 0.       (1)

The profile is fixed. Put H=L^2(R^2;C), L=log N,

    p_t(x) = (4 pi t)^(-1) exp(-|x|^2/(4t)),
    u=|f|^(1/2),       v=sgn(f)|f|^(1/2),
    ell(h)=integral v(x)h(x) dx,
    P h=u ell(h)/m,       mu=m/(4 pi).

Tensor products below use the linear functional ell, without conjugating
h. Since u and v are real, ell is also the usual Hilbert pairing with v.
P is a bounded projection, generally not an orthogonal projection.
Multiplication operators are denoted by M, and p_t* is convolution.

Define the compact weighted sharp-time operator

    A_N = L^(-1) integral_0^N M_u (p_t*) M_v dt.                  (2)

For large N let Lambda_N be its unique dominant positive simple
eigenvalue. The existence of this eigenvalue is established below;
it is the Brownian coefficient audited in the previous work.
Let alpha_N>0 obey the same sharp-time critical tuning:

    alpha_N L Lambda_N
       = 1 + (theta+epsilon_N)/L,       epsilon_N -> 0.           (3)

Thus alpha_N is the quantity denoted beta_N^2 in the previous note.
For Re z>0 define

    B_N(z)=alpha_N integral_0^infinity
                      exp(-zt/N) M_u (p_t*) M_v dt,
    d_theta(z)=log z+gamma-theta,
    z_star=exp(theta-gamma),                                    (4)

where log is the principal logarithm and gamma is Euler's constant.
All time integrals of operators in this note are Bochner integrals.

## Theorem

For every compact K contained in {Re z>0} with z_star not in K,
I-B_N(z) is invertible for z in K and N sufficiently large, and

    sup_{z in K} || L^(-1) B_N(z)(I-B_N(z))^(-1)
                         - P/d_theta(z) ||
        <= C_K (L^(-1)+|epsilon_N|).                            (5)

There is also an actual signed renewal density. With operator convolution
in the time variable, set

    Q(t)=M_u (p_t*) M_v,
    R_N(t)=sum_{k>=1} alpha_N^k Q^{*k}(t),       t>=0.           (6)

The series converges in operator norm uniformly on bounded time intervals.
For compact K contained in {Re z>z_star}, its Laplace transform exists
in operator norm for all sufficiently large N, and

    integral_0^infinity exp(-zt) [N/L R_N(Nt)] dt
       = L^(-1) B_N(z)(I-B_N(z))^(-1).                          (7)

Consequently this transform converges locally uniformly to P/d_theta(z),
with the error in (5). In particular, for real z>z_star,

    L^(-1) integral_0^infinity exp(-zt)
             ell(N R_N(Nt)u)/m dt  ->  1/d_theta(z).            (8)

This is a pair-resolvent theorem for a fixed Brownian profile. It asserts
neither pointwise convergence of R_N(Nt) nor convergence of stochastic flows.

## Proof

### 1. Integrability and the sharp-time coefficient

The exponential envelope implies that f is bounded, integrable and has
all absolute polynomial moments. Also u,v belong to H and are bounded.
The semigroup p_t* is a contraction on H. Hence, with M=||f||_infinity,

    ||Q(t)|| <= M.                                               (9)

For t>=1, its Hilbert–Schmidt norm satisfies

    ||Q(t)|| <= ||Q(t)||_HS
              <= ||f||_1/(4 pi t),                              (10)

by bounding p_t pointwise by 1/(4 pi t). These estimates prove the
operator integrability in (2) and (4), including absolute integrability
of the operator norm in (4).

Let S_N(r)=integral_0^N p_t(r) dt. For r>0, substitution s=r^2/(4t)
gives S_N(r)=(4 pi)^(-1) E_1(r^2/(4N)). The identity

    E_1(q)=-gamma-log q+integral_0^q (1-exp(-s)) ds/s

follows by differentiating both sides and matching the constant at q=1.
For that constant, integration by parts in
Gamma'(1)=integral_0^infinity exp(-s)log s ds=-gamma gives

    integral_1^infinity exp(-s) ds/s
       + integral_0^1 (exp(-s)-1) ds/s = -gamma.

The integrations by parts are first performed from a positive lower
cutoff, and their logarithmic boundary terms cancel as the cutoff tends
to zero. Since 0<=1-exp(-s)<=s, it follows that

    S_N(r)=L/(4 pi)+g(r)+r_N(r),
    g(r)=(log 4-gamma-2 log r)/(4 pi),
    0<=r_N(r)<=r^2/(16 pi N).                                   (11)

The kernel u(x)g(x-y)v(y) defines a Hilbert–Schmidt operator K_f.
Indeed, in |x-y|<1 bound |f(y)| by C and integrate
(1+|log|x-y||)^2 over the unit disk, then integrate |f(x)|.
Outside that set use |g(x-y)|<=C'(1+|x|+|y|) and the second absolute
moments of f. In particular the integral

    I_f=integral integral f(x)g(x-y)f(y) dx dy                    (12)

is absolutely convergent, by Cauchy–Schwarz with measure
|f(x)f(y)| dx dy. The remainder in (11) has weighted Hilbert–Schmidt
norm at most

    (16 pi N)^(-1)
       [integral integral |f(x)f(y)| |x-y|^4 dx dy]^(1/2).

Therefore

    A_N=mu P+K_f/L+O(1/(NL))                                    (13)

in operator norm. Each term is compact: the first is rank one and the
other two have Hilbert–Schmidt kernels. Values of kernels on x=y do
not affect these operators.

For completeness, the elementary perturbation fact used here and below
is as follows. If P is a fixed bounded rank-one projection and b>0,
then for T=bP+E with ||E|| small, its spectrum has one simple
eigenvalue lambda near b, and the associated projection Pi satisfies

    ||Pi-P||=O(||E||),
    lambda=b+ell(Eu)/m+O(||E||^2),
    ||T(I-Pi)||=O(||E||).                                       (14)

To verify this, use the explicit resolvent

    (w-bP)^(-1)=w^(-1)(I-P)+(w-b)^(-1)P.

It is uniformly bounded outside fixed disjoint disks around 0 and b.
A Neumann series for I-(w-bP)^(-1)E excludes spectrum there. Integration
of the perturbed resolvent on |w-b|=b/4 gives a projection Pi within
O(||E||) of P. The resolvent identity gives this norm bound directly.
Projections at distance less than one have equal finite rank: restricting
one to the range of the other is injective, in each direction. Thus Pi
has rank one. Normalize its eigenvector as
w_E=m Pi u/ell(Pi u)=u+O(||E||). Applying ell to T w_E=lambda w_E
gives the middle formula in (14). Finally

    T(I-Pi)=E(I-Pi)+bP(P-Pi),

which proves the last formula. When T is real, the isolated eigenvalue
is real because the disk around b is conjugation invariant and contains
only one eigenvalue. It is positive for small E. The other spectrum lies
near zero, so this eigenvalue is dominant. All estimates are uniform
over perturbations bounded by a common small norm.

Apply (14) to (13). Since ell(K_f u)=I_f,

    Lambda_N=mu+I_f/(mL)+O(L^-2).                               (15)

This also checks the earlier main claim. For comparison with the full
unweighted operator L^(-1)(S_N*)M_f, take
X=L^(-1)(S_N*)M_v and Y=M_u. These are bounded, since convolution
by S_N has norm at most N. Then XY is the full operator and YX=A_N.
For bounded X,Y, the resolvent identity

    (w-XY)^(-1)=w^(-1)[I+X(w-YX)^(-1)Y],       w!=0,

and the same identity with X,Y interchanged show that their nonzero
spectra agree. On nonzero generalized eigenspaces X and Y are injective
intertwiners, so the algebraic multiplicities agree as well.

Writing eta=I_f/(m mu), equations (3) and (15) give

    alpha_N=(mu L)^(-1)
       [1+(theta+epsilon_N-eta)/L+O(L^-2)].                      (16)

Here and below N is large enough that epsilon_N is bounded.

### 2. Replacing the time cutoff by exponential damping

For Re z>0 put w_z(s)=exp(-zs)-1_{s<=1}. Directly subtracting the two
heat-kernel time integrals, and then substituting t=Ns, gives

    integral_0^infinity exp(-zt/N)p_t(r) dt - S_N(r)
       = (4 pi)^(-1) integral_0^infinity
                 w_z(s) exp(-r^2/(4Ns)) ds/s.                   (17)

Both sides are interpreted for r>0. The difference on the right is
absolutely integrable even with the spatial exponential removed.
For compact K in Re z>0 choose delta>0 and M_K<infinity such that
Re z>=delta and |z|<=M_K there. For 0<s<=1, the identity

    exp(-zs)-1=-zs integral_0^1 exp(-tzs) dt

implies |w_z(s)|<=M_K s. For s>1, |w_z(s)|<=exp(-delta s).

Define D(z)=integral_0^infinity w_z(s) ds/s. This is holomorphic
on Re z>0, by these bounds locally uniformly and the corresponding
derivative bounds. Differentiating under the integral gives D'(z)=-1/z.
The integration by parts calculation in Step 1 gives D(1)=-gamma.
The half-plane is connected, so

    D(z)=-gamma-log z.                                          (18)

For q>=0 the elementary inequality

    0<=1-exp(-q/s)<=min(1,q/s)<=sqrt(q/s)

now bounds the error in replacing exp(-q/s) by 1 in (17) by

    (4 pi)^(-1) sqrt(q)
       [M_K integral_0^1 s^(-1/2) ds
                    + integral_1^infinity exp(-delta s)s^(-3/2) ds]
       <= C_K sqrt(q).

With q=r^2/(4N), the error is at most C_K r/sqrt(N). Multiplication
by u(x),v(y), followed by the Hilbert–Schmidt estimate, gives an
operator error of size at most

    C_K N^(-1/2)
       [integral integral |f(x)f(y)||x-y|^2 dx dy]^(1/2).

Combining (11), (17) and (18) proves, locally uniformly on Re z>0,

    J_N(z):=integral_0^infinity exp(-zt/N)Q(t) dt
       = L mu P+K_f+mu(-gamma-log z)P+O_K(N^-1/2).              (19)

This derivation does not use a small-argument Bessel expansion.

### 3. The tuned inverse

Multiply (19) by (16). With a(z)=-gamma-log z, this gives

    B_N(z)=P+L^(-1)[K_f/mu
                      +(theta+epsilon_N-eta+a(z))P]+O_K(L^-2).
                                                                    (20)

The N^(-1/2)/L error is absorbed into O(L^-2). Apply (14), with b=1,
uniformly for z in K. Denote its eigenvalue and projection by b_N(z)
and Pi_N(z). Since ell(K_f u)/(m mu)=eta, equation (20) yields

    b_N(z)=1+[-d_theta(z)+epsilon_N]/L+O_K(L^-2),
    ||Pi_N(z)-P||<=C_K/L,
    C_N(z):=B_N(z)(I-Pi_N(z)),       ||C_N(z)||<=C_K/L.         (21)

Both cross products of C_N and Pi_N vanish. Thus

    (I-B_N)^(-1)
       = Pi_N/(1-b_N)+(I-C_N)^(-1)(I-Pi_N).                    (22)

If z_star is not in K, then |d_theta| is bounded below there:
log z=theta-gamma has only the solution z_star in Re z>0.
By (21), L(1-b_N) is consequently bounded away from zero for
large N, uniformly on K; also ||C_N||<1/2. Equation (22) proves
invertibility. Its second term is bounded uniformly, and

    [L(1-b_N(z))]^(-1)
       = d_theta(z)^(-1)+O_K(|epsilon_N|+L^-1).

It follows that

    L^(-1)(I-B_N(z))^(-1)
       = P/d_theta(z)+O_K(|epsilon_N|+L^-1).                   (23)

Finally B_N(I-B_N)^(-1)=(I-B_N)^(-1)-I. Subtracting I/L from
(23) proves (5).

### 4. An actual signed renewal density and its Laplace transform

By (9) and the volume of a time simplex, for k>=1,

    ||Q^{*k}(t)||<=M^k t^(k-1)/(k-1)!.

The sum (6) therefore converges locally uniformly in operator norm,
with bound alpha_N M exp(alpha_N M t).

Let H_N=Delta+alpha_N M_f, with domain H^2(R^2). It is self-adjoint
because Delta is self-adjoint and alpha_N M_f is a bounded real
potential. Its semigroup has the Duhamel expansion in the bounded
perturbation alpha_N M_f. Multiplying the expansion by alpha_N M_u
on the left and M_v on the right, and using M_v M_u=M_f between
successive heat operators, identifies every term with (6). The
simplex bound just proved justifies summation. Hence

    R_N(t)=alpha_N M_u exp(t H_N) M_v.                          (24)

To obtain the needed large-time bound without replacing f by |f|,
fix a real x_0>z_star and put q=x_0/N. Define

    T_q=(q-Delta)^(-1/2),
    X=sqrt(alpha_N) M_u T_q,
    Y=sqrt(alpha_N) T_q M_v.

Then XY=B_N(x_0), whereas

    YX=S_q=alpha_N T_q M_f T_q

is bounded and self-adjoint. The XY/YX identity proved in Step 1
shows that their nonzero spectra agree. For real x_0, (21) implies

    b_N(x_0)=1-[d_theta(x_0)-epsilon_N]/L+O(L^-2)<1,

and b_N(x_0)>1/2 for large N. All remaining spectrum of B_N(x_0)
has modulus at most ||C_N(x_0)||=O(1/L). Therefore

    sup spectrum(S_q)<=b_N(x_0)<1.

For every psi in H^1(R^2), let h=(q-Delta)^(1/2)psi. By functional
calculus T_q h=psi. The quadratic form identity gives

    <psi,(q-H_N)psi>
       =<h,(I-S_q)h>
       >=(1-b_N(x_0))||h||^2
       >=q(1-b_N(x_0))||psi||^2.

It follows that sup spectrum(H_N)<=q b_N(x_0)<q. In particular
the spectral theorem gives ||exp(tH_N)||<=exp(t sup spectrum(H_N)).
Equation (24) is thus Laplace integrable in operator norm whenever
Re z>x_0, with damping exp(-zt/N). For a compact K in Re z>z_star,
choose x_0 strictly between z_star and inf_{z in K} Re z. This
proves integrability for all z in K, with one sufficiently large N_0.

Write G=(z/N-H_N)^(-1) and R=(z/N-Delta)^(-1). Both exist in this
region. Integrating (24) by the spectral theorem gives

    integral_0^infinity exp(-zt/N)R_N(t) dt=alpha_N M_u G M_v.

The resolvent identity G=R+alpha_N R M_f G, multiplied by the same
outer factors, yields

    alpha_N M_u G M_v
       =B_N(z)+B_N(z)[alpha_N M_u G M_v].

Using invertibility from Step 3 proves that this integral equals
B_N(z)(I-B_N(z))^(-1). Changing variables t=Ns and dividing by L
proves (7). Applying the bounded functional T -> ell(Tu)/m, and
using ell(Pu)=m, proves (8).

No exchange of an infinite signed renewal sum with a critical Laplace
integral was assumed. The sum was first identified on finite time
intervals with a bounded-potential semigroup; its spectral upper bound
then justified the integral.

## Independent normalization checks

For r>0 and positive real z, another exact expression for the Laplace
heat kernel is

    integral_0^infinity exp(-zt/N)p_t(r) dt
       = (2 pi)^(-1) K_0(r sqrt(z/N)).                           (25)

Here K_0 may be defined by
K_0(w)=1/2 integral_0^infinity exp(-s-w^2/(4s)) ds/s, so (25)
follows directly by substitution. Its logarithmic constant is also
fixed by (17)–(18). Holomorphic continuation gives the same identity on
Re z>0, using the principal square root. It is checked against direct integration
in verify.py, independently of the operator argument.

For the signed covariance example f=2 phi_1-phi_2, where phi_s is the
planar centered Gaussian density of covariance s Id,

    4 pi integral integral f(x)p_t(x-y)f(y) dx dy
       =4/(t+1)-4/(t+3/2)+1/(t+2).

Gaussian convolution proves this formula. Its sharp-time integral has
renormalized limit log(81/32), verifying the old constant. Independently,
the planar logarithmic Gaussian moment
E log|Z_s|=(log(2s)-gamma)/2 gives the same value in (12).
The exponentially damped overlap can also be evaluated exactly:

    4 pi ell(J_N(z)u)
       =4 F(z/N)-4 F(3z/(2N))+F(2z/N),
    F(q)=exp(q) E_1(q).                                        (26)

This follows by integrating exp(-zt/N)/(t+b) and substituting s=t+b.
Its finite part, after subtracting log N, tends to

    log(81/32)-gamma-log z,

in agreement with (19). Both sides of the scalar identity (18),
the old constant, (25), and (26) are checked in verify.py.
These scalar calculations do not approximate an operator eigenvalue.

## Scope relative to the open conjecture

Hindy Drillick, Jonathan Hou and Shalin Parekh,
*A universality result for the critical 2d stochastic heat flow*,
[arXiv:2609.15832](https://arxiv.org/html/2609.15832v1),
leave the signed exponential spatial-kernel extension as Conjecture 1.17.
The theorem above addresses one transform-side pair estimate in its
Brownian, fixed-profile, positive-mass special case. The critical
coefficient is still the sharp-time Lambda_N; no retuning by the
absolute mass of f is made. The exponential damping changes the
denominator by gamma, not the definition of Lambda_N.

No inverse Laplace estimate uniform on unbounded vertical lines has
been proved here. Nor have spatial endpoints on diffusive scales,
arbitrary N-dependent profiles and gap processes, or third and fourth
moments been controlled. Thus (5)–(8) do not establish Conjecture 1.17
or define a critical KPZ field.
