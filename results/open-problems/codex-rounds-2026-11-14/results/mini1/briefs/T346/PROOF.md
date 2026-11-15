# Sharp bounds for input-dependent Gaussian smoothing

## Finite-radius theorem: arbitrary covariance dependence

Fix d>=1, 2<p<=infinity, sigma>0, a in (1/2,1), and x in R^d. Let Phi be the standard normal distribution function and z=Phi^{-1}(a)>0. Consider any kernel

    P_y=N(y,Sigma(y)),    y in R^d,

where every Sigma(y) is positive definite. No continuity, differentiability, or independence is assumed. Suppose B=Sigma(x) satisfies tr B<=d sigma^2.

Define the universal majority radius at x from the probability a by

    R(P,x,a)=sup {r>=0 : for every measurable A with P_x(A)=a,
                         and every ||h||_p<r, P_{x+h}(A)>1/2}.

This definition uses open balls. In a binary classifier, A is the class-one region; probability greater than 1/2 ensures the same prediction for any tie rule. The quantifier over arbitrary A is essential.

Set

    M_p(B)=max_{||v||_p<=1} sqrt(v^T B^{-1}v).

Then

    R(P,x,a) <= z/M_p(B)
             <= sigma z d^{1/p-1/2}.                            (F1)

Both inequalities can be equalities: the constant isotropic kernel P_y=N(y,sigma^2 I) has radius exactly sigma z d^{1/p-1/2}. Thus this is the exact minimax optimum over ALL input-dependent Gaussian covariance schemes under the local trace budget. An attaining scheme must have Sigma(x)=sigma^2 I, although this condition alone need not suffice for an arbitrary field.

### Proof of the finite upper bound

The maximum defining M_p(B) exists by continuity on the compact unit ball. A maximizer v can be chosen with ||v||_p=1, since the quadratic form is positive and homogeneous. Put s=M_p(B)>0 and u=B^{-1}v/s. Then u^T B u=1 and u^T v=s. The fixed halfspace

    A={w:u^T(w-x)<=z}

has P_x(A)=Phi(z)=a. For t>0, the projection u^T(W-x), with W distributed according to P_{x+tv}, is Gaussian with mean ts and strictly positive variance

    b(t)^2=u^T Sigma(x+tv)u.

Consequently,

    P_{x+tv}(A)=Phi((z-ts)/b(t)).                                (F2)

At t=z/s this equals 1/2; at EVERY t>z/s it is strictly less than 1/2, whatever b(t)>0 is. For any r>z/s choose t with z/s<t<r. The displacement tv lies inside the ball of radius r and flips the binary majority for the halfspace classifier, whose nominal majority probability is a. Thus no r>z/s satisfies the defining property of R, proving its first upper bound.

The sign-vector calculation in Section 3 below proves M_p(B)>=d^{1/2-1/p}/sigma and its equality condition, giving the second upper bound and the necessary condition for attainment. The likelihood-ratio calculation in Section 4 below proves that a constant covariance B has exact transfer T_a(r;x)=Phi(z-r M_p(B)). Therefore its open-ball majority radius is exactly z/M_p(B). In particular constant isotropic covariance attains both bounds in (F1). These arguments prove the finite theorem without using the local theorem below.

The same finite upper-bound proof also applies when P_x is Gaussian but every other P_y is any centrally symmetric distribution about y with atomless, full-support one-dimensional projections. Under that condition a halfspace whose boundary passes through y has probability 1/2, and shifting its threshold strictly below the center gives probability below 1/2. No optimality claim for arbitrary non-Gaussian P_x is implied.

An independent geometric expression for the constant is useful. The distance in p norm from x to the hyperplane n^T(w-x)=z sqrt(n^T B n) is

    z sqrt(n^T B n) / ||n||_q,    1/p+1/q=1.

Holder gives the lower bound on this distance, and a vector maximizing the linear functional n on the compact p unit ball attains it after rescaling. Moreover,

    M_p(B)
      = max_{||v||_p<=1} max_{||w||_2<=1} w^T B^{-1/2}v
      = max_{||w||_2<=1} ||B^{-1/2}w||_q
      = max_{n!=0} ||n||_q / sqrt(n^T B n).

Here the first identity is Euclidean duality, the second exchanges maxima over two compact sets and uses p/q duality, and the last substitutes n=B^{-1/2}w and uses homogeneity. Thus the minimum halfspace-boundary distance over all normals is independently z/M_p(B), agreeing with (F1). Reflection symmetry of the endpoint kernel again gives the majority obstruction at that boundary and a strict flip just beyond it.

## Local refinement: smooth covariance dependence

Let d >= 1, 2 < p <= infinity, and sigma > 0. Put 1/p = 0 when p = infinity. Let Phi and phi be the standard normal distribution function and density. All sets below are Lebesgue measurable.

## Statement

On a neighborhood of x in R^d, consider the smoothing kernel

    P_y = N(y, Sigma(y)),

where Sigma is C1 and takes values in the symmetric positive-definite matrices. At the point x assume only

    tr Sigma(x) <= d sigma^2.                                      (1)

Thus the local expected squared Euclidean noise is at most d sigma^2. No independence assumption is imposed on its coordinates, and the covariance may vary with the input.

For a in (0,1), write z = Phi^{-1}(a), and define the worst class-probability transfer

    T_a(r;x) = inf { P_{x+h}(A) : ||h||_p <= r, P_x(A) = a }.

The set A represents one class region of an arbitrary base classifier. It remains fixed when its probability is evaluated at x+h. The infimum ranges over both A and h. Since h=0 is allowed, T_a(r;x) <= a. Define

    L_{p,a}(x) = lim_{r down to 0} [a - T_a(r;x)] / r.

The limit exists, is finite, and satisfies

    L_{p,a}(x) >= phi(z) d^{1/2 - 1/p} / sigma.                    (2)

Equality is attained by the constant isotropic kernel Sigma(y) = sigma^2 I. Consequently, the infimum of L_{p,a}(x) over all covariance fields satisfying (1) equals the right side of (2). Any attaining field must have Sigma(x) = sigma^2 I. No assertion is made that this condition alone is sufficient for an arbitrary covariance derivative.

This is a local minimax theorem for transfer of one class probability, under a noise budget. Unlike the finite theorem, it applies to every a in (0,1). A nominal probability a is not the clean accuracy on a dataset. Neither theorem imposes a relation between those two quantities.

## 1. Existence and the derivative formula

Write B = Sigma(x). Let f_y(w) be the density of P_y. On a sufficiently small closed ball around x, the eigenvalues of Sigma(y) lie between two positive constants, its first derivatives are bounded, and y is bounded. Differentiating the Gaussian density therefore gives the integrable uniform bound

    |partial_j f_y(w)| <= C (1 + ||w||_2^2) exp(-c ||w||_2^2)

for some C,c>0. For example, use ||w-y||_2^2 >= ||w||_2^2/2 - ||y||_2^2 in the Gaussian exponential. This also bounds the density after increasing C. Each partial derivative is continuous in y pointwise in w; dominated convergence makes it continuous in L1(dw).

The fundamental theorem of calculus along the segment from x to x+h now yields the L1 expansion

    f_{x+h} = f_x + Df_x[h] + R_h,
    ||R_h||_1 = o(||h||_p).                                      (3)

Indeed, the remainder norm is bounded by a constant times ||h||_p times the largest L1 variation of a first derivative on that segment. That variation tends uniformly to zero as h tends to zero. Finite dimensionality gives the comparison between coordinate norms used here.

For a direction v, let D_v = D Sigma(x)[v]. Differentiating log f_y at x gives the score

    S_v(w) = v^T B^{-1}(w-x)
           + (1/2) [(w-x)^T B^{-1} D_v B^{-1}(w-x)
                     - tr(B^{-1} D_v)].                          (4)

In particular, Df_x[v] = f_x S_v. All scores have finite first absolute moments. Equation (3) gives, uniformly over all measurable A,

    P_{x+h}(A) = P_x(A) + E_x[1_A S_h] + o(||h||_p).             (5)

The uniformity follows because the absolute error of integration over A is at most ||R_h||_1. Taking h=rv with ||v||_p <= 1 and then infima in (5) proves

    L_{p,a}(x)
      = sup_{||v||_p <= 1} sup_{A:P_x(A)=a} -E_x[1_A S_v].       (6)

To see that the error remains o(r) over the whole ball, write its bound as ||h||_p eta(||h||_p), with eta tending to zero, and replace eta by its nondecreasing envelope. The supremum in (6) is finite: (4) is linear in v, and the finitely many coordinate scores have finite first absolute moments. Sets of probability a exist since a nondegenerate Gaussian has continuous one-dimensional projections. This proves all existence claims.

## 2. Reflected halfspaces remove possible covariance cancellation

Fix v with ||v||_p = 1. Put

    s = sqrt(v^T B^{-1} v),    u = B^{-1}v / s,
    lambda = u^T D_v u.

Then s>0, u^T B u=1, and u^T v=s. Define two fixed halfspaces

    A_+ = {w :  u^T(w-x) <= z},
    A_- = {w : -u^T(w-x) <= z}.

Both have P_x-probability a. For the direction v and t near zero, their exact probabilities are

    P_{x+tv}(A_+) = Phi((z-ts) / sqrt(u^T Sigma(x+tv) u)),
    P_{x+tv}(A_-) = Phi((z+ts) / sqrt(u^T Sigma(x+tv) u)).

Since u^T Sigma(x+tv) u = 1 + t lambda + o(t), their derivatives at t=0 are respectively

    phi(z)(-s - z lambda/2),
    phi(z)( s - z lambda/2).                                    (7)

Changing the attack direction from v to -v negates either derivative, with the halfspace held fixed. Hence the four choices of halfspace and attack sign, all allowed in (6), imply

    L_{p,a}(x) >= phi(z) max(|s+z lambda/2|, |s-z lambda/2|)
               = phi(z)(s + |z lambda|/2)
               >= phi(z) s.                                    (8)

The middle identity follows by checking the two signs of the real number z lambda/2, using s>=0. The argument also applies when z=0; no division by z is used. Taking a supremum over v gives

    L_{p,a}(x) >= phi(z) M_p(B),
    M_p(B) = max_{||v||_p <= 1} sqrt(v^T B^{-1}v).                (9)

In particular, a covariance derivative cannot improve on the constant-covariance local minimax sensitivity with the same B. It can make the sensitivity larger.

## 3. The trace budget gives the dimension exponent

For a sign vector epsilon in {-1,1}^d, set v_epsilon = d^{-1/p} epsilon. This vector has p norm one, including when p=infinity. Uniform independent signs give

    M_p(B)^2 >= E_epsilon[v_epsilon^T B^{-1}v_epsilon]
              = d^{-2/p} tr(B^{-1}).                            (10)

The equality uses E[epsilon_i epsilon_j] = 0 for i!=j and 1 for i=j. If beta_1,...,beta_d are the eigenvalues of B, Cauchy-Schwarz gives

    d^2 = (sum_i sqrt(beta_i)/sqrt(beta_i))^2
         <= (sum_i beta_i)(sum_i 1/beta_i).

Consequently,

    tr(B^{-1}) >= d^2/tr(B) >= d/sigma^2,
    M_p(B) >= d^{1/2-1/p}/sigma.                                (11)

Combining (9) and (11) proves (2). Equality at the end of this chain requires equality in the eigenvalue Cauchy-Schwarz inequality and in (1). Thus all beta_i equal sigma^2, so B=sigma^2 I. This proves the asserted necessary condition on any attaining field.

## 4. Attainment and an exact finite-radius check

First consider any constant covariance B. For a fixed displacement h!=0, set s_h = sqrt(h^T B^{-1}h) and

    U(w) = h^T B^{-1}(w-x)/s_h.

Under P_x, U is standard normal. The likelihood ratio is

    f_{x+h}(w)/f_x(w) = exp(s_h U(w) - s_h^2/2),

which increases with U. Among sets of P_x-probability a, the set A_0={U<=z} minimizes P_{x+h}(A). To verify this directly, let c=exp(s_h z-s_h^2/2), and integrate

    (1_A - 1_{A_0})(f_{x+h}/f_x - c) >= 0

against P_x. The inequality holds pointwise: outside A_0 both factors are nonnegative, and inside A_0 both are nonpositive. The term involving c integrates to zero because P_x(A)=P_x(A_0). Thus P_{x+h}(A)>=P_{x+h}(A_0). Under P_{x+h}, U has distribution N(s_h,1), giving

    inf_{A:P_x(A)=a} P_{x+h}(A) = Phi(z-s_h).

For h=0 the same formula holds with s_h=0. Homogeneity and monotonicity of Phi now give the exact expression

    T_a(r;x) = Phi(z-r M_p(B))                                  (12)

for constant covariance. Differentiating at zero proves L_{p,a}=phi(z)M_p(B).

For B=sigma^2 I, Holder's inequality gives

    ||v||_2 <= d^{1/2-1/p} ||v||_p,

with equality at v=d^{-1/p}(1,...,1). For finite p this follows by applying Holder to sum |v_i|^2, with exponents p/2 and p/(p-2); for infinity it is sum |v_i|^2<=d||v||_infinity^2. Therefore M_p(B)=d^{1/2-1/p}/sigma. Equations (12) and (2) establish the claimed sharp minimax value.

As a finite-radius consequence confined to constant Gaussian covariance and a>1/2, the supremum radius certified from the single class probability a against every base classifier is

    R_p(B,a) = z/M_p(B).

Predictions remain strictly above probability 1/2 for all radii smaller than R_p(B,a); at the boundary a halfspace has probability 1/2 and may tie. Under (1), the largest such radius over constant Gaussian covariances is exactly

    sigma Phi^{-1}(a) d^{1/p-1/2},

attained uniquely in covariance by B=sigma^2 I. The upper bound extends to arbitrary variable covariance by the halfspace argument (F2); attainment here uses constant covariance.

## 5. Independent derivations of the two key steps

For (7), one can instead integrate the score (4). Put Z=B^{-1/2}(w-x), b=B^{-1/2}v, e=b/||b||_2, H=B^{-1/2}D_v B^{-1/2}, and T=e^T Z. Then ||b||_2=s and e^T H e=lambda. Orthogonal Gaussian coordinates are independent, so conditioning on T gives

    E[S_v | T] = s T + (lambda/2)(T^2-1).

Using phi'(t)=-t phi(t), integration gives

    E[T 1_{T<=z}] = -phi(z),
    E[(T^2-1) 1_{T<=z}] = -z phi(z).

For T>=-z the corresponding values are phi(z) and -z phi(z). These yield exactly both derivatives in (7). This derivation does not differentiate the halfspace CDF.

There is also a second route to (11) which does not average inverse quadratic forms. Sign averaging gives E[epsilon^T B epsilon]=tr B, so some epsilon obeys epsilon^T B epsilon<=d sigma^2. Matrix Cauchy-Schwarz applied to B^{1/2}epsilon and B^{-1/2}epsilon gives

    (epsilon^T B epsilon)(epsilon^T B^{-1}epsilon)
       >= (epsilon^T epsilon)^2 = d^2.

For this same sign vector, v=d^{-1/p}epsilon has norm one and

    v^T B^{-1}v >= d^{1-2/p}/sigma^2,

again proving (11).

## Scope and relation to the original question

The finite theorem includes arbitrary correlations and arbitrary input-dependent covariance, including nonsmooth choices. It uses a fixed local second-moment budget and a universal quantifier over class regions. It does not optimize non-Gaussian nominal kernels, singular covariances, changes to the mean y, classifier-specific information, or an accuracy constraint imposed only on a dataset. The local refinement gives no uniform control of its Taylor remainder as d grows; the finite theorem instead uses the exact halfspace identity (F2).

Fixed clean accuracy alone does not specify a universal radius optimization problem: a constant-label data distribution admits a constant classifier with accuracy one and infinite actual robustness, while rescaling a nontrivial dataset changes distances without changing clean accuracy. A data model, scale or noise budget, and the information available to the certificate must be specified. The budget and universal transfer formulation above supply one precise special case.

The global dimension exponent is already present in the literature. Avrim Blum, Travis Dick, Naren Manoj, and Hongyang Zhang, *Random Smoothing Might be Unable to Certify l_infinity Robustness for High-Dimensional Images*, [arXiv:2002.03517](https://arxiv.org/abs/2002.03517), prove a moment barrier for arbitrary additive noise. Greg Yang, Tony Duan, J. Edward Hu, Hadi Salman, Ilya Razenshteyn, and Jerry Li, *Randomized Smoothing of All Shapes and Sizes*, [arXiv:2002.08118](https://arxiv.org/abs/2002.08118), Theorem 7.3 and Corollary 7.4, allow general families of smoothing distributions under their useful-smoothing assumptions. The results proved here give a Gaussian special case with exact constants and explicit input-dependence quantifiers; no literature-priority claim is made.
