# The leading lattice cube-capacity coefficient

Let P be the transition matrix of simple random walk on Z^3 and let
g(x,y)=sum_{n>=0} P^n(x,y). All capacities below use this Green-function
normalization. For an integer R>=1 set

    B_R = [-R,R]^3 intersect Z^3,    Q_a = [-a,a]^3.

Define the continuum variational quantity

    kappa = inf { (1/6) integral_{R^3} |grad F|^2 :
                  F compactly supported and Lipschitz, F=1 on Q_1 }.

There is no assertion that kappa has an elementary closed form. This
definition fixes its normalization, including the factor 1/6.

## 1. Statements

For every integer R>=1,

    kappa R <= cap(B_R) <= kappa (R+1/2).                 (1)

In particular,

    0 <= cap(B_R)-kappa R <= kappa/2,                    (2)
    lim_{R->infinity} cap(B_R)/R = kappa.                (3)

Thus kappa is the smallest possible leading coefficient in a bound
cap(B_R)<=D R+o(R).

The distance-profile coefficient of the preceding report is strictly
larger than kappa. More explicitly, put

    delta = sqrt(9-24/pi),
    C = 2 pi delta / [3 log((3+delta)/(3-delta))],
    D = 24+16 pi,
    C_1 = C - 486 pi^2 C^2/D^4.

Then

    2 pi/3 <= kappa <= C_1 < C < 3.                     (4)

For nearest-neighbor lattice connections let

    p_R(h) = P(0 connects to boundary B_R in {phi>=h}),
    L_rel(t) = min{R>=1: p_R(h_*+t)<=p_R(h_*)/2}.

Using the same density input as the previous reports, L_rel(t) is finite
for t>0 and

    liminf_{t downarrow 0} t^2 log(1/t) L_rel(t)
      >= (log 2)^2/(8 kappa)
      >= (log 2)^2/(8 C_1) > (log 2)^2/(8 C).           (5)

No critical exponent or equivalence with another correlation length is
asserted.

## 2. The lattice variational formula

For a finite nonempty K let G_K=(g(x,y))_{x,y in K}. Then

    cap(K) = 1^T G_K^(-1)1
           = inf { E_Z(f): f finitely supported, f=1 on K },
    E_Z(f) = (1/6) sum_{x in Z^3} sum_{i=1}^3
                            (f(x+e_i)-f(x))^2.          (6)

Here is a justification including the equality of the infimum, which is
needed for the lower bound in (1). Kill the walk outside a finite box U
containing K. Its Green matrix is G_U=(I-P_U)^(-1); I-P_U is positive
definite. The eigenvalues of G_U are at least 1/2. Principal submatrices
and increasing-box limits therefore show that G_K is positive definite.

For f zero outside U, expansion of the squared differences gives
E_Z(f)=f^T(I-P_U)f. Minimize this positive definite quadratic form under
f=1 on K. The minimizer f_U satisfies (I-P_U)f_U=0 off K. If
q_U=(I-P_U)f_U, solving f_U=G_U q_U on K gives minimum energy

    c_U = 1^T ((G_U)_{K,K})^(-1)1.

The killed Green functions converge entrywise to g. Since G_K is positive
definite, their inverses on K converge, so c_U tends to 1^T G_K^(-1)1.
Every finitely supported admissible f lies in some U and satisfies
E_Z(f)>=c_U>=1^T G_K^(-1)1; the second inequality also follows by
increasing U, since the admissible classes grow. Conversely the minimizers
f_U are finitely supported and their energies tend to that value. This
proves the infimum formula.

To agree with the random-walk definition, put
e_K(y)=P_y(X_n not in K for every n>=1), y in K. A transient walk visits
K only finitely many times almost surely. Decomposition by its last visit
gives G_K e_K=1. Consequently sum e_K=1^T G_K^(-1)1, as in (6).

## 3. Reverse transfer by trilinear interpolation

Let f:Z^3->R be finitely supported. On each unit cube n+[0,1]^3 define
its trilinear interpolant

    I f(n+t) = sum_{epsilon in {0,1}^3} f(n+epsilon)
                 product_{j=1}^3 w_{epsilon_j}(t_j),
    w_0(t)=1-t,    w_1(t)=t.

Adjacent formulas agree on their common faces. The interpolant is
continuous, compactly supported and Lipschitz; only finitely many cubes
have a nonzero value, and their first derivatives are bounded.

Fix a coordinate i. Inside one cube, partial_i I f is the convex
combination of the four edge increments in direction i, with weights
product_{j!=i} w_{epsilon_j}(t_j). The weights are nonnegative and sum
to one. Jensen's inequality and integration over the cube yield

    integral_{n+[0,1]^3} |partial_i I f|^2
      <= (1/4) sum_{epsilon: epsilon_i=0}
                   (f(n+epsilon+e_i)-f(n+epsilon))^2.   (7)

The derivative is independent of t_i. Each of the other two weight
integrals is 1/2, explaining the factor 1/4. On summing over n, each
oriented lattice edge in direction i belongs to exactly four cubes.
Thus

    integral_{R^3} |partial_i I f|^2
       <= sum_{x in Z^3} (f(x+e_i)-f(x))^2.

Summing over i gives

    (1/6) integral |grad I f|^2 <= E_Z(f).               (8)

If f=1 on B_R, all vertices of every unit cube inside Q_R have value
one. Hence I f=1 on Q_R, including its boundary by continuity.

Scaling y=a z in the continuum variational problem shows, in both
directions, that

    inf_{F=1 on Q_a} (1/6) integral |grad F|^2 = a kappa, (9)

with the same compact-support and Lipschitz conditions. Apply (9) with
a=R to I f, then (8), and finally take the infimum in (6). The result is

    kappa R <= cap(B_R).                                (10)

## 4. Forward transfer by cell averaging

For compactly supported Lipschitz F let

    A F(x) = integral_{[-1/2,1/2]^3} F(x+z) dz.

The cell volume is one. Absolute continuity on almost every coordinate
line and Jensen's inequality give

    |A F(x+e_i)-A F(x)|^2
      <= integral_{[-1/2,1/2]^3} integral_0^1
                    |partial_i F(x+z+u e_i)|^2 du dz.

For every fixed u the shifted cells tile R^3 up to null boundaries.
Sum over x and i, then integrate u, to obtain

    E_Z(A F) <= (1/6) integral |grad F|^2.               (11)

If F=1 on Q_{R+1/2}, then A F=1 on B_R. It is finitely supported.
Equations (6), (11), and (9) give

    cap(B_R) <= kappa (R+1/2).                          (12)

Together with (10), this proves (1)--(3). Neither transfer uses the
existence of an infinite-support minimizer. The half-cell in (12) is
needed because the cells centered at boundary vertices extend beyond Q_R.

## 5. Positivity and the preceding distance-profile bound

For every admissible F in the definition of kappa, F=1 on the unit sphere
and F vanishes outside a sufficiently large ball. For almost every unit
vector omega, Cauchy-Schwarz on a radial line gives

    1 = |integral_1^infinity partial_r F(r omega) dr|^2
      <= [integral_1^infinity r^2 |partial_r F(r omega)|^2 dr]
         [integral_1^infinity r^(-2) dr]
      = integral_1^infinity r^2 |partial_r F(r omega)|^2 dr.

Integrating over omega and using |partial_r F|<=|grad F| proves
integral |grad F|^2>=4 pi. Thus kappa>=2 pi/3.

For the upper bound let d(y) be Euclidean distance to Q_1 and put

    S(s)=24+12 pi s+4 pi s^2,
    J_T=integral_0^T ds/S(s),    J=integral_0^infinity ds/S(s).

Decomposing the exterior into six face regions, twelve edge regions and
eight corner regions gives, for F(y)=u(d(y)),

    integral |grad F|^2 = integral_0^infinity S(s) u'(s)^2 ds. (13)

The face areas contribute 24; the edges contribute
12*2*(pi/2)*s=12 pi s; the corner octants together contribute 4 pi s^2.
For finite T use

    u_T(s)=1-J_T^(-1) integral_0^s dr/S(r),  0<=s<=T;
    u_T(s)=0,                               s>=T.

Then F_T=u_T composed with d is compactly supported, Lipschitz and one
on Q_1. Equation (13) gives energy integral 1/J_T. Hence
kappa<=1/(6J). Substituting w=2s+3 gives

    J = (1/(2 pi)) integral_3^infinity dw/(w^2-delta^2)
      = log((3+delta)/(3-delta))/(4 pi delta),

so 1/(6J)=C. Here 0<delta<3, since pi>8/3.

For completeness, C<3 follows from an elementary trial profile. Use
u(s)=b/(b+s). The compactly supported profiles
v_T(s)=(u(s)-u(T))/(1-u(T)) on [0,T], extended by zero beyond T,
have energy tending to that of u, because u(T) tends to zero and
integral_0^infinity S(s)u'(s)^2 ds is finite. That energy divided by 6 is

    4/(3b)+pi/3+(2 pi b)/9.

Indeed the three integrals of (b+s)^(-4), s(b+s)^(-4), and
s^2(b+s)^(-4) over [0,infinity) are respectively
1/(3b^3), 1/(6b^2), and 1/(3b). Cauchy-Schwarz in (13) shows that
C is the infimum over distance profiles, so at b=3/2,

    C <= 8/9+2 pi/3 < 8/9+44/21 = 188/63 < 3.          (14)

## 6. A strict improvement by a face variation

The limiting profile

    u(s)=J^(-1) integral_s^infinity dr/S(r)

satisfies

    u'(s)=-1/(J S(s)),    u''(s)=S'(s)/(J S(s)^2)>0.

It is therefore not harmonic in the open face regions. A compactly
supported variation there strictly lowers its energy. The following
calculation gives an explicit bound and uses finite-T functions throughout
the variational argument.

Define the tent functions

    alpha(s)=(1-|2s-1|)_+,    beta(v)=(1-|v|)_+.

For i in {1,2,3}, sigma in {-1,1}, define

    eta_{i,sigma}(y)=alpha(sigma y_i-1) product_{j!=i} beta(y_j),
    eta=sum_{i,sigma} eta_{i,sigma}.

Each term has support in a face region with 1<=sigma y_i<=2 and
|y_j|<=1 for j!=i. Their interiors are disjoint. The function eta is
compactly supported and Lipschitz, and eta=0 on Q_1.

The one-dimensional integrals are

    integral alpha=1/2,  integral alpha^2=1/3,
    integral (alpha')^2=4;
    integral beta=1,     integral beta^2=2/3,
    integral (beta')^2=2.

Consequently each face contributes

    integral |grad eta_{i,sigma}|^2
       = 4(2/3)^2 + 2(1/3)*2*(2/3) = 8/3.

Null boundary intersections cause no cross terms. Thus

    H := integral |grad eta|^2 = 6*(8/3)=16.             (15)

On one face region d(y)=sigma y_i-1=s. Integration by parts in s,
with alpha zero at both endpoints, gives

    -integral grad(u composed with d) dot grad eta_{i,sigma}
       = integral_0^1 u''(s) alpha(s) ds.

The tangential integrals are both integral beta=1. Therefore, writing

    I := 6 integral_0^1 u''(s) alpha(s) ds,

we have I>0. On 0<=s<=1, S'(s)>=12 pi and S(s)<=D=24+16 pi. Hence

    I >= 6*[12 pi/(J D^2)]*(1/2)=36 pi/(J D^2).         (16)

For every T>1 put I_T=-integral grad F_T dot grad eta. The same
calculation gives I_T=(J/J_T)I. The admissible function
F_T+(I_T/H)eta has energy

    integral |grad(F_T+(I_T/H)eta)|^2
       = 1/J_T - I_T^2/H.

Taking T to infinity only after applying the definition of kappa yields

    kappa <= C-I^2/(6H)
           <= C - [36 pi/(J D^2)]^2/96
            = C - 486 pi^2 C^2/D^4 = C_1.               (17)

The last equality uses J^(-1)=6C. Since C>0, the decrement is positive.
Also C_1>=kappa>=2 pi/3, so there is no issue with a nonpositive upper
bound. This proves (4). The variational class does not require trial
functions to stay below one. If that convention is preferred, truncating
them to [0,1] can only lower energy and preserves the prescribed value.

## 7. Consequence for the relative one-arm radius

For a centered nondegenerate Gaussian vector X on K with covariance G_K,
let mu be its law and Q the law of X-t1. Put

    a=1^T G_K^(-1)1,    s=t sqrt(a),    L=dmu/dQ.

Under Q, log L=sZ-s^2/2 for a standard normal Z, so
E_Q L^r=exp(r(r-1)s^2/2) for r>1. For any event with probabilities
p under mu and q under Q, Holder's inequality gives

    p <= q^((r-1)/r) exp((r-1)s^2/2),
    log(q/p) >= -log(1/p)/(r-1)-r s^2/2.

For s>0 set r-1=sqrt(2 log(1/p))/s. The case s=0 follows directly.
With K=B_R and the level-h connection event, (6) gives

    p_R(h+t)/p_R(h)
       >= exp[-t sqrt(2 cap(B_R) log(1/p_R(h)))
               -t^2 cap(B_R)/2].                       (18)

The event is measurable on B_R by stopping a path at its first boundary
visit. Its probability lies strictly between zero and one by finite
Gaussian nondegeneracy.

The external input is Stephen Muirhead, *Percolation of strongly
correlated Gaussian fields II. Sharpness of the phase transition*,
[arXiv:2206.10724v2](https://arxiv.org/html/2206.10724v2), Theorems 1.2
and 1.10. In dimension three, these give theta(h_*-v)>=c_q v^q for
each q>4 at small v>0, and p_R(h_*+t)<=exp(-c_t sqrt(R)) for fixed
t>0. The excluded endpoint q=4 is not used.

Here theta is the infinite-cluster probability. Since theta(h)<=p_R(h),
take h=h_*-R^(-1/2) in (18). The quantity s is bounded by (1), and
p_R(h)>=c_q R^(-q/2). For fixed s>=0 the function

    p -> p exp[-s sqrt(2 log(1/p))-s^2/2]

is increasing on (0,1). Thus (18) gives

    log(1/p_R(h_*)) <= (q/2)log R+O_q(sqrt(log R)).

Choose q>4 sufficiently close to 4. For each epsilon>0 it follows that

    log(1/p_R(h_*)) <= (2+epsilon)log R                 (19)

for all sufficiently large R. In particular critical nonpercolation has
not been assumed.

Fix c<(log 2)^2/(8 kappa). Choose epsilon>0 with
sqrt(4 kappa c(2+epsilon))<log 2. Put H_t=log(1/t) and
M_t=c/(t^2 H_t). For small t, log M_t<=2H_t. Uniformly over sufficiently
large integers R<=M_t, (1) and (19) give

    t^2 cap(B_R) <= kappa c/H_t+kappa t^2/2,
    log(1/p_R(h_*)) <= 2(2+epsilon)H_t.

The negative logarithm of the lower bound in (18) is therefore at most

    sqrt[(kappa c/H_t+kappa t^2/2)*4(2+epsilon)H_t]
       +(kappa c/H_t+kappa t^2/2)/2,

which tends to sqrt(4 kappa c(2+epsilon))<log 2. The ratio is consequently
greater than 1/2 at every such radius. At the remaining finitely many
radii it tends to one by continuity under Gaussian translations, so the
same strict inequality holds for all integers R<=M_t when t is small.
This argument does not require the ratio to be monotone in R.

For fixed t>0 the external subcritical bound and (19), with epsilon=1,
bound the ratio by R^3 exp(-c_t sqrt(R)), tending to zero. Thus L_rel(t)
is finite. The preceding uniform estimate gives L_rel(t)>floor(M_t).
Multiply by t^2 H_t, take the liminf, and increase c to its endpoint.
This proves the first inequality in (5). The remaining inequalities in
(5) follow from (4).

## 8. Limits of the conclusion

The limit in (3) identifies a deterministic capacity coefficient. It is
not a lattice percolation exponent. Formula (17) also shows that the
previously optimized distance-profile class misses the true coefficient
by a fixed positive amount. No exact numerical value of kappa is supplied.

The logarithmic loss in (5) remains. Its coefficient is a guaranteed
lower bound for this relative radius, not an asymptotic value. Critical
nonpercolation, exponent existence and values, and agreement with cable
exponents are not proved here.
