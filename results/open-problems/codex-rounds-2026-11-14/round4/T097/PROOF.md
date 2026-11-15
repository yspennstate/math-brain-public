# A capacity bound using Euclidean distance from a cube

The field has simple-random-walk Green covariance on Z^3:

    g(x,y) = sum_{n>=0} P_x(X_n=y).

For integer R>=1 put B_R=[-R,R]^3 intersect Z^3 and

    p_R(h) = P(0 connects to boundary B_R in {phi>=h}),
    L_rel(t) = min{R>=1: p_R(h_*+t)<=p_R(h_*)/2}.

All connections are nearest-neighbor lattice connections, and logarithms
are natural. Define

    delta = sqrt(9-24/pi),
    C_cube = (2 pi delta)/(3 log((3+delta)/(3-delta))).       (1)

Then

    cap(B_R) <= C_cube (R+1/2),                            (2)
    C_cube <= 8/9+2 pi/3 < 3.                              (3)

Here capacity has the normalization determined by g. In particular (2)
strictly improves the preceding shell bound A_R>4R for every integer R>=2.
Together with the previously established critical arm estimate, (2) gives

    liminf_{t downarrow 0} t^2 log(1/t) L_rel(t)
        >= (log 2)^2/(8 C_cube) > (log 2)^2/24.             (4)

The earlier coefficient was (log 2)^2/32. The assertions concern upper
bounds on capacity and lower bounds on this specified relative radius.
They do not assert asymptotic equalities or any critical exponent.

## 1. Lattice capacity and its energy normalization

For finite K, write G_K=(g(x,y))_{x,y in K} and 1 for its all-one vector.
The matrix G_K is positive definite. To see this, kill the walk outside
a finite box U containing K. Its Green matrix is (I-P_U)^(-1), where
P_U is symmetric and has spectrum in (-1,1). Its Green eigenvalues are
at least 1/2. Passing to the principal submatrix on K and then increasing
U gives G_K >= (1/2)I.

Define e_K(x)=P_x(X_n not in K for all n>=1) for x in K. Transience and
the decomposition according to the last visit to K give G_K e_K=1.
Consequently

    cap(K) = sum_{x in K} e_K(x) = 1^T G_K^(-1)1.          (5)

For finitely supported f:Z^3 -> R put

    E_Z(f) = (1/6) sum_{x in Z^3} sum_{i=1}^3
                            (f(x+e_i)-f(x))^2.

Every unordered edge occurs once. Expanding shows E_Z(f)=f^T(I-P)f.
Minimizing in a finite box U with f=1 on K gives energy
`1^T ((G_U)_{K,K})^(-1)1`: the Euler equations say (I-P_U)f is supported
on K, and solving on K gives that formula. Increasing U and using
continuity of the inverse proves the bound

    cap(K) <= E_Z(f)  if f is finitely supported and f|_K=1. (6)

## 2. An exact transfer by averaging over unit cells

Let Q=[-1/2,1/2]^3 and let F:R^3 -> R be compactly supported and Lipschitz.
Define

    f(x) = integral_Q F(x+z) dz, x in Z^3.

The cell volume is one. The fundamental theorem of calculus along lines
and Jensen's inequality give, for each i,

    f(x+e_i)-f(x)
      = integral_Q integral_0^1 partial_i F(x+z+u e_i) du dz,

    (f(x+e_i)-f(x))^2
      <= integral_Q integral_0^1 |partial_i F(x+z+u e_i)|^2 du dz.

Lipschitz regularity suffices: the line identities hold almost everywhere,
and Fubini discards the exceptional lines. For each fixed u, the translated
cells x+Q+u e_i tile R^3 up to boundaries. Therefore summing first over x
and then over i gives

    E_Z(f) <= (1/6) integral_{R^3} |grad F(y)|^2 dy.         (7)

If F=1 on the solid cube Q_a=[-a,a]^3 with a=R+1/2, then f=1 on B_R.
It is finitely supported because F is compactly supported. Equations
(6) and (7) show that every such F supplies an upper bound on cap(B_R).
There is no limiting mesh argument or unestimated discretization error
in (7).

## 3. Energy of a profile depending on distance to the cube

Let a>0 and d_a(y) be the Euclidean distance from y to Q_a. It has the
explicit formula

    d_a(y)^2 = sum_{i=1}^3 (|y_i|-a)_+^2.

Outside Q_a, its gradient has norm one almost everywhere. For a function
F(y)=u(d_a(y)) with u(0)=1, the continuum energy is

    integral |grad F|^2 = integral_0^infinity S_a(s) u'(s)^2 ds,
    S_a(s) = 24a^2 + 12 pi a s + 4 pi s^2.                (8)

Here is a direct derivation that accounts for all geometric pieces.
Partition the exterior according to how many coordinates lie outside
[-a,a]. If one coordinate is outside, the six face regions give
`6(2a)^2 integral u'(s)^2 ds`. If two are outside, the twelve edge
regions have the remaining coordinate in an interval of length 2a;
polar coordinates in each positive quadrant give
`12(2a)(pi/2) integral s u'(s)^2 ds`. If all three are outside, the eight
corner octants combine into one full spherical integral
`4pi integral s^2 u'(s)^2 ds`. These are exactly (8). The separating
planes have zero volume, and grad F vanishes inside Q_a.

For T>0 define

    I_{a,T} = integral_0^T ds/S_a(s),
    u_{a,T}(s) = 1 - (integral_0^s dr/S_a(r))/I_{a,T}, 0<=s<=T,
    u_{a,T}(s) = 0, s>=T.

The associated F is compactly supported, Lipschitz, and one on Q_a.
Substitution into (8) gives the exact energy

    integral |grad F|^2 = 1/I_{a,T}.                      (9)

This is the minimum among absolutely continuous distance profiles
with u(0)=1 and u(T)=0. Indeed Cauchy-Schwarz gives

    1 = (integral_0^T -u'(s) ds)^2
      <= (integral_0^T S_a(s)u'(s)^2 ds) I_{a,T},

with equality precisely for -u' proportional to 1/S_a. Thus the
optimization is exact in this continuum distance-profile class. No
optimality over all continuum or lattice trial functions is asserted.

Take a=R+1/2. Applying (7) to these finite-T functions and then letting
T tend to infinity gives

    cap(B_R) <= 1/(6 I_a),
    I_a = integral_0^infinity ds/S_a(s).                  (10)

The integral is positive and finite since S_a is positive and quadratic.
The finite-T argument avoids applying (6) to a trial function of infinite
support.

## 4. Evaluation and comparison of the constant

On substituting s=av,

    I_a = J/a,
    J = integral_0^infinity dv/(24+12pi v+4pi v^2).

Put b_-=(3-delta)/2 and b_+=(3+delta)/2. Since 8/3<pi,
we have 0<delta<3 and both b_-,b_+ are positive. Factoring gives

    24+12pi v+4pi v^2 = 4pi (v+b_-)(v+b_+).

Partial fractions now give

    J = log(b_+/b_-)/(4pi delta),
    1/(6J) = C_cube.

Equations (10) and (1) prove (2).

For an upper bound without logarithms, use the untruncated profile
`u(s)=b/(b+s)`, where b=lambda a and lambda>0. Its weighted energy is
finite. Its finite-T truncations

    u_T(s) = (u(s)-u(T))/(1-u(T)), 0<=s<=T;
    u_T(s) = 0, s>=T

have energies tending to that of u, so they are admissible for the infimum
in (10). With v=s/a, direct integration gives

    (1/(6a)) integral_0^infinity S_a(s)u'(s)^2 ds
      = 4/(3lambda) + pi/3 + (2pi lambda)/9.              (11)

For verification, the three needed integrals are

    integral_0^infinity (lambda+v)^(-4) dv = 1/(3lambda^3),
    integral_0^infinity v(lambda+v)^(-4) dv = 1/(6lambda^2),
    integral_0^infinity v^2(lambda+v)^(-4) dv = 1/(3lambda).

Taking lambda=3/2 in (11), minimality of (10) gives

    C_cube <= 8/9+2pi/3 < 8/9+44/21 = 188/63 < 3,

where pi<22/7 was used. This proves (3). If R>=2,
`C_cube(R+1/2)<3R+3/2<4R`, proving the stated strict improvement
over A_R>4R. For R=1, use the smaller of (2) and the preceding shell
bound; no improvement at that radius is claimed.

## 5. Gaussian comparison and the critical arm input

For a finite Gaussian vector with covariance G_K, put
`a_K=1^T G_K^(-1)1`. Let P be its centered law and Q the law with mean
-t1. For an event D set p=P(D), q=Q(D), and s=t sqrt(a_K). Under Q the
likelihood L=dP/dQ has moments

    E_Q L^r = exp(r(r-1)s^2/2), r>1.

This follows by writing log L=sZ-s^2/2 with Z standard normal under Q.
Holder's inequality gives

    p <= q^((r-1)/r) exp((r-1)s^2/2),
    q/p >= exp[-log(1/p)/(r-1)-r s^2/2].

For s>0 choose `r-1=sqrt(2 log(1/p))/s`; the case s=0 is immediate.
For the lattice connection event on B_R this yields

    p_R(h+t)/p_R(h)
      >= exp[-t sqrt(2 cap(B_R) log(1/p_R(h)))
              -t^2 cap(B_R)/2].                         (12)

Finite-dimensional nondegeneracy gives 0<p_R(h)<1, so all expressions
are defined. The event is measurable on B_R by stopping a path at its
first visit to the boundary.

The external input is Stephen Muirhead, *Percolation of strongly correlated
Gaussian fields II. Sharpness of the phase transition*,
[arXiv:2206.10724v2](https://arxiv.org/html/2206.10724v2), Theorems 1.2
and 1.10. With ell=-h, alpha=1 and d=3 these give, for every q>4,

    theta(h_*-u) >= c_q u^q for all sufficiently small u>0, (13)

and, for fixed t>0 and some c_t>0,

    p_R(h_*+t) <= exp(-c_t R^(1/2)).                    (14)

The endpoint q=4 is not used. To recover the earlier critical arm bound
without any exponent assumption, take u=R^(-1/2). At level h_*-u the
arm probability is at least c_q R^(-q/2). Equation (2) bounds
`u^2 cap(B_R)` uniformly. Equation (12), and monotonicity in p of
`p exp[-s sqrt(2 log(1/p))-s^2/2]`, therefore give

    -log p_R(h_*) <= (q/2)log R + O_q(sqrt(log R)).

For every epsilon>0 choose q=4+epsilon and absorb the subleading term.
Thus, for all sufficiently large R,

    log(1/p_R(h_*)) <= (2+epsilon) log R.               (15)

This reproduces the earlier arm estimate and does not strengthen its
power. It does not assume absence of percolation at h_*.

## 6. Improved coefficient for the relative radius

Write C=C_cube and fix c<(log 2)^2/(8C). Choose epsilon>0 sufficiently
small that

    sqrt(4 C c (2+epsilon)) < log 2.                    (16)

Let R_epsilon>=2 be large enough for (15). Put H=log(1/t) and
M=c/(t^2 H). For sufficiently small t, M>=R_epsilon and log M<=2H.
For every integer R in [R_epsilon,M], equations (2) and (15) give

    t^2 cap(B_R) <= Cc/H + Ct^2/2,
    log(1/p_R(h_*)) <= 2(2+epsilon)H.

By (12) the negative logarithm of the lower bound on the ratio is at most

    sqrt[(Cc/H+Ct^2/2) 4(2+epsilon)H]
       + (Cc/H+Ct^2/2)/2.

It tends to sqrt(4 C c (2+epsilon)) as t decreases to zero. By (16),
the ratio is strictly greater than 1/2 uniformly in every such R. For
each of the finitely many R<R_epsilon, the ratio tends to one: dominated
convergence applies to the translated Gaussian density. Its denominator
is strictly positive. Thus these radii also have ratio greater than 1/2
for all sufficiently small t.

Consequently L_rel(t)>floor(M), whenever L_rel is defined. It is finite:
combine (14) and (15) with epsilon=1 to bound the ratio by
`R^3 exp(-c_t R^(1/2))`, which tends to zero for each fixed t>0.
Multiplying L_rel(t)>floor(M) by t^2H and taking the liminf gives a bound
at least c; increasing c to (log 2)^2/(8C) proves (4).

No monotonicity in R of the probability ratio has been used. The endpoint
constant is a liminf bound, not a finite-t assertion or an asymptotic value.

## 7. Scope

The improvement comes from a smaller deterministic energy bound, obtained
by a profile that is not constant on sup-norm shells. It leaves the power
t^(-2) and the logarithmic loss unchanged. It gives neither a connection-
specific improvement of the Gaussian score nor a comparison of L_rel to
a crossing or two-point correlation length. Critical nonpercolation,
existence of lattice critical exponents, their values, and equality with
cable-system exponents remain unresolved by this argument.
