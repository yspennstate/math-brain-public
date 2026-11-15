# Uniform Brownian pair limits for moving signed profiles

Let C,a,m_0 be positive, and let F be the class of real measurable
functions f on R^2 satisfying

    |f(x)| <= C exp(-a|x|) almost everywhere,
    m_f := integral f(x) dx >= m_0.                            (1)

Assume F is nonempty. All operators act on H=L^2(R^2;C), and all
operator norms below are on H. Put

    p_t(x)=(4 pi t)^(-1) exp(-|x|^2/(4t)),
    u_f=sqrt(|f|),       v_f=sgn(f)u_f,
    ell_f(h)=integral v_f(x)h(x) dx,
    P_f=u_f tensor v_f/m_f,       mu_f=m_f/(4 pi).

Here a tensor b sends h to a integral conjugate(b)h. The generator of
p_t* is Delta. Write M_w for multiplication by w and define

    Q_f(t)=M_u exp(t Delta) M_v,
    T_{N,f}=L^-1 integral_0^N Q_f(t) dt,       L=log N.         (2)

Subscripts f on u,v are suppressed in formulas with a fixed f.
All time integrals are Bochner integrals in operator norm.

## Theorem

There is N_0 depending only on C,a,m_0 such that, for every f in F and
N>=N_0, T_{N,f} has a unique dominant positive algebraically simple
eigenvalue Lambda_N(f). This is also the dominant eigenvalue of
the unweighted operator

    h -> L^-1 integral S_N(x-y)f(y)h(y)dy,
    S_N(x)=integral_0^N p_t(x)dt.                             (3)

Fix theta in R and a nonnegative sequence e_N tending to zero. For
f in F and real |epsilon|<=e_N use the original sharp-time tuning

    alpha=alpha_N(f,epsilon)
          =[1+(theta+epsilon)/L]/[L Lambda_N(f)].              (4)

It is positive for all sufficiently large N, uniformly in f and epsilon.
Define operator convolution in time with the indicated order of factors,
and set

    R_{N,f,epsilon}(t)=sum_{k>=1} alpha^k Q_f^{*k}(t),
    F_{N,f,epsilon}(t)=N R_{N,f,epsilon}(Nt)/L.                (5)

Let gamma be Euler's constant, z_*=exp(theta-gamma), and

    g_theta(t)=integral_0^infinity z_*^s t^(s-1)/Gamma(s) ds,
                       t>0.                                  (6)

For every 0<delta<T<infinity,

    sup_{f in F, |epsilon|<=e_N} sup_{delta<=t<=T}
         ||F_{N,f,epsilon}(t)-g_theta(t)P_f|| -> 0.           (7)

For b>z_* and every continuous complex psi on [0,infinity) having a
finite limit at infinity, there is also the uniform time-test limit

    sup_{f in F, |epsilon|<=e_N}
      ||integral_0^infinity psi(t)e^(-bt)F_{N,f,epsilon}(t)dt
           - P_f integral_0^infinity psi(t)e^(-bt)g_theta(t)dt||
             -> 0.                                          (8)

In particular, (7) and (8) apply to arbitrary sequences f_N in F,
without any convergence of the profiles or of P_{f_N}. The gap process
in this theorem remains Brownian with generator Delta.

## Proof

### 1. Bounds independent of the profile

Polar coordinates and the gamma integral give, for each integer k>=0,

    integral |x|^k |f(x)| dx <= M_k,
    M_k=2 pi C (k+1)!/a^(k+2).                                (9)

Consequently m_0<=m_f<=M_0, ||u||_2=||v||_2<=sqrt(M_0), and

    P_f^2=P_f,
    ||P_f||=||f||_1/m_f<=kappa:=M_0/m_0,
    ||I-P_f||<=1+kappa,
    mu_-:=m_0/(4 pi)<=mu_f<=mu_+:=M_0/(4 pi).                 (10)

For k=2,4, the inequality |x-y|^k<=2^(k-1)(|x|^k+|y|^k) yields

    integral integral |f(x)f(y)||x-y|^k dx dy
        <=2^k M_0 M_k.                                      (11)

The heat contraction and its pointwise kernel bound give

    ||Q_f(t)||<=C,
    ||Q_f(t)||<=||Q_f(t)||_HS<=M_0/(4 pi t),       t>0.        (12)

These prove integrability in (2) and in the damped free resolvents used
below. The maps are norm-continuous for t>0, hence Bochner measurable;
no assertion of norm continuity at t=0 is needed.

Define for r>0

    k(r)=(log 4-gamma-2 log r)/(4 pi),
    K_f(x,y)=u(x)k(|x-y|)v(y),
    I_f=integral integral f(x)k(|x-y|)f(y) dx dy.              (13)

There is a common bound ||K_f||_HS<=K_0. To verify it, on |x-y|<1
use |f(y)|<=C and |k(r)|<=c_0(1+|log r|). The resulting bound is

    C M_0 c_0^2 integral_{|z|<1}(1+|log|z||)^2 dz<infinity.

Here the polar integral is 2 pi integral_0^1 r(1-log r)^2 dr,
which is finite. On |x-y|>=1, use
|k(|x-y|)|<=c_1(1+|x|+|y|), square it, and use M_0,M_2.
The constants c_0,c_1 are numerical. Thus K_0 depends only on C,a.
Weighted Cauchy–Schwarz now gives absolute convergence and the bound

    |I_f|<=M_0 K_0.                                         (14)

### 2. The sharp-time expansion and a uniform perturbation argument

Substitution s=r^2/(4t) gives

    S_N(r)=(4 pi)^-1 E_1(r^2/(4N)),
    E_1(q)=integral_q^infinity e^-s ds/s.

The identity

    E_1(q)=-gamma-log q+integral_0^q(1-e^-s)ds/s

follows by differentiation and matching the constant. For the latter,
integration by parts in Gamma'(1)=-gamma gives

    integral_1^infinity e^-s ds/s
       + integral_0^1(e^-s-1)ds/s=-gamma.

One may first integrate from a positive cutoff; the logarithmic boundary
terms cancel when it decreases to zero. Since 0<=1-e^-s<=s,

    S_N(r)=L/(4 pi)+k(r)+r_N(r),
    0<=r_N(r)<=r^2/(16 pi N).                                (15)

Equations (11) and (15), applied to the weighted kernels, give

    T_{N,f}=mu_f P_f+K_f/L+E_{N,f},
    ||E_{N,f}||<=sqrt(16 M_0 M_4)/(16 pi N L).               (16)

Each term is compact: K_f and the remainder are Hilbert–Schmidt, and
the leading term has rank one. Values of kernels on x=y are immaterial.

Here is the uniform perturbation fact required for (16). For any P=P_f,
mu=mu_f and a bounded error E,

    (w-mu P)^-1=w^-1(I-P)+(w-mu)^-1 P.                       (17)

Let r=mu_-/4. Outside the disks |w|<r and |w-mu|<r, (17) is bounded
by (1+2 kappa)/r. For small ||E||, with a threshold independent of f,
the resolvent Neumann series excludes spectrum of mu P+E there.
On the circle |w-mu|=r it also gives, by integration and the resolvent
identity, a Riesz projection Pi satisfying

    ||Pi-P||<=c_2||E||.                                     (18)

The circle length and all resolvent bounds are common. Choose the error
threshold so that this difference is less than 1. Two projections at
distance less than 1 have equally dimensional ranges: restriction of
one to the range of the other is injective, in both directions. Hence
Pi has rank one. There is a unique algebraically simple eigenvalue
lambda near mu. For a real operator this eigenvalue is real, since
complex conjugation preserves its disk and its spectrum.

To obtain a uniform first-order expansion, normalize its eigenvector by

    w_E=m_f Pi u/ell_f(Pi u).

Since ell_f(u)=m_f>=m_0, the denominator differs from m_f by at most
M_0||Pi-P||. After decreasing the common error threshold it is bounded
below in absolute value by m_0/2. Equations (10),(18) then give
||w_E-u||<=c_3||E|| and ell_f(w_E)=m_f. Applying ell_f to the
eigenvalue equation yields

    lambda=mu_f+ell_f(Eu)/m_f+O(||E||^2).                     (19)

Every constant here depends only on the class bounds. Moreover

    ||(mu_f P_f+E)(I-Pi)||
       <=||E||||I-Pi||+mu_f||P_f||||P_f-Pi||=O(||E||).        (20)

The spectral complement is thus small in norm. In particular lambda
is positive and dominant when ||E|| is below a common threshold.
Applying (19) to (16), and using ell_f(K_f u)=I_f, proves uniformly

    Lambda_N(f)=mu_f+I_f/(m_f L)+O(L^-2).                    (21)

The O((NL)^-1) error in (16) is absorbed here since L<=N.

To check that this is exactly the coefficient in (3), let S_N* denote
convolution and take X=L^-1(S_N*)M_v, Y=M_u. They are bounded since
||S_N*||<=N. Then XY is (3), while YX=T_{N,f}. For w!=0,

    (w-XY)^-1=w^-1[I+X(w-YX)^-1Y],                           (22)

when the right side exists. Multiplication verifies the identity, and
interchanging X,Y proves equality of their nonzero spectra. The
operators X,Y intertwine the generalized eigenspaces at any nonzero
eigenvalue and are injective there: for instance Yh=0 implies XYh=0,
whereas XY is invertible on such a generalized eigenspace. The two
injections give equal algebraic multiplicities. Both operators are
compact. For the unweighted one this follows from

    ||kernel||_2^2=L^-2 ||S_N||_2^2 ||f||_2^2<infinity.

Indeed S_N is logarithmic at zero, and E_1(q)<=e^-q/q bounds its tail.
This proves (3) without redefining Lambda_N.

### 3. Uniform free resolvent and tuned inverse

Fix a real z>0 and write

    J_{N,f}(z)=integral_0^infinity e^(-zt/N)Q_f(t)dt,
    B_{N,f,epsilon}(z)=alpha J_{N,f}(z).

The symbol J_{N,f}(z) here denotes a resolvent integral, not a sign
multiplier. Subtract the sharp-time integral, substitute t=Ns, and set
w_z(s)=e^(-zs)-1_{s<=1}. Its scalar kernel difference is

    (4 pi)^-1 integral_0^infinity
        w_z(s)e^(-r^2/(4Ns)) ds/s.                            (23)

The integral with the spatial exponential removed equals
-gamma-log z. Differentiating in z gives -1/z and its value at z=1
is the gamma identity above. These operations are justified by
|w_z(s)|<=zs for s<=1 and |w_z(s)|<=e^(-zs) for s>1.
Using 1-e^-q<=sqrt(q) for q>=0 bounds the error in (23) by

    (4 pi)^-1 [r/(2 sqrt(N))]
      [2z+integral_1^infinity e^(-zs)s^(-3/2)ds].              (24)

The weighted Hilbert–Schmidt error is at most a constant times
N^-1/2 sqrt(4 M_0 M_2), by (11). Combining with (16) proves

    J_{N,f}(z)=L mu_f P_f+K_f
                  +mu_f(-gamma-log z)P_f+O_z(N^-1/2).        (25)

All error constants are independent of f and, for z in a fixed compact
subset of (0,infinity), independent of z as well.

Put eta_f=I_f/(m_f mu_f), which is uniformly bounded by (10),(14).
For large N, e_N<=1. Inverting (21) in (4) gives, uniformly for the
allowed f,epsilon,

    alpha=(mu_f L)^-1
        [1+(theta+epsilon-eta_f)/L+O(L^-2)].                  (26)

With d(z)=log z+gamma-theta, multiplication gives

    B(z)=P_f+L^-1[K_f/mu_f
              +(theta+epsilon-eta_f-gamma-log z)P_f]
              +O_z(L^-2).                                  (27)

Apply the same uniform perturbation argument at the eigenvalue 1 of
P_f. It gives a rank-one Riesz projection Pi(z), an eigenvalue b_N(z)
and a complementary operator C_N(z) such that

    b_N(z)=1+[-d(z)+epsilon]/L+O_z(L^-2),
    ||Pi(z)-P_f||=O_z(L^-1),
    B(z)=b_N(z)Pi(z)+C_N(z),
    ||C_N(z)||=O_z(L^-1),       Pi C_N=C_N Pi=0.              (28)

The cancellation in its first line is exact at first order, because
ell_f(K_f u)/(m_f mu_f)=eta_f. For real z>z_*, d(z)>0. For large N,
uniformly in f,epsilon, b_N(z)<1 and ||C_N(z)||<1/2. Therefore

    L^-1 B(z)(I-B(z))^-1
       =P_f/d(z)+O_z(L^-1+e_N).                             (29)

In detail, decompose the inverse as

    (I-B)^-1=Pi/(1-b_N)+(I-C_N)^-1(I-Pi).

The second term is uniformly bounded, and
1/[L(1-b_N)]=1/d(z)+O_z(e_N+L^-1). Subtracting I/L from the inverse
divided by L proves (29). This argument uses a common threshold in N,
not a threshold chosen after fixing a profile.

### 4. Uniform spectral upper bound and actual renewal transforms

For a fixed real c>z_* put q=c/N and

    H_{N,f,epsilon}=Delta+alpha M_f,
    U_q=(q-Delta)^-1/2,
    X=sqrt(alpha) M_u U_q,
    Y=sqrt(alpha) U_q M_v.

H is self-adjoint on H^2 because alpha f is real and bounded. We have
XY=B(c), while YX=alpha U_q M_f U_q is self-adjoint. Identity (22)
gives equality of their nonzero spectra. By (28), the largest spectral
value of YX is at most b_N(c)<1, uniformly for large N: b_N(c)>1/2,
and all other nonzero spectral values have modulus O_c(L^-1).
For psi in H^1 and h=(q-Delta)^1/2 psi, quadratic forms give

    <psi,(q-H)psi>=<h,(I-YX)h>
       >=(1-b_N(c))||h||^2
       >=q(1-b_N(c))||psi||^2.

It follows, uniformly for large N, that

    sup spectrum(NH)<=c b_N(c)<c.                            (30)

The simplex bound from (12) is

    ||Q_f^{*k}(t)||<=C^k t^(k-1)/(k-1)!.

Thus (5) converges uniformly on bounded time intervals, for each N.
The bounded-potential Duhamel expansion, using M_v M_u=M_f, gives

    R_{N,f,epsilon}(t)=alpha M_u exp(tH)M_v.                  (31)

For any real z>z_*, choose c strictly between z_* and z. Equation (30)
shows that (31) is integrable with damping e^(-zt/N), in operator norm.
The resolvent identity for (z/N-H)^-1, sandwiched by alpha M_u and
M_v, gives B(z)(I-B(z))^-1. Changing variables in time and using
(29) proves the uniform estimate

    ||integral_0^infinity e^-zt F_{N,f,epsilon}(t)dt
                    -P_f/d(z)||<=c_z(L^-1+e_N).             (32)

Finite-time convergence of the signed series alone would not justify
this integral. The separate spectral bound (30) supplies that step.

### 5. Scalar density and uniform positive time-test estimates

The density in (6) is finite and continuous for t>0. Near s=0 use
1/Gamma(s)=s/Gamma(s+1)=O(s). For s>=1, restricting the defining gamma
integral to [s,s+1] gives

    Gamma(s)>=e^(-(s+1))s^(s-1).

For t in a compact subset of (0,infinity), the integrand of (6) is
therefore bounded for large s by a constant times s(e z_* T/s)^s.
This is integrable and proves continuity by dominated convergence.
For z>z_*, positivity, Tonelli and the gamma integral give

    integral_0^infinity e^-zt g_theta(t)dt
        =integral_0^infinity (z_*/z)^s ds=1/d(z).             (33)

In particular the damped density is integrable even near t=0.

Define j_f(x)=sgn(f(x)) for f(x)!=0 and j_f(x)=1 otherwise. Set

    J_f=M_{j_f},       A_f=P_f J_f=u tensor u/m_f.

J_f is a self-adjoint unitary, A_f is positive and ||A_f||<=kappa.
Moreover A_f J_f=P_f. From (31),

    S_{N,f,epsilon}(t):=F_{N,f,epsilon}(t)J_f
         =(N alpha/L)M_u exp(tNH)M_u >=0.                    (34)

Fix b>z_* and choose c in (z_*,b). For all sufficiently large N,
(30) and the spectral theorem show that

    D_{N,f,epsilon}(t):=e^-bt S_{N,f,epsilon}(t)

is positive and decreasing in the order of self-adjoint operators.
Indeed exp(t(NH-b)) decreases at every spectral value lambda<=c<b;
sandwiching with M_u preserves the order. No commutation with M_u
is used. For each fixed N its operator norm is integrable, including
at zero, by (30) and boundedness of M_u.

Define its moving comparison density by

    D_f^0(t)=h_b(t)A_f,       h_b(t)=e^-bt g_theta(t).          (35)

Right multiplication of (32) by J_f gives uniform convergence of the
total masses of D_{N,f,epsilon} to A_f/d(b). Their norms are bounded
by a common constant. The total masses of D_f^0 have the same common
bound by (33) and ||A_f||<=kappa.

For a real bounded measurable r, positivity gives

    -||r||_infinity integral D <= integral r(t)D(t)dt
                                  <=||r||_infinity integral D,
    ||integral r(t)D(t)dt||
                <=||r||_infinity ||integral D||,             (36)

for either D=D_{N,f,epsilon} or D=D_f^0. The estimate uses the norm
of the positive total mass, not an integral of operator norms.

Let psi be real continuous with a finite limit at infinity. The function
x -> psi(-log x), with that limit at x=0, is continuous on [0,1].
Given rho>0, approximate it uniformly by a real polynomial p. Thus

    sup_{t>=0}|psi(t)-p(e^-t)|<rho.

For p(x)=sum_{k=0}^K a_k x^k, (32) at b+k and (33) show that

    sup_{f,epsilon}
      ||integral p(e^-t)[D_{N,f,epsilon}(t)-D_f^0(t)]dt|| -> 0.

The same single polynomial works for every f. The two errors in
replacing p(e^-t) by psi are at most a common constant times rho,
by (36). Taking N to infinity and then rho to zero proves

    sup_{f,epsilon}
       ||integral psi(t)[D_{N,f,epsilon}(t)-D_f^0(t)]dt||->0. (37)

For complex psi apply this separately to real and imaginary parts.
Since ||J_f||=1 and A_f J_f=P_f, (37) proves (8), even when the sign
multiplier has no limit.

### 6. Uniform reconstruction with moving targets

The comparison family (35) is uniformly norm-continuous on every
compact positive time interval, since

    ||D_f^0(s)-D_f^0(t)||<=kappa |h_b(s)-h_b(t)|.             (38)

Fix t>0 and rho>0. By continuity of h_b choose 0<h<t, independently
of f, such that the right side of (38) is less than rho whenever
|s-t|<h. Choose nonnegative continuous functions phi_- and phi_+,
each of integral one, supported in (t-h,t) and (t,t+h), respectively.
Monotonicity of D_{N,f,epsilon} gives

    integral phi_+(s)D_{N,f,epsilon}(s)ds
       <=D_{N,f,epsilon}(t)
       <=integral phi_-(s)D_{N,f,epsilon}(s)ds.                (39)

By (37), these two averages differ from their moving comparison
averages by less than rho for all f,epsilon and all sufficiently
large N. By (38), each comparison average differs from D_f^0(t)
by less than rho. In the order on self-adjoint operators, (39) then
implies

    -2 rho I <= D_{N,f,epsilon}(t)-D_f^0(t) <= 2 rho I.

Thus the norm difference tends to zero uniformly over f,epsilon for
each fixed t>0. This argument never asks A_f or J_f to converge.

For [delta,T], choose a finite partition delta=t_0<...<t_k=T such
that kappa |h_b(s)-h_b(t)|<rho for any two points of a partition
interval. By the fixed-time conclusion, for all sufficiently large N
all endpoint errors are less than rho simultaneously, uniformly over
f,epsilon. For t_i<=t<=t_{i+1}, monotonicity gives

    D_{N,f,epsilon}(t_{i+1})<=D_{N,f,epsilon}(t)
                              <=D_{N,f,epsilon}(t_i).

Subtract D_f^0(t) and use the endpoint errors and (38). The difference
lies between -2 rho I and 2 rho I. Hence its norm is at most 2 rho
uniformly on [delta,T], f and epsilon. Multiply by e^bt, bounded on
this interval, and on the right by J_f. Equations (34),(35) yield (7).

## Independent checks and the role of the lower mass bound

The first-order denominator can also be checked without using the
Riesz projection in (28). Relative to the bounded direct sum
range(P_f) plus ker(P_f), let M=I-B(z) have blocks a,b,c,D. Formula
(27) and P_f K_f P_f=(I_f/m_f)P_f give

    a=[d(z)-epsilon]/L+O_z(L^-2),
    ||b||+||c||=O_z(L^-1),       D=I+O_z(L^-1).

All direct-sum coordinate maps have norms bounded by (10).
Thus D^-1 is uniformly bounded, and its Schur complement satisfies

    a-b D^-1 c=[d(z)-epsilon]/L+O_z(L^-2).

The block inverse divided by L has leading term P_f/d(z) and all
other terms tending uniformly to zero. This independently checks
(29) and the absence of a profile-dependent change to theta.

For a family without a positive lower mass bound, the constants in
(10) need not remain bounded. For example, phi_s is the centered
planar Gaussian density with covariance s Id. The profiles

    f_delta=(1+delta)phi_1-phi_2,       0<delta<=1,

share an exponential envelope, but have mass delta. In fact

    ||f_delta||_1=delta+1/[2(1+delta)],
    ||P_{f_delta}||=1+1/[2 delta(1+delta)] -> infinity.

To check the absolute mass directly, for A>B>0 the function
A phi_1-B phi_2 changes sign at r^2=4 log(2A/B). Its negative
tail has mass B exp(-r^2/4)-A exp(-r^2/2)=B^2/(4A).
Thus its absolute mass is A-B+B^2/(2A). Apply this with
A=1+delta,B=1 to obtain the formulas. The proof does not cover
this family with delta tending to zero. This observation is a limitation
of the uniform result, not a counterexample to Conjecture 1.17.

The family f_b=(1+b)phi_1-b phi_2, 0<=b<=3, has mass 1 and a common
envelope, for instance C=(4e^(1/2)+(3/2)e)/(2 pi), a=1, since

    exp(-r^2/(2s))<=exp(s/2)exp(-r).

It allows changing sign, changing negative mass, and nonconvergent
sequences. Gaussian convolution and Gaussian logarithmic moments
independently give

    4 pi I_{f_b}=2b(1+b)log(3/2)-b^2 log 2,                  (40)
    4 pi integral integral f_b(x)p_t(x-y)f_b(y)dxdy
      =(1+b)^2/(t+1)-2b(1+b)/(t+3/2)+b^2/(t+2).             (41)

For (40), the difference of two Gaussians has covariance (s+t)Id,
and E log|Z_v|=(log(2v)-gamma)/2, so E k(|Z_v|)=log(2/v)/(4 pi).
Summing with the coefficients (1+b),-b gives (40). For (41), the
heat kernel has covariance 2t Id, so the Gaussian overlap for component
variances s_1,s_2 equals 1/[2 pi(s_1+s_2+2t)]; summing gives (41).
Integrating
(41) sharply and subtracting log N gives

    -2b(1+b)log(2/3)+b^2 log(1/2),

again (40). At b=1 it is log(81/32). More explicitly, if H_b is the
right side of (41), then

    integral_0^N H_b(t)dt-log N-4 pi I_{f_b}
      =(1+b)^2 log(1+1/N)
           -2b(1+b)log(1+3/(2N))+b^2 log(1+2/N).

Using log(1+x)<=x, its absolute value is at most
(1+5b+6b^2)/N<=70/N for 0<=b<=3. Applying the preceding absolute-mass
calculation with A=1+b,B=b also gives

    ||P_{f_b}||=1+b^2/[2(1+b)]<=17/8.

The b=0 formula follows directly by nonnegativity. The scalar script
verify.py checks both constant routes, the envelope moments, these
absolute-mass formulas, and the gamma shift. These checks are not a
numerical approximation to an operator eigenvalue.

## Scope

Hindy Drillick, Jonathan Hou and Shalin Parekh,
*A universality result for the critical 2d stochastic heat flow*,
[arXiv:2609.15832](https://arxiv.org/html/2609.15832v1), formulate the
signed exponential spatial-kernel extension as Conjecture 1.17.
The result here makes the Brownian signed pair theorem uniform over
moving profiles with a common envelope and a positive lower mass bound.
The same sharp-time Lambda_N is used for each profile.

No discrete gap process, non-Brownian continuum gap process, diffusive
spatial endpoint limit, third or fourth moment convergence, or convergence
of the stochastic flows is proved here. No estimate uniform down to
zero time and no rate for (7) is asserted. The argument neither takes
a logarithm of a singular flow nor constructs a critical KPZ field.
