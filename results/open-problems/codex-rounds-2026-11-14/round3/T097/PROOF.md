# An optimized shell bound for lattice capacity and the relative crossover radius

The covariance throughout is the simple-random-walk Green function on
Z^3,

    g(x,y) = sum_{n>=0} P_x(X_n=y).

Set B_R={x: |x|_infinity<=R} for integers R>=1 and define lattice connection
probabilities

    p_R(h) = P(0 connects to boundary B_R in {phi>=h}),
    theta(h) = P(0 connects to infinity in {phi>=h}).

Paths are nearest-neighbor paths. Stopping at the first boundary visit shows
that p_R(h) is measurable on B_R. Let Phi and varphi be the standard normal
distribution function and density, and Q=1-Phi. All logarithms are natural.

## 1. Statements

Write

    S_R = sum_{k=R}^infinity (2k+1)^(-2),   A_R = 1/S_R.

Then

    cap(B_R) <= A_R <= 4R + 1/(3R).                         (1)

Here A_R is exactly the infimum of the Dirichlet energy over finitely
supported functions equal to one on B_R and constant on each sup-norm shell.
In particular,

    A_R = 4R + 1/(3R) + O(R^(-3)).                         (2)

The optimality assertion concerns this restricted class of test functions;
it is not an assertion that cap(B_R)=A_R.

For every h in R and t>=0,

    p_R(h+t) >= Phi(Phi^(-1)(p_R(h)) - t sqrt(A_R)).        (3)

Define, as in the earlier report,

    L_rel(t) = min{R>=1: p_R(h_*+t)<=p_R(h_*)/2}.

Using the density input in section 5, this minimum is finite for every t>0,
and

    liminf_{t downarrow 0} t^2 log(1/t) L_rel(t)
        >= (log 2)^2/32.                                 (4)

No existence or value of a lattice critical exponent is asserted.

## 2. Capacity normalization and the energy bound

For finite nonempty K let G_K=(g(x,y))_{x,y in K} and

    e_K(x) = P_x(X_n not in K for all n>=1), x in K.

Since the walk is transient, it visits finite K only finitely many times
almost surely. Partition by the last visit to K and apply the Markov
property to obtain G_K e_K=1. The matrix G_K is positive definite: in a
finite box U, the killed Green matrix is (I-P_U)^(-1), whose eigenvalues
are at least 1/2. Its principal submatrix on K converges to G_K as U
increases, preserving this lower bound. Therefore

    cap(K) := sum_{x in K} e_K(x) = 1^T G_K^(-1)1.        (5)

The energy of a finitely supported real function f is

    E(f) = (1/6) sum_{unordered edges {x,y}}(f(x)-f(y))^2.

The factor 1/6 gives E(f)=f^T(I-P)f. In a finite box U containing the
support of f, minimize this quadratic form subject to f=1 on K. The
Euler equations for the unique minimizer f_0 give (I-P_U)f_0=0 off K.
If q=(I-P_U)f_0, then q is supported on K and

    q|_K = ((G_U)_{K,K})^(-1)1,
    E(f_0) = 1^T ((G_U)_{K,K})^(-1)1.

This is at most E(f). Let U increase to Z^3; convergence of the Green
matrices and their inverses gives

    cap(K) <= E(f) whenever f is finitely supported and f|_K=1. (6)

## 3. Exact optimization over sup-norm shells

Fix an integer N>R. Write f(x)=u_k when |x|_infinity=k, put u_k=1 for
k<=R and u_k=0 for k>=N, and let d_k=u_k-u_{k+1}. Edges that stay in the
same shell contribute zero. Between shells k and k+1 there are exactly
6(2k+1)^2 edges: choose one of the six outward coordinate directions and
then the other two coordinates in [-k,k]. Consequently

    E(f) = sum_{k=R}^{N-1} (2k+1)^2 d_k^2,
    sum_{k=R}^{N-1} d_k = 1.                             (7)

Cauchy-Schwarz yields

    1 <= E(f) sum_{k=R}^{N-1}(2k+1)^(-2).

Equality holds precisely when

    d_k = (2k+1)^(-2) / S_{R,N},
    S_{R,N} = sum_{j=R}^{N-1}(2j+1)^(-2).

These differences give a valid finitely supported f, and its energy is
1/S_{R,N}. Thus the infimum over all such functions and all N is

    inf_N 1/S_{R,N} = 1/S_R = A_R.                       (8)

Applying (6) for each N and taking N to infinity proves cap(B_R)<=A_R.
The argument allows arbitrary real shell values; monotonicity of the trial
function was not an extra constraint. The optimizer for fixed N happens
to be decreasing and between zero and one.

For an explicit upper bound, put F(k)=3k/(12k^2+1). Direct subtraction gives

    (2k+1)^(-2) - (F(k)-F(k+1))
      = 16 / [(2k+1)^2(12k^2+1)(12(k+1)^2+1)] > 0.       (9)

Sum from k=R to infinity; F(k) tends to zero. Hence

    S_R >= F(R) = 3R/(12R^2+1),
    A_R <= 4R + 1/(3R),

which completes (1). Also

    (2k+1)^(-2) < 1/[4k(k+1)]

for k>=1. Telescoping shows S_R<1/(4R), so A_R>4R.

To verify the correction term in (2), denote the positive right side of
(9) by D_k. For k>=1 its denominator is at least
4k^2 times 12k^2 times 12k^2, so D_k<=1/(36k^6). Therefore

    0 <= S_R-F(R)
      <= (1/36)[R^(-6) + integral_R^infinity x^(-6) dx]
      = O(R^(-5)).                                      (10)

Since S_R>=F(R) and F(R)>=3/(13R) for R>=1,

    0 <= 1/F(R)-1/S_R
       = (S_R-F(R))/(F(R)S_R) = O(R^(-3)).               (11)

Now 1/F(R)=4R+1/(3R), proving (2), including the coefficient 1/3.

## 4. Gaussian comparison and its normal-tail loss

For completeness, consider X with centered nondegenerate Gaussian law mu
and covariance G on a finite index set. Put a=1^T G^(-1)1 and
Z=1^T G^(-1)X/sqrt(a), which is standard normal. The law of X-t1 has
density

    w(X)=exp(-sZ-s^2/2),   s=t sqrt(a),

relative to mu. If D is any event of probability p and b=Phi^(-1)(1-p),
let H={Z>=b}. Since w is decreasing in Z,

    (1_D-1_H)(w-w(b)) >= 0.

The constant w(b) integrates to zero in this difference, since D and H
have the same probability. It follows that

    E_mu[1_D w] >= E_mu[1_H w]
      = integral_b^infinity varphi(z) exp(-sz-s^2/2) dz
      = Q(b+s) = Phi(Phi^(-1)(p)-s).                     (12)

Take D={X-h1 belongs to the level-zero connection event} and G=G_{B_R}.
Equations (5), (12) and cap(B_R)<=A_R give (3).

For later use suppose 0<p<=1/2 and b=-Phi^(-1)(p)>=0. Changing variables
in the Gaussian integral and applying Jensen's inequality gives

    Q(b+s)/Q(b)
      = exp(-s^2/2) E[exp(-sZ)|Z>=b]
      >= exp(-s^2/2-s lambda(b)),
    lambda(b)=varphi(b)/Q(b).                            (13)

For b>0, integration by parts gives

    Q(b) = varphi(b)/b - integral_b^infinity varphi(u)/u^2 du
         >= varphi(b)/b - Q(b)/b^2,

so lambda(b)<=b+1/b. Also lambda'(b)=lambda(b)(lambda(b)-b)>0, since
lambda(b) is the conditional mean of Z above b. Thus lambda(b)<=2 for
0<=b<=1, and lambda(b)<=b+1 for b>=1. In particular lambda(b)<=b+2.
The exponential-moment bound Q(b)<=exp(-b^2/2) gives
b<=sqrt(2 log(1/p)). Consequently (12) implies

    p_R(h+t)/p_R(h)
      >= exp[-s^2/2-s(sqrt(2 log(1/p_R(h)))+2)]           (14)

whenever p_R(h)<=1/2 and s=t sqrt(A_R). The event has probability strictly
between zero and one, since it depends on finitely many nondegenerate
Gaussian coordinates.

## 5. The existing density input and critical arm bound

Stephen Muirhead, *Percolation of strongly correlated Gaussian fields II.
Sharpness of the phase transition*,
[arXiv:2206.10724v2](https://arxiv.org/html/2206.10724v2), Theorems 1.2
and 1.10, gives in this normalization:

    for every q>4, theta(h_*-t)>=c_q t^q for small t>0;  (15)
    for fixed t>0, p_R(h_*+t)<=exp(-c_t R^(1/2)).        (16)

These follow by taking ell=-h, d=3, alpha=1, and respectively gamma=1/q
and gamma=1/2. In particular gamma=1/4 is excluded in the density theorem.

Here is the critical arm consequence needed below, without any exponent
existence assumption. In (3) take h=h_*-u, u=R^(-1/2), and use
p_R(h_*-u)>=theta(h_*-u). The displacement u sqrt(A_R) is bounded by
sqrt(13/3) for R>=1, using (1). Apply (13) with p=c_q R^(-q/2), for
large R when this is at most 1/2. The result is

    -log p_R(h_*) <= (q/2)log R + O_q(sqrt(log R)).       (17)

For every epsilon>0 choose q=4+epsilon and enlarge R to absorb the error.
It follows that

    p_R(h_*) >= R^(-(2+epsilon)) for all sufficiently large R. (18)

This also independently verifies the earlier report's unconditional arm
bound. The inequality theta(h_*-u)<=p_R(h_*-u), bounded displacement,
and normal-tail estimate likewise give rho<=beta/2 if the two exponents
exist, as asserted in that report.

## 6. An explicit asymptotic coefficient for L_rel

The given fact h_*>0 implies

    p_R(h_*) <= P(phi_0>=h_*) < 1/2.

Fix a positive number c<(log 2)^2/32. Choose epsilon>0 sufficiently small
that

    4 sqrt(c(2+epsilon)) < log 2.                        (19)

Let R_epsilon be large enough for (18). Write H=log(1/t) and
M(t)=c/(t^2 H). For all sufficiently small t, M(t)>=R_epsilon and
log M(t)<=2H. For every integer R in [R_epsilon,M(t)], (1) gives

    s_R^2 = t^2 A_R <= 4c/H + t^2/(3R_epsilon),
    log(1/p_R(h_*)) <= (2+epsilon) log R
                    <= 2(2+epsilon)H.                  (20)

The negative logarithm of the lower bound in (14) is therefore at most

    (4c/H+t^2/(3R_epsilon))/2
    + sqrt(4c/H+t^2/(3R_epsilon))
        [sqrt(4(2+epsilon)H)+2].                        (21)

This expression converges to 4 sqrt(c(2+epsilon)), since H tends to
infinity and t^2 H tends to zero. By (19) it is strictly less than log 2
for every sufficiently small t, uniformly in all the indicated R. Thus

    p_R(h_*+t)/p_R(h_*) > 1/2,  R_epsilon<=R<=M(t).     (22)

For the finitely many R<R_epsilon the ratio tends to one by continuity
of finite-dimensional Gaussian event probabilities; all denominators are
positive. After reducing t further, (22) holds there as well. Consequently
L_rel(t)>floor(M(t)), so

    liminf_{t downarrow 0} t^2 H L_rel(t) >= c.

Let c increase to (log 2)^2/32 to obtain (4). There is no assertion at
the endpoint for each individual t. No monotonicity of the probability
ratio as a function of R was used: every radius below M(t) was checked.

Finally, L_rel(t) is finite. For fixed t>0, (16) and (18) with epsilon=1
give

    p_R(h_*+t)/p_R(h_*) <= R^3 exp(-c_t R^(1/2)) -> 0.

## 7. Scope of the refinement

The linear capacity coefficient is improved from 28/3 to 4 within the
comparison method, with an explicit finite-R remainder and an exact
restricted variational characterization. The coefficient in (4) is a
lower bound, not a measured or conjectured asymptotic value. Neither the
true capacity coefficient for the cube nor optimality of (4) is claimed.
This relative one-arm radius is not identified with a correlation length
defined by two-point decay or box crossings. No critical nonpercolation,
critical exponent existence, or equality with cable-system exponents is
proved.
