# P0017: Gaussian posterior bridge and a refuted averaging shortcut

Author w357, 2026-10-10. Independent referee w359; adversary w358. All deductions below are author proofs awaiting their checks. No novelty or full-KLS-proof claim is made. The parent theorem is already claimed in October 2026 primary preprints.

## Exact target and source status

For every n>=1 and every full-dimensional isotropic log-concave probability measure mu on R^n, prove C_P(mu)<=C for a numerical constant C independent of n and mu. Here E X=0, Cov(X)=I, mu has density exp(-V)/Z for convex extended-real V, and C_P is defined by Var_mu f <= C_P integral |grad f|^2 dmu for locally Lipschitz square-integrable f of finite gradient energy. The covariance formulation is C_P(mu)<=C ||Cov(mu)||_op. For a general covariance matrix, the lower bound ||Cov(mu)||_op<=C_P(mu) follows by testing a linear function.

Bizeul-Klartag-Lehec, arXiv:2610.05474v1, Theorem 1.1 and equations (5)-(6), explicitly state this full target. Song-Zhang, arXiv:2610.01447v2, Theorem 1.1, also state the full target. The latter was revised 4 October 2026 from its earlier log-star bound. These are source-verified proof claims, not mathematical certifications by this worker. The September ranking's attempted_un is historical.

## Selected bridge

Let X~mu, G~N(0,I) independent, t>0, Y=X+sqrt(t)G, nu_t=Law(Y), and T_t f(y)=E[f(X)|Y=y]. Write A_y=Cov(X|Y=y), h_y=E[|grad f(X)|^2|Y=y], and D_mu(f)=E|grad f(X)|^2. Define

    Q_t(mu) = sup_f D_nu_t(T_t f)/D_mu(f),

where the supremum is over nonconstant smooth bounded test functions of finite positive energy, then over their Sobolev closure. Begin with a regular log-concave mu: its smooth potential has a I <= Hess V <= b I for some a,b>0 and polynomially growing derivatives. This guarantees all differentiations and a finite K=C_P(mu). The conditional and variance inequalities extend by approximation to the usual finite-energy class. Only the uniform strict bound Q_t<=q<1 remains unproved here.

## L1. Exact posterior and conditional bounds

Bayes' rule gives mu_y(dx) proportional to exp(-V(x)-|x-y|^2/(2t)) dx. Differentiating its normalized integral gives

    grad_y T_t f(y) = Cov_mu_y(f,X)/t.

The posterior potential has Hessian at least I/t. The classical strong-log-concavity Poincare inequality therefore gives C_P(mu_y)<=t, and applying it to a linear test gives 0<=A_y<=t I. Crucially the Hessian of the original V is only nonnegative in the general parent target; the I/t term belongs to the posterior. The source's Brownian-observation convention Y_s=sX+B_s agrees with this packet after s=1/t and division by s. Numerical t here is noise variance, not localization time.

## L2. Unweighted MMSE matrix bound

For any centered isotropic X of finite second moment, even without log-concavity,

    E_Y A_Y <= t/(1+t) I.

Proof: m(Y)=E[X|Y] minimizes mean-square prediction error. Orthogonality of X-m(Y) to every square-integrable function of Y gives the matrix identity

    E[(X-cY)(X-cY)^T] = E A_Y + E[(m(Y)-cY)(m(Y)-cY)^T].

Take c=1/(1+t). Independence of X and G and Cov(X)=I give the left matrix t/(1+t) I. The second matrix on the right is positive semidefinite. This is an additive conditional-expectation identity, not an independence claim about A_Y and another Y-dependent quantity.

## L3. Strict contraction for affine functions

For f(x)=a.x+b and isotropic log-concave mu,

    D_nu_t(T_t f) <= |a|^2/(1+t) = D_mu(f)/(1+t).

Proof: L1 gives grad T_t f=A_Y a/t. Since A_Y is positive semidefinite and A_Y<=t I, its spectral decomposition gives A_Y^2<=t A_Y. Thus E|A_Y a/t|^2 <= a^T(E A_Y)a/t <= |a|^2/(1+t), by L2. This checks only affine functions, not the supremum defining Q_t.

## L4. Conditional bridge: a strict Q_t bound implies KLS

For a log-concave mu with finite K=C_P(mu), if Q_t(mu)<=q<1, then

    K <= t(1+q)/(1-q).

Proof: independent tensorization of the Poincare inequalities for X and sqrt(t)G gives C_P(nu_t)<=K+t. Explicitly, for F(Y), use the law of total variance conditioning on G, then apply Poincare to X for the first term and Gaussian Poincare plus Jensen to G for the second term. Both gradients are gradients of F at Y, with the Gaussian term acquiring factor t.

Now condition the original f on Y:

    Var_mu f = E Var_mu_Y f + Var_nu_t(T_t f)
             <= t D_mu(f) + (K+t) D_nu_t(T_t f)
             <= [t+q(K+t)] D_mu(f).

Take the supremum over f and rearrange (1-q)K<=t(1+q). Regular isotropic measures have finite K by strong log-concavity, so a fixed t and q valid uniformly for those measures would give a numerical bound. Standard Gaussian convolution, a small quadratic tilt, and affine recentering/covariance normalization approximate arbitrary isotropic log-concave measures by regular isotropic ones. Testing compactly supported smooth functions passes a uniform Poincare bound to the limit. Hence that uniform bridge suffices for the exact parent target. This last approximation is explicitly described in arXiv:2610.05474v1, Section 2, immediately after (12).

Conversely, if KLS provides K<=C, then the same conditional covariance identity and A_Y<=t I give

    |grad T_t f|^2 <= Var_mu_Y(f)/t,
    D_nu_t(T_t f) <= Var_mu(f)/t <= (C/t) D_mu(f).

Taking t=2C gives q=1/2. Thus a uniform strict posterior Dirichlet contraction at some fixed noise level is equivalent to a uniform KLS bound, not a shortcut that has already removed its difficulty.

## L5. Gaussian special case

If mu=N(0,I), then mu_y=N(y/(1+t), t/(1+t) I). Differentiate by translating this Gaussian to obtain grad T_t f=(1/(1+t)) E[grad f(X)|Y=y]. Jensen yields Q_t(mu)<=(1+t)^(-2); linear f attains equality. Using C_P(mu_y)=t/(1+t) and C_P(nu_t)=1+t in total variance gives Var_mu f<=D_mu(f). A linear f attains equality, so C_P(mu)=1. This is a proved special case, not evidence for a general nonlinear bound.

## L6. The weighted covariance shortcut is false, even in dimension one

The tempting sufficient estimate is

    E[||A_Y||_op h_Y] <= t q E[h_Y]  for a numerical q<1.

It would imply Q_t<=q via |Cov_mu_y(f,X)|^2 <= ||A_y||_op Var_mu_y f <= t ||A_y||_op h_y. But L2 does not imply that weighted estimate. In fact no q<1 works for all f even for one fixed isotropic log-concave law.

Take the centered Laplace density p(x)=(lambda/2) exp(-lambda|x|), lambda=sqrt(2), so Var X=2/lambda^2=1. Its posterior has variance a(y)<=t. One direct proof of this bound, avoiding nonsmooth-Hessian issues, is integration by parts: with posterior mean m, 1=E[(X-m)((X-y)/t+lambda sign X)]=a(y)/t+lambda Cov(X,sign X), and the covariance is nonnegative because sign is increasing.

As y tends to positive infinity, a(y) tends to t. To prove this, put m_y=y-lambda t. Relative to N(m_y,t), the posterior density has weight w(x)=1 on x>=0 and w(x)=exp(2lambda x) on x<0. After x=m_y+z, w(m_y+z) tends to 1 and is bounded by 1. Gaussian domination proves convergence of the zeroth, first and second z moments. Consequently Var(X|Y=y) tends to t. Thus even a pointwise bound a(y)<=t q with q<1 is impossible.

For the stronger weighted refutation, choose a nonzero smooth phi supported in (0,1), and f_L(x)=integral_{-infinity}^x phi(u-L)du. This is bounded and smooth; f'_L(x)=phi(x-L). Conditional expectation and Fubini give

    E[a(Y) h_Y] = E[phi(X-L)^2 a(X+sqrt(t)G)].

Divide by t E h_Y=t E phi(X-L)^2. Since the derivative lives on X=L+s with 0<s<1, the resulting ratio equals

    integral_0^1 phi(s)^2 exp(-lambda s) E_G[a(L+s+sqrt(t)G)/t] ds
      / integral_0^1 phi(s)^2 exp(-lambda s) ds.

For each s and finite G the inner a/t tends to 1; it lies between 0 and 1. Dominated convergence makes this ratio tend to 1. Every q<1 is violated at some finite L. The isotropic Laplace law remains fixed as L varies. This refutes the weighted covariance route, not KLS and not the actual strict Dirichlet contraction criterion in L4.

## Single hardest remaining gap

Prove a uniform strict bound D_nu_t(T_t f)<=q D_mu(f) for arbitrary nonlinear f with fixed numerical t>0 and q<1. L3 establishes it only for affine functions. L6 rules out obtaining it by replacing the energy-weighted posterior covariance by the unweighted MMSE bound or by asserting a pointwise posterior variance gap. A correct argument must retain the dependence between the posterior covariance and the function's conditional energy, or control Cov_mu_Y(f,X) more sharply. The new KLS preprints may imply the criterion; this packet has not independently checked their load-bearing nonlinear steps.

NEXT: Check L4 and L6 independently with w359, measure the Laplace ratios under a small fresh compute gate, then submit the proved deductions and refuted route as DRAFT nodes.
