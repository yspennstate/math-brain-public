# A capacity comparison for lattice critical one-arm probabilities

Let P be the transition matrix of simple random walk on Z^3, and normalize
the Gaussian free field by

    E[phi_x phi_y] = g(x,y) = sum_{n >= 0} P^n(x,y).

Write B_R = {x : |x|_infinity <= R} and boundary B_R = {x : |x|_infinity = R},
where R is a positive integer. All connections below are nearest-neighbor
lattice connections. Define

    p_R(h) = P(0 connects to boundary B_R in {phi >= h}),
    theta(h) = P(0 connects to infinity in {phi >= h}).

A path to boundary B_R can be stopped at its first visit there. Thus p_R(h)
depends only on the field on B_R, even if paths are initially allowed to
leave B_R. In particular theta(h) <= p_R(h).

Let Phi and varphi denote the standard normal distribution function and
density. The constant C below is 28/3.

## Statements

For every R >= 1, h in R and t >= 0,

    Phi(Phi^{-1}(p_R(h)) - t sqrt(cap(B_R)))
        <= p_R(h+t) <= p_R(h),                         (1)

and

    cap(B_R) <= (28 R - 1/R)/3 <= C R.                  (2)

Consequently:

1. If theta(h_* - t) = t^{beta+o(1)} with finite beta >= 0 and
   p_R(h_*) = R^{-rho+o(1)} with finite rho >= 0, then beta >= 2 rho.
   Neither existence assumption is asserted.
2. Using the existing density theorem specified below, for every epsilon > 0
   there is R_epsilon such that

       p_R(h_*) >= R^{-2-epsilon},  R >= R_epsilon.     (3)

   In particular limsup [-log p_R(h_*)]/log R <= 2, whether or not a one-arm
   exponent exists. This is a consequence of existing density information
   and (1), not a claim of a new exact critical exponent.
3. Define a relative one-arm crossover radius by

       L_rel(t) = min{R >= 1 : p_R(h_*+t) <= p_R(h_*)/2}.

   The minimum exists for t > 0. For some c > 0 and all sufficiently small t,

       L_rel(t) >= c t^{-2}/log(1/t).                   (4)

   If L_rel(t) = t^{-nu_rel+o(1)}, then nu_rel >= 2. This definition does not
   identify L_rel with a correlation length defined by a two-point decay rate
   or by box crossings.

## 1. Capacity and its normalization

For finite nonempty K let G_K = (g(x,y))_{x,y in K}. Define

    e_K(x) = P_x(X_n not in K for every integer n >= 1), x in K.

Transience implies that the number of visits to K is finite almost surely:
its expectation is sum_{y in K} g(x,y), which is finite. Starting at x in K,
partition trajectories by the time n and position y of the last visit to K.
The Markov property gives

    1 = sum_{y in K} sum_{n >= 0} P_x(X_n=y) e_K(y).

Therefore G_K e_K = 1, and

    cap(K) := sum_{x in K} e_K(x) = 1^T G_K^{-1} 1.    (5)

Here is also a finite-volume justification of invertibility and the energy
bound needed below. For a finite box U containing K, kill the walk when it
leaves U. Its Green matrix is G_U = (I-P_U)^{-1}. The symmetric matrix
Q_U = I-P_U is positive definite: a finite killed walk exits almost surely,
so the spectral radius of P_U is less than one. Its eigenvalues are at most
2, hence G_U >= (1/2)I as quadratic forms. The same lower bound holds for
principal submatrices and their limits. Monotone convergence of killed
Green functions gives (G_U)_{K,K} -> G_K as U increases to Z^3; G_K is thus
positive definite and inversion is continuous in this limit.

For finitely supported f, extended by zero outside U, its Dirichlet energy is

    E(f) = f^T Q_U f
         = (1/6) sum_{unordered nearest-neighbor edges {x,y}}
                        (f(x)-f(y))^2.                (6)

To check the factor, the ordered-edge sum has coefficient 1/12; each
unordered edge occurs twice. Equivalently the squared terms in (6) sum to
sum_x f(x)^2 - (1/3) sum_{unordered {x,y}} f(x)f(y), which is f^T(I-P)f.

Minimize f^T Q_U f subject to f=1 on K. Strict convexity gives a unique
minimizer f_0. Its Euler equations say Q_U f_0 vanishes outside K. Write
Q_U f_0 = q, extending q by zero away from K. Then

    f_0 = G_U q,
    q|_K = ((G_U)_{K,K})^{-1} 1,
    E(f_0) = f_0^T q = 1^T ((G_U)_{K,K})^{-1} 1.

The last expression is at most E(f) for every finitely supported f equal
to one on K and supported inside U. Letting U increase to Z^3 proves

    cap(K) <= E(f) whenever f is finitely supported and f|_K=1. (7)

Set f_R(x)=1 on B_R, f_R(x)=(2R-|x|_infinity)/R when
R < |x|_infinity < 2R, and f_R(x)=0 when |x|_infinity >= 2R.
Nonzero differences occur exactly across shells k and k+1 for
k=R,...,2R-1. There are 6(2k+1)^2 such edges: choose one of six outward
coordinate directions, then the other two coordinates in [-k,k]. Each
edge has squared difference R^{-2}. Therefore

    E(f_R) = R^{-2} sum_{k=R}^{2R-1} (2k+1)^2
           = (28 R - 1/R)/3.                           (8)

For the last equality use sum_{k=0}^{n-1}(2k+1)^2 = n(4n^2-1)/3 at n=2R
and n=R. Equations (7) and (8) prove (2).

## 2. Gaussian comparison by the score

Consider a centered Gaussian vector X with positive definite covariance G
on a finite set K. Put a = 1^T G^{-1}1 and let A be a measurable increasing
subset of R^K. Write p(h)=P(X-h1 in A). For a nontrivial event, p(h) is
strictly between zero and one. Differentiating the Gaussian density of
X-h1 under the integral gives

    p'(h) = -E[1_{X-h1 in A} 1^T G^{-1}X].             (9)

This differentiation is valid locally uniformly in h, since the derivative
is a linear polynomial times a Gaussian density, with an integrable
Gaussian majorant on every bounded h-interval. Higher derivatives exist
by the same argument. Let Z = 1^T G^{-1}X/sqrt(a); it is standard normal.

For any event D of probability p, put b=Phi^{-1}(1-p) and H={Z>=b}.
Pointwise (Z-b)(1_D-1_H) <= 0. Since P(D)=P(H), integration implies

    E[Z 1_D] <= E[Z 1_H] = varphi(b).

Applying the same upper bound to D's complement and using E Z=0 proves
E[Z 1_D] >= -varphi(b). Thus

    |p'(h)| <= sqrt(a) varphi(Phi^{-1}(p(h))).

The chain rule and monotonicity now give

    -sqrt(a) <= d/dh Phi^{-1}(p(h)) <= 0.

Integrate from h to h+t, then apply Phi. For the increasing connection
event on K=B_R and covariance G_K, (5) yields (1).

## 3. Independent check by a likelihood ratio

Keep the notation of section 2 and fix D={X-h1 in A} under the centered
Gaussian law mu. The law of X-t1 has density

    w(X) = exp(-t sqrt(a) Z - t^2 a/2)

with respect to mu. Thus p(h+t)=E_mu[1_D w]. Write s=t sqrt(a).
For s>0, w is decreasing in Z. Among all events of mu-probability p(h),
the event H={Z >= b}, b=Phi^{-1}(1-p(h)), minimizes this integral.
Indeed (1_D-1_H)(w-w(b)) >= 0 pointwise and the constant w(b) cancels on
integration. Direct one-dimensional integration gives

    E_mu[1_H w]
      = integral_b^infinity varphi(z) exp(-s z-s^2/2) dz
      = 1-Phi(b+s)
      = Phi(Phi^{-1}(p(h))-s).

This recovers the lower bound of (1) with the same sign and coefficient;
s=0 is immediate. Equality is attained for half-space events
{1^T G^{-1}X >= u}. For a lattice Green matrix G_K these events are
increasing, since G_K^{-1}1=e_K has nonnegative entries. Therefore the
coefficient sqrt(cap(K)) cannot be uniformly improved over all increasing
events measurable on K. This optimality assertion does not say that the
connection event itself attains equality.

## 4. A normal-tail bound with explicit loss

For 0<p<=1/2 let b=-Phi^{-1}(p)>=0 and Q(b)=1-Phi(b). For s>=0,

    Q(b+s)/Q(b)
      = exp(-s^2/2) E[exp(-s Z) | Z>=b]
      >= exp(-s^2/2 - s lambda(b)),                    (10)

by Jensen's inequality, where lambda(b)=varphi(b)/Q(b) is the conditional
mean E[Z|Z>=b]. Integration by parts, for b>0, gives

    Q(b) = varphi(b)/b - integral_b^infinity varphi(u)/u^2 du
         >= varphi(b)/b - Q(b)/b^2.

Hence lambda(b)<=b+1/b when b>0. If b>=1 this is at most b+1.
Also lambda'(b)=lambda(b)(lambda(b)-b)>0, since the conditional mean is
strictly greater than b. For 0<=b<=1 it follows that
lambda(b)<=lambda(1)<=2. Thus lambda(b)<=b+2 for all b>=0.

The Gaussian exponential-moment bound gives Q(b)<=exp(-b^2/2): apply
Markov's inequality to exp(bZ), whose expectation is exp(b^2/2).
Consequently b<=sqrt(2 log(1/p)). Combining these observations with (10),

    Phi(Phi^{-1}(p)-s)
      >= p exp[-s^2/2 - s(sqrt(2 log(1/p))+2)].         (11)

## 5. Density-to-arm reduction and the conditional exponent constraint

Apply (1) at h=h_*-t and use theta(h_*-t)<=p_R(h_*-t). Since
p -> Phi(Phi^{-1}(p)-s) is increasing, (2) gives the finite-scale reduction

    p_R(h_*) >= Phi(Phi^{-1}(theta(h_*-t))-t sqrt(CR)). (12)

Suppose first that theta(h_*-t)=t^{beta+o(1)} with finite beta>=0.
Fix eta>0. For sufficiently small t,
theta(h_*-t)>=t^{beta+eta}. Take t=R^{-1/2}; then s=t sqrt(CR)=sqrt(C).
Apply (11) to p=R^{-(beta+eta)/2}, which is <=1/2 for large R. Equation
(12) implies

    -log p_R(h_*)
      <= ((beta+eta)/2) log R
         + sqrt(C) sqrt((beta+eta) log R) + C/2 + 2 sqrt(C).

Divide by log R, take limsup, and then let eta decrease to zero. This proves

    limsup_{R->infinity} [-log p_R(h_*)]/log R <= beta/2. (13)

If rho exists, (13) is rho<=beta/2. This argument includes beta=0 and
does not assume theta(h_*)=0.

For an unconditional conclusion use Stephen Muirhead, *Percolation of
strongly correlated Gaussian fields II. Sharpness of the phase transition*,
[arXiv:2206.10724v2](https://arxiv.org/html/2206.10724v2), Theorems 1.2(2)
and 1.10. With ell=-h and ell_c=-h_*, they imply: for every q>4 there
are c_q>0 and t_q>0 such that

    theta(h_*-t) >= c_q t^q,  0<t<t_q.                (14)

Use p=c_q R^{-q/2} in (11) and t=R^{-1/2} in (12). For large R,

    -log p_R(h_*) <= (q/2) log R + O_q(sqrt(log R)).    (15)

Constants depend on c_q and q. For any epsilon>0 choose q=4+epsilon;
the error in (15) is at most (epsilon/2) log R eventually. This proves
(3), including its absence of an unspecified multiplicative constant once
R_epsilon is enlarged.

## 6. The relative crossover radius

By (3) with epsilon=1 there is R_0>=2 such that

    p_R(h_*) >= R^{-3},  R>=R_0.                      (16)

The positive critical level supplied in the problem implies
p_R(h_*) <= P(phi_0>=h_*) < 1/2. Apply (1) and (11) with
p=p_R(h_*), s=t sqrt(CR), and then (16). For R>=R_0,

    p_R(h_*+t)/p_R(h_*)
      >= exp[-Ct^2R/2 - t sqrt(CR)(sqrt(6 log R)+2)]. (17)

Put H=log(1/t). Choose c_0=10^{-6}/C. When t is sufficiently small and

    R_0 <= R <= c_0 t^{-2}/H,

we have log R<=2H and t sqrt(CR)<=sqrt(C c_0/H). Therefore the negative
logarithm of the right side of (17) is at most

    C c_0/(2H) + sqrt(12 C c_0) + 2 sqrt(C c_0/H),

which tends to sqrt(12)*10^{-3}<1/2<log 2. For the elementary last
inequality, log 2=integral_1^2 du/u>1/2. Thus the ratio in (17) is
strictly greater than 1/2 for every R in this range and sufficiently small t.
For the finitely many 1<=R<R_0, continuity of p_R and p_R(h_*)>0 make the
ratio greater than 1/2 as well, after decreasing t's upper bound.

It follows that L_rel(t)>floor(c_0 t^{-2}/H). Since this last quantity
tends to infinity, (4) follows, for example with c=c_0/2.

Finally L_rel(t) is finite: Theorems 1.2(1) and 1.10 of the same paper
give p_R(h_*+t)<=exp(-c_t R^{1/2}) for each fixed t>0. Together with (16)
this makes p_R(h_*+t)/p_R(h_*) tend to zero. No monotonicity in R of this
ratio is needed to define or bound its first crossing of 1/2. Taking
logarithms in (4) gives

    liminf_{t downarrow 0} log L_rel(t)/log(1/t) >= 2,

because log log(1/t)/log(1/t) tends to zero.

## Scope

The comparison uses only lattice Gaussian marginals and lattice paths.
It neither imports cable sign-cluster identities nor determines rho, beta,
or the existence of either exponent. The logarithmic loss in (4) comes from
the normal-tail factor sqrt(log(1/p_R(h_*))) in (11). Removing that loss by
this argument would require additional control of the connection event.
No equality with cable exponents, critical nonpercolation, or correlation-
length exponent for another definition is proved here.
